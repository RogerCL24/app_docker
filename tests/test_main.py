from app.db import get_connection

def test_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()
