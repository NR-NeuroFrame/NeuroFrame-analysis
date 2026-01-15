import numpy as np

from matplotlib import pyplot as plt
from scipy.ndimage import distance_transform_edt, label

from ..logger import logger

from .overlap import get_local_skull



def get_holes(ct: np.ndarray, brain_mask: np.ndarray):
    # 1. Get the local skull
    skull = get_local_skull(ct, brain_mask)

    target_slice = (slice(None), slice(None), skull.shape[2]//2+20)
    plt.figure()
    plt.imshow(skull[target_slice])
    plt.title("Local Skull")
    plt.show(block=False)

    # 2. Fill the skull (skull space)
    skull_space = get_skull_space(skull, brain_mask)
    plt.figure()
    plt.imshow(skull_space[target_slice])
    plt.title("Skull Space")
    plt.show(block=False)

    # 3. Get all that is not skull, brain and is inside the skull space
    intersection = np.where(skull + brain_mask > 0, 1, 0)

    plt.figure()
    plt.imshow(intersection[target_slice])
    plt.title("Intersection")
    plt.show(block=False)

    possible_holes = np.where(skull_space != intersection, 1, 0)

    plt.figure()
    plt.imshow(possible_holes[target_slice])
    plt.title("Possible Holes")
    plt.show(block=False)

    # 4. Get the connected clusters
    lab, n = label(possible_holes)
    if n == 0: logger.critical("No clusters were found! cannot get skull space")
    print(n)
    lab = np.where(lab == 1, 0, lab)

    """
    sizes = np.bincount(lab.ravel())          # sizes[label_id]
    keep = sizes >= 1
    keep[0] = False                           # never keep background

    filtered = keep[lab]                      # boolean mask of kept components
    lab = lab * filtered

    n = len(np.unique(lab))
    print(n)
    """

    hole_space = np.nansum(np.where(lab > 0, 1, 0))
    print(f"The space in between brain and skull is : {hole_space} voxels")

    plt.figure()
    plt.imshow(skull[target_slice], cmap="gray", alpha=0.2)
    plt.imshow(np.where(lab[target_slice] == 0, np.nan, lab[target_slice]), cmap="hsv")
    plt.title("All Clusters")
    plt.show(block=False)

    target_slice = (slice(None), slice(None), skull.shape[2]//2)
    plt.figure()
    plt.imshow(skull[target_slice], cmap="gray", alpha=0.2)
    plt.imshow(np.where(lab[target_slice] == 0, np.nan, lab[target_slice]), cmap="hsv")
    plt.title("All Clusters")
    plt.show(block=False)

    target_slice = (skull.shape[0]//2, slice(None), slice(None))
    plt.figure()
    plt.imshow(skull[target_slice], cmap="gray", alpha=0.2)
    plt.imshow(np.where(lab[target_slice] == 0, np.nan, lab[target_slice]), cmap="hsv")
    plt.title("All Clusters")
    plt.show(block=False)

    target_slice = (slice(None), skull.shape[1]//2, slice(None))
    plt.figure()
    plt.imshow(skull[target_slice], cmap="gray", alpha=0.2)
    plt.imshow(np.where(lab[target_slice] == 0, np.nan, lab[target_slice]), cmap="hsv")
    plt.title("All Clusters")
    plt.show(block=True)

    # 5. Count them and their size (maybe use a dataclass)
    pass

def get_skull_space(skull: np.ndarray, brain_mask: np.ndarray) -> np.ndarray:
    # 1. Enlarge the brain mask
    brain_mask = np.asanyarray(brain_mask, dtype=bool)
    large_brain_mask = distance_transform_edt(~brain_mask) <= 10

    return large_brain_mask

    # 2. Subtract the skull to the enlarged brain mask
    cluster_skull_zone = np.where(large_brain_mask - skull > 0, 1, 0)

    # 3. Get the biggest connected component (skull space)
    incomplete_skull_space = get_biggest_group(cluster_skull_zone)

    # 4. Merge the incomplete skull space with skull again
    closed_skull = np.where(incomplete_skull_space + skull > 0, 1, 0)

    target_slice = (slice(None), slice(None), closed_skull.shape[2]//2)
    plt.figure()
    plt.imshow(cluster_skull_zone[target_slice])
    plt.show(block=False)

    plt.figure()
    plt.imshow(incomplete_skull_space[target_slice])
    plt.show(block=False)

    plt.figure()
    plt.imshow(closed_skull[target_slice])
    plt.show()

def get_biggest_group(cluster: np.ndarray) -> np.ndarray:
    lab, n = label(cluster)
    if n == 0: logger.critical("No clusters were found! cannot get skull space")

    print(n)

    target_slice = (slice(None), slice(None), lab.shape[2]//2)
    plt.figure()
    plt.imshow(lab[target_slice])
    plt.show(block=False)

    sizes = np.bincount(lab.ravel())
    sizes[0] = 0  # ignore background
    biggest_label = sizes.argmax()

    biggest_label = np.where(lab == biggest_label, 1, 0)

    return biggest_label
