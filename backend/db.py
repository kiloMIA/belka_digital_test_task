from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


POSTGRES_HOST = getenv('POSTGRES_HOST')
POSTGRES_DB = getenv('POSTGRES_DB')
POSTGRES_USER = getenv('POSTGRES_USER')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = getenv('POSTGRES_PORT')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL, echo=True)  
SessionLocal = sessionmaker(bind=engine) 
Base: DeclarativeMeta = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_user(username: str):
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM users WHERE username=%s", (username,))
#         user_record = cur.fetchone()

#     if user_record:
#         user = UserInDB(
#             username=user_record[0],
#             hashed_password=user_record[1],
#             email=user_record[2],
#             full_name=user_record[3],
#             disabled=user_record[4]
#         )
#         return user
#     return None

