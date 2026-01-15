import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine, select

load_dotenv()
try:
    engine = create_engine(os.getenv("DATABASE_URL"))
    with Session(engine) as session:
        session.execute(select(1))
    print("✅ Database Connection: SUCCESSFUL on Port 5757!")
except Exception as e:
    print(f"❌ Database Error: {e}")
