from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

url = "cockroachdb://" + os.getenv('DB_USER') + "@" + os.getenv("DB_HOST") + ":" + os.getenv("DB_PORT") + "/" + os.getenv("DB_NAME") + "?sslmode=" + os.getenv("DB_SSL")

engine = create_engine(url, connect_args={"application_name": "stock_alertify"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
