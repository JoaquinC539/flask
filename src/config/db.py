import psycopg2
# from app import app
import os
def get_db_connection():
    connect_string=f"postgresql://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_HOST")}/{os.getenv("DATABASE_NAME")}"
    # conn = psycopg2.connect(app.config['DATABASE_URL'])
    conn = psycopg2.connect(connect_string)
    return conn