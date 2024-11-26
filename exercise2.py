# """2. Класс для управления таблицей
# Создайте класс User, который будет управлять таблицей users в SQLite3. 
# Реализуйте методы для добавления нового пользователя, получения пользователя по ID и удаления пользователя."""
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

#     def add_user(self, name, email, age):
#         try:
#             self._execute_query(
#                 "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
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
#             "DELETE FROM users WHERE id = ?",
#             (user_id,),
#             commit=True
#         )
#         print(f"Пользователь с ID {user_id} успешно удален.")

# if __name__ == "__main__":
#     user_manager = User()

#     user_manager.add_user("Асанов Усон", "Asanov@example.com", 30)
#     user_manager.add_user("Мухаммад Абдурасулжанов", "Abdurasuljanow@example.com", 15)

#     user_manager.get_user_by_id(1)

#     user_manager.delete_user_by_id(2)
