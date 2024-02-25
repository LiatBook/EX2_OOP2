from User import User


class SocialNetwork:
    __instance = None
    __is_initialized = False

    def __new__(cls,name):
        # If an instance does not exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # Additional initialization can be done here
        return cls.__instance

    def __init__(self, name):
        if self.__is_initialized:
            raise Exception("This class is a singleton!")
        self.name = name
        self._users = {}  # map between name to the user object
        print("The social network " + name + " was created!")

    def sign_up(self, name, password):
        if len(password) < 4 or len(password) > 8:
            raise Exception("This password not good")
        if name in self._users:
            raise Exception("This name user not good")
        new_user = User(name, password)
        self._users[name] = new_user
        return self._users[name]

    def log_in(self, name, password):
        if name not in self._users:
            raise Exception("The user not logged in")
        if name in self._users:
            user = self._users.get(name)
            if password == user.password:
                user._online = True
                print(name + " connected")
            else:
                raise Exception("The password is wrong")

    def log_out(self, name):
        if name not in self._users:
            raise Exception("The user don't sign up")
        if name in self._users:
            user = self._users.get(name)
            if user.online==False:
                raise Exception("Can't log out")
            user.online = False
        print(f"{name} disconnected")
        return True

    def __str__(self):
        p=self.name+" social network:"
        for k,v in self._users.items():
            p += "\n" +v.__str__()
        return p
