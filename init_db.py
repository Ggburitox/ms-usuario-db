import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def create_tables():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME")
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                dni CHAR(8) UNIQUE NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("Tabla 'usuarios' creada correctamente.")
    except Exception as e:
        print(f"Error al conectar o crear la tabla: {e}")

if __name__ == "__main__":
    create_tables()
