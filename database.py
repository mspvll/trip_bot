import sqlite3

#файл users.db будет создан, если его не существует

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS places(
    city TEXT,
    cost INTEGER
)
''')
conn.commit()

def add_places():
    cursor.execute('''
         INSERT INTO places(city,cost)
    VALUES
        ("Москва",30000),
        ("Санкт-Петербург",24000),
        ("Мурманск", 45000),
        ('Нью-Йорк', 250000),
        ('Лас-Вегас', 260000),
        ('Лос-Анджелес',270000),
        ('Рим',100000),
        ('Венеция',115000),
        ('Барселона',130000),
        ('Мадрид',120000),
        ('Пекин',115000),
        ('Шанхай',105000),
        ('Рио-де-Жанейро', 170000)
    ''')
    conn.commit()



def select_cost(budget):
    t = cursor.execute('''
        SELECT * FROM places WHERE cost <= ?
    
    ''', (budget,))
    return t.fetchall()
