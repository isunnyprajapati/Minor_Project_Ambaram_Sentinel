import os
from datetime import datetime

import xarray as xr

from .database import Session, engine
from .models import SatelliteLog, WeatherAlert

TEMP_THRESHOLD_CELSIUS = -40


def process_satellite_file(file_path):
    file_name = os.path.basename(file_path)

    try:
        ds = xr.open_dataset(file_path)

        data = ds["bt_ir1"]

        extreme_points = data.where(data < (TEMP_THRESHOLD_CELSIUS + 273.15), drop=True)

        if extreme_points.size > 0:
            with Session(engine) as session:
                new_alert = WeatherAlert(
                    latitude=float(extreme_points.lat.mean()),
                    longitude=float(extreme_points.lon.mean()),
                    region_name="Detected Region",
                    event_type="Potential Storm",
                    severity="High",
                    value=float(extreme_points.min()),
                )
                session.add(new_alert)

                log = SatelliteLog(file_name=file_name, status="Success")
                session.add(log)
                session.commit()
            print(f"✅ Alert saved for {file_name}")

    except Exception as e:
        print(f"❌ Failed to process {file_name}: {e}")
