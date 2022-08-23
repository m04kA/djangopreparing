import os

USER = os.getenv("POSTGRES_USER", "admin")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "root")
HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
PORT_DB = int(os.getenv("PORT_DB", "5433"))