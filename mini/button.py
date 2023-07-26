import sqlite3

conn = sqlite3.connect("users.db") # Создаем объект, представляющий базу данных

c = conn.cursor() # создаем объект для выполнения команд

c.execute("CREATE TABLE user (name, age integer)") # СОздаем таблицу

c.execute("INSERT INTO user VALUES ('User1', 42)") # Добавляем 1-ю запись в таблицу
c.execute("INSERT INTO user VALUES ('User2', 37)") # Добавляем 2-ю запись в таблицу

conn.commit() # Сохраняем изменения

# Выводим содержимое таблицы на экран
c.execute("SELECT * FROM user") 
print(c.fetchall())

conn.close # Закрываем работу с базой