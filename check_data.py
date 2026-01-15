import os

import xarray as xr

stuff = "data/3DIMG_24MAY2024_0800_L1B_STD_V01R00_B3.h5"

if os.path.exists(stuff):
    data = xr.open_dataset(stuff)
    print("--- INFO ---")
    print(data)
    print("\n--- VARS ---")
    print(data.data_vars)
else:
    print("File not found in data folder")
