# """5. Работа с транзакциями
# Добавьте в класс DatabaseManager метод, который будет выполнять несколько операций с базой данных в одной транзакции.
# Реализуйте простую логику для добавления нескольких записей в таблицу и откат транзакции в случае ошибки.
# """
# import sqlite3

# class DatabaseManager:
#     def __init__(self, db_name='users.db'):
#         self.db_name = db_name

#     def _execute_query(self, query, params=(), fetchone=False, commit=False, connection=None):
#         if connection is None:
#             with sqlite3.connect(self.db_name) as connection:
#                 cursor = connection.cursor()
#                 cursor.execute(query, params)
#                 if commit:
#                     connection.commit()
#                 if fetchone:
#                     return cursor.fetchone()
#                 return cursor.fetchall()
#         else:
#             cursor = connection.cursor()
#             cursor.execute(query, params)
#             return cursor

#     def create_table(self):
#         self._execute_query(
#             """
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 email TEXT UNIQUE NOT NULL,
#                 age INTEGER
#             )
#             """,
#             commit=True
#         )
#         print("Таблица 'users' создана или уже существует.")

#     def add_user(self, name, email, age):
#         try:
#             self._execute_query(
#                 (name, email, age),
#                 commit=True
#             )
#             print(f"Пользователь {name} успешно добавлен.")
#         except sqlite3.IntegrityError:
#             print(f"Ошибка: Пользователь с email '{email}' уже существует.")

#     def execute_transaction(self, operations):

#         try:
#             with sqlite3.connect(self.db_name) as connection:
#                 connection.execute("BEGIN") 
#                 for query, params in operations:
#                     self._execute_query(query, params, connection=connection)
#                 connection.commit()
#                 print("Транзакция успешно выполнена.")
#         except sqlite3.Error as e:
#             connection.rollback()
#             print(f"Ошибка транзакции: {e}. Все изменения отменены.")

# if __name__ == "__main__":
#     db_manager = DatabaseManager()

#     db_manager.create_table()

#     operations = [
#         ("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Асанов Усон", "Asanov@gmail.com", 28)),
#         ("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Билол Болтабоев", "Bilol@gmail.com", 24)),
#         ("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", ("Мухаммад Абдурасулжанов", "Muhammad@gmail.com", 30)), 
#     ]

#     db_manager.execute_transaction(operations)
