import os
import urllib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Connection with database
DB_SERVER = os.getenv('DB_SERVER')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_UID = os.getenv('DB_UID')
DB_PASS = os.getenv('DB_PASS')

DATABASE_URL = urllib.parse.quote_plus(f'Driver={{ODBC Driver 18 for SQL Server}};Server={DB_SERVER},{DB_PORT};Database={DB_NAME};Uid={DB_UID};Pwd={DB_PASS};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
CONNECTION_STR = 'mssql+pyodbc:///?odbc_connect={}'.format(DATABASE_URL)

engine = create_engine(CONNECTION_STR, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()