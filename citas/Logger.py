from User import User
from UserManager import UserManager


class Logger:
    users = UserManager()

    def __init__(self):
        self.user_logged = ''

    def set_users(self, user_manager):
        self.users = user_manager

    def log_on(self, email, password):
        if not self.user_logged:
            user_log = [x for x in self.users.user_list if x.email == email]

            if user_log[0].password == password:
                self.user_logged = user_log[0]
                print("%s ha iniciado sesión" % email)
            else:
                print("La contraseña es incorrecta")
        else:
            raise ValueError("Ya hay un usuario loggeado")

    def log_off(self):
        if self.user_logged:
            self.user_logged = ''
            print("Hasta luego")


if __name__ == "__main__":
    # Create an Email object
    user = User()
    user2 = User()
    user3 = User()
    uM = UserManager()
    log = Logger()

    user.set_email('carlos7ma@gmail.com')
    user.set_password('Carlos7ma')

    user2.set_email('morales@gmail.com')
    user2.set_password('pruebacontrasenia')

    user3.set_email('aguilera@gmail.com')
    user3.set_password('pruebanormal111')

    uM.add(user)
    uM.add(user2)
    uM.add(user3)

    log.set_users(uM)

    log.log_on('carlos7ma@gmail.com', 'Carlos7ma')

    log.log_off()

    log.log_on('carlos7ma@gmail.com', 'prueba')

    log.log_on('carlos7ma@gmail.com', 'Carlos7ma')

    log.log_on('aguilera@gmail.com', 'Carlos7ma')
