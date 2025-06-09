import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME","pedidos"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", "postgres"),
        host=os.environ.get("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 5432))
    )
