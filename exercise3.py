# """3. Наследование и работа с несколькими таблицами
# Реализуйте классы Admin и Customer, которые будут наследовать от класса User. 
# Добавьте дополнительные поля для каждой роли и методы для работы с соответствующими таблицами admins и customers."""
# import sqlite3

# class User:
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

#     def get_user_by_id(self, user_id):
#         user = self._execute_query(
#             (user_id,),
#             fetchone=True
#         )
#         if user:
#             print(f"Найден пользователь: ID={user[0]}, Имя={user[1]}, Email={user[2]}, Возраст={user[3]}")
#         else:
#             print(f"Пользователь с ID {user_id} не найден.")
#         return user

#     def delete_user_by_id(self, user_id):
#         self._execute_query(
#             (user_id,),
#             commit=True
#         )
#         print(f"Пользователь с ID {user_id} успешно удален.")

# if __name__ == "__main__":
#     user_manager = User()

#     user_manager.create_table()

#     user_manager.add_user("Асанов Усон", "Asanov@example.com", 30)
#     user_manager.add_user("Мухаммад Абдурасулжанов", "Abdurasuljanow@example.com", 25)

#     user_manager.get_user_by_id(1)

#     user_manager.delete_user_by_id(2)
