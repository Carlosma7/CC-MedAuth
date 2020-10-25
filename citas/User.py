import re


class User:
    def __init__(self):
        self.email = ''
        self.password = ''

    @staticmethod
    def __check_email(email):
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if len(email) > 40:
            return False
        else:
            if re.search(email_regex, email):
                return True
            else:
                return False

    def set_email(self, email):
        if self.__check_email(email):
            self.email = email
        else:
            raise ValueError('El Email no es válido')

    @staticmethod
    def __check_password(password):
        if len(password) > 20:
            return False
        else:
            if any(not c.isalnum() for c in password):
                return False
            else:
                return True

    def set_password(self, password):
        if self.__check_password(password):
            self.password = password
        else:
            raise ValueError('La contraseña no es válida')


if __name__ == "__main__":
    # Create an Email object
    user = User()
    user.set_email('carlos7ma@gmail.com')
    user.set_password('Carlos7ma')
    print(user.email)
    print(user.password)

    user.set_email('morales@gmail.com')
    user.set_password('prueba_contrasenia')
    print(user.email)
    print(user.password)

    user.set_email('aguilera@gmail.com')
    user.set_password('pruebanormal111')
    print(user.email)
    print(user.password)

    user.set_email('carlos.com')
    user.set_password('123241413')
    print(user.email)
    print(user.password)
