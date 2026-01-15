import sqlalchemy

from src.database import create_db_and_tables, engine
from src.models import SatelliteLog, WeatherAlert

try:
    print("Attempting to create tables...")
    create_db_and_tables()
    print("Tables created successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
