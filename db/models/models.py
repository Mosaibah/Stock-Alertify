from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

url = "cockroachdb://" + os.getenv('DB_USER') + "@" + os.getenv("DB_HOST") + ":" + os.getenv("DB_PORT") + "/" + os.getenv("DB_NAME") + "?sslmode=" + os.getenv("DB_SSL")

engine = create_engine(url, connect_args={"application_name": "stock_alertify"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        print("Failed to connect to database.")
        print(f"{err}")
        raise
    finally:
        db.close()
