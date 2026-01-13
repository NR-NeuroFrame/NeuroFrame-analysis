from neuroframe_analysis import compress_nifty
import os

folders = [
    "data/S872"
]

compressed_folder = [
    "compress/S872"
]


for idx, folder in enumerate(folders):
    out_folder = compressed_folder[idx]
    os.makedirs(out_folder, exist_ok=True)

    compress_nifty(folder, out_folder)
