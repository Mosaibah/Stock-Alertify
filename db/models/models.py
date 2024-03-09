from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()


url = "cockroachdb://"+ os.getenv('DB_USER') + "@" + os.getenv("DB_HOST") +": " + os.getenv("DB_PORT") + "?sslmode=" + os.getenv("DB_SSL") 

try:
    engine = create_engine(url, connect_args={"application_name":"stock_alertify"})
    
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())
        
except Exception as err:
    print("Failed to connect to database.")
    print(f"{err}")