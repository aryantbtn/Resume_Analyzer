import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class Database:

    @staticmethod
    def get_connection():

        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            autocommit=True
        )

        conn.ping(reconnect=True)

        return conn