class User:
    """Класс для представления обычного пользователя."""

    def __init__(self, user_id, name):
        self.__user_id = user_id  # Уникальный идентификатор пользователя
        self.__name = name  # Имя пользователя
        self.__access_level = 'user'  # Уровень доступа по умолчанию

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
    """Класс для представления администратора, наследуется от User."""

    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Инициализация родительского класса
        self.__access_level = 'admin'  # Уровень доступа для администратора
        self.__users = []
    # Метод для добавления пользователя в систему
    def add_user(self, user):
        """Добавляет пользователя в список пользователей."""
        self.__users.append(user)  # Добавляем пользователя в список

    # Метод для удаления пользователя из системы
    def remove_user(self, user):
        """Удаляет пользователя из списка пользователей."""
        if user in self.__users:
            self.__users.remove(user)  # Удаляем пользователя из списка
        else:
            print("Пользователь не найден в списке.")  # Сообщение, если пользователь не найден

            #print(user.get_name())  # Выводит имена оставшихся пользователей

    def get_users(self):
        return [user.get_name() for user in self.__users]


    def get_access_level(self):
        return self.__access_level

        # Создаем список пользователей
if __name__ == "__main__":
        # Создаем обычных пользователей
    user1 = User(1, "Иван")
    user2 = User(2, "Анна")

        # Создаем администратора
    admin = Admin(3, "Сергей")

        # Добавляем пользователей в список
    admin.add_user(user1)
    admin.add_user(user2)

        # Удаляем пользователя
    admin.remove_user(user2)

        # Проверяем список пользователей
    print(admin.get_users())  # Выводит имена оставшихся пользователей
        #print("Оставшиеся пользователи:", admin.get_users())