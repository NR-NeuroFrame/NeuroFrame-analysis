# ================================================================
# 0. Section: Imports
# ================================================================
import os

from typing import cast
from nibabel.loadsave import load as niload, save as nisave
from nibabel.nifti1 import Nifti1Image
import numpy as np

from .image_utils import normalize



# ================================================================
# 1. Section: Convert Files
# ================================================================
def compress_nifty(input_path: str, output_path: str, data_compression: bool = False) -> None:
    # Compress a full folder
    if os.path.isdir(input_path): _compress_nifty_folder(input_path, output_path, data_compression)
    else: _compress_nifty_file(input_path, output_path, data_compression)

def _compress_nifty_folder(input_path: str, output_path: str, data_compression: bool = False) -> None:
    nifty_files_path = [file for file in os.listdir(input_path) if file.endswith('.nii') or file.endswith('.nii.gz')]
    os.makedirs(output_path, exist_ok=True)

    for nifty_file in nifty_files_path:
        _compress_nifty_file(os.path.join(input_path, nifty_file), os.path.join(output_path, nifty_file), data_compression=data_compression)

def _compress_nifty_file(input_path: str, output_path: str, data_compression: bool = False) -> None:
    img = cast(Nifti1Image, niload(input_path))

    # Compress the values inside after normalizing to int8
    if data_compression: img = compress_data(img)

    # Save the NIfTI file with gzip compression
    nisave(img, output_path)


def compress_data(nifty: Nifti1Image) -> Nifti1Image:
    img_arr = normalize(nifty.get_fdata()).astype(np.uint8)
    nifty = Nifti1Image(img_arr, nifty.affine)

    return nifty
