import h5py

test_file = "data/3DIMG_24MAY2024_0800_L1B_STD_V01R00_B3.h5"

try:
    with h5py.File(test_file, "r") as f:
        print("--- Groups & Variables ---")

        for item in f.keys():
            print(item)

        if "IMG_TIR1" in f.keys():
            print("\nFound TIR1! This is our temperature data.")

except Exception as e:
    print(f"Error opening file: {e}")
