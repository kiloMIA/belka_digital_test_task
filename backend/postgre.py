import psycopg2
from os import getenv
from models.entity_models import UserInDB


conn = psycopg2.connect(
    host = getenv("POSTGRES_HOST"),
    dbname = getenv("POSTGRES_DB"),
    user = getenv("POSTGRES_USER"),
    password = getenv("POSTGRES_PASSWORD"),
    port = getenv("POSTGRES_PORT")
)

def get_user(username: str):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_record = cur.fetchone()

    if user_record:
        user = UserInDB(
            username=user_record[0],
            hashed_password=user_record[1],
            email=user_record[2],
            full_name=user_record[3],
            disabled=user_record[4]
        )
        return user
    return None