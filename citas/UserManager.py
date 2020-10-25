from User import User


class UserManager:
    def __init__(self):
        self.user_list = []

    def add(self, new_user):
        self.user_list.append(new_user)

    def remove(self, del_user):
        pos = 0
        for x in self.user_list:
            if x.email == del_user.email:
                break
            pos = pos+1

        self.user_list.pop(pos)


if __name__ == "__main__":
    # Create an Email object
    user = User()
    user2 = User()
    user3 = User()
    uM = UserManager()

    user.set_email('carlos7ma@gmail.com')
    user.set_password('Carlos7ma')
    uM.add(user)
    [print("%s %s" % (i.email, i.password)) for i in uM.user_list]
    print()

    user2.set_email('morales@gmail.com')
    user2.set_password('pruebacontrasenia')
    uM.add(user2)
    [print("%s %s" % (i.email, i.password)) for i in uM.user_list]
    print()

    user3.set_email('aguilera@gmail.com')
    user3.set_password('pruebanormal111')
    uM.add(user3)
    [print("%s %s" % (i.email, i.password)) for i in uM.user_list]
    print()

    uM.remove(user2)
    [print("%s %s" % (i.email, i.password)) for i in uM.user_list]
