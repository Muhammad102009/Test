# """4. Поиск данных в базе
# Напишите метод в классе DatabaseManager, который будет принимать имя пользователя и возвращать 
# его данные из таблицы users. Используйте SQL-запросы для поиска данных."""
# import sqlite3

# class DatabaseManager:
#     def __init__(self, db_name='users.db'):
#         self.db_name = db_name

#     def _execute_query(self, query, params=(), fetchone=False, commit=False):
#         with sqlite3.connect(self.db_name) as connection:
#             cursor = connection.cursor()
#             cursor.execute(query, params)
#             if commit:
#                 connection.commit()
#             if fetchone:
#                 return cursor.fetchone()
#             return cursor.fetchall()

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

#     def get_user_by_name(self, name):
#         user = self._execute_query(
#             (name,),
#             fetchone=True
#         )
#         if user:
#             print(f"Найден пользователь: ID={user[0]}, Имя={user[1]}, Email={user[2]}, Возраст={user[3]}")
#         else:
#             print(f"Пользователь с именем '{name}' не найден.")
#         return user

# if __name__ == "__main__":
#     db_manager = DatabaseManager()

#     db_manager.create_table()

#     db_manager.add_user("Асанов Усон", "Asanov@example.com", 30)
#     db_manager.add_user("Мухаммад Абдурасулжанов", "Abdurasuljanow@example.com", 15)

#     db_manager.get_user_by_name("Иван Иванов")
#     db_manager.get_user_by_name("Алексей Петров")