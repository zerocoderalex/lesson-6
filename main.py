class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # Защищённый атрибут
        self.__name = name  # Защищённый атрибут
        self.__access_level = 'user'  # Уровень доступа для обычных сотрудников

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администраторов
        self.__users = []  # Список пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Только пользователь может быть добавлен.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
            print(f"Пользователь {user.get_name()} удаленг.")
        else:
            print("Пользователя нет в списке.")

    # Метод для получения списка пользователей
    def get_users(self):
        return [user.get_name() for user in self.__users]

    # Метод для получения уровня доступа администратора
    def get_access_level(self):
        return self.__access_level


# Пример использования
if __name__ == "__main__":
    # Создание экземпляров пользователей
    user1 = User(1, "Анна")
    user2 = User(2, "Борис")

    # Создание экземпляра администратора
    admin = Admin(3, "Виктор")

    # Добавление пользователей администратором
    admin.add_user(user1)
    admin.add_user(user2)

    # Печать списка пользователей
    print("Пользователи:", admin.get_users())

    # Удаление пользователя
    admin.remove_user(user1)

    # Печать списка пользователей после удаления
    print("Оставшиеся пользователи:", admin.get_users())