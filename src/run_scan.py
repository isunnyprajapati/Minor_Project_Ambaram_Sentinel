import os

from src.xadl import process_satellite_file

sample_file = "data/sample_insat_3d.nc"

if os.path.exists(sample_file):
    print(f"Scanning {sample_file} for extreme weather...")
    process_satellite_file(sample_file)
else:
    print("❌ No sample file found. Run 'create_sample_data.py' first.")
