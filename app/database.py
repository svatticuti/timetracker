import imp
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#We no longer need this since we are connecting to database via SQLALCHEMY, keep it just for documentation purposes
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='timetracker', user='postgres', password='Ninja0001', cursor_factory=RealDictCursor )
#         cursor = conn.cursor()
#         print("DB Conn successful")
#         break
#     except Exception as error:
#         print("DB Conn failed")
#         print(error)
#         time.sleep(2)
