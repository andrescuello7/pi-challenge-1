import os
import urllib

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decouple import config

# Connection with database
DB_SERVER = os.getenv('DB_SERVER') or 'server-acuello.database.windows.net'
DB_PORT = os.getenv('DB_PORT') or 1433
DB_NAME = os.getenv('DB_NAME') or 'db-acuello'
DB_UID = os.getenv('DB_UID') or 'db-acuello'
DB_PASS = os.getenv('DB_PASS') or 'T3rnari0_js'

DATABASE_URL = urllib.parse.quote_plus(f'Driver={{ODBC Driver 18 for SQL Server}};Server={DB_SERVER},{DB_PORT};Database={DB_NAME};Uid={DB_UID};Pwd={DB_PASS};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
CONNECTION_STR = 'mssql+pyodbc:///?odbc_connect={}'.format(DATABASE_URL)

engine = create_engine(CONNECTION_STR, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create variables db for calling to database
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()