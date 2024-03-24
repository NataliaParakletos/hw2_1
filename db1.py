import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# SQL-запит для створення таблиці users
cur.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        email VARCHAR(100) UNIQUE
    )
""")

# SQL-запит для створення таблиці status
cur.execute("""
    CREATE TABLE status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE
    )
""")

# SQL-запит для створення таблиці tasks
cur.execute("""
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    )
""")

conn.commit()

cur.close()
conn.close()
