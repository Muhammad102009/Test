# """1. Создание класса для работы с базой данных
# Напишите класс DatabaseManager, который будет использовать 
# SQLite3 для подключения к базе данных. Реализуйте методы для открытия и закрытия соединения."""
# import sqlite3

# class DatabaseManager:
#     def __init__(self, db_name='users.db'):
#         self.db_name = db_name
#         self.connection = None
#         self.cursor = None

#     def open_connection(self):
#         self.connection = sqlite3.connect(self.db_name)
#         self.cursor = self.connection.cursor()
#         print(f"Соединение с базой данных '{self.db_name}' открыто.")

#     def close_connection(self):
#         if self.connection:
#             self.connection.close()
#             print(f"Соединение с базой данных '{self.db_name}' закрыто.")

#     def create_table(self):
#         self.open_connection()
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name VARCHAR(40) NOT NULL,
#                 email TEXT UNIQUE NOT NULL,
#                 age INTEGER
#             )
#         """)
#         self.connection.commit()
#         print("Таблица 'users' создана или уже существует.")
#         self.close_connection()

#     def add_user(self, name, email, age):
#         try:
#             self.open_connection()
#             self.cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
#             self.connection.commit()
#             print(f"Пользователь {name} добавлен в базу данных.")
#         except sqlite3.IntegrityError:
#             print(f"Ошибка: Пользователь с email '{email}' уже существует.")
#         finally:
#             self.close_connection()

#     def get_user(self, email):
#         self.open_connection()
#         self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
#         user = self.cursor.fetchone()
#         self.close_connection()
#         return user

#     def delete_user(self, email):
#         self.open_connection()
#         self.cursor.execute("DELETE FROM users WHERE email = ?", (email,))
#         self.connection.commit()
#         print(f"Пользователь с email '{email}' удален.")
#         self.close_connection()


# if __name__ == "__main__":
#     db_manager = DatabaseManager()
#     db_manager.create_table()
    
#     db_manager.add_user("Асанов Усон", "Asanov@example.com", 30)
#     db_manager.add_user("Мухаммад Абдурасулжанов", "Abdurasuljanow@example.com", 15)
    
#     user = db_manager.get_user("ivan@example.com")
#     if user:
#         print(f"Найден пользователь: {user}")
#     else:
#         print("Пользователь не найден.")
    
#     db_manager.delete_user("maria@example.com")
