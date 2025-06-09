import csv
from db import get_connection

def importar_pedidos(csv_file):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
         id SERIAL PRIMARY KEY,
         cliente TEXT,
         productos TEXT, 
         cantidad INTEGER,
         precio FLOAT       
        )
    """)

    conn.commit()

    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO pedidos (cliente, productos, cantidad, precio)
                VALUES (%s, %s, %s, %s)
        """, (row['cliente'], row['productos'], int(row['cantidad']), float(row['precio'])))
    
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    importar_pedidos("/app/pedidos.csv")