import fastapi
import torch
import xarray as xr

print(f"✅ AI Core (Torch): {torch.__version__}")
print(f"✅ Data Core (Xarray): {xr.__version__}")
print(f"✅ API Core (FastAPI): {fastapi.__version__}")
print("\n🔥 Environment is 100% Healthy!")
