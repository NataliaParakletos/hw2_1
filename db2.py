from faker import Faker 
import psycopg2 
 
fake = Faker() 
 
conn = psycopg2.connect( 
    dbname="postgres", 
    user="postgres", 
    password="123", 
    host="localhost", 
    port="5432" 
) 
 
cur = conn.cursor() 
conn.commit()

def generate_fake_data() -> tuple:
    fake_users = [(fake.name(), fake.email()) for _ in range(30)]  # Генеруємо список з 30 користувачів з їхніми email
    fake_statuses = ['new', 'in progress', 'completed']  # Список статусів
    fake_tasks = [(fake.sentence(), fake.text(), fake.random_element(elements=fake_statuses)) for _ in range(30)]  # Генеруємо список з 30 завдань

    return fake_users, fake_statuses, fake_tasks

fake_users, fake_statuses, fake_tasks = generate_fake_data()

for user in fake_users:
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (user[0], user[1]))

for status in fake_statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))

for task in fake_tasks:
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, (SELECT id FROM status WHERE name = %s), (SELECT id FROM users ORDER BY RANDOM() LIMIT 1))", 
                (task[0], task[1], task[2]))

conn.commit() 
 
cur.close() 
conn.close()
