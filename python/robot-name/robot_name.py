import random
import string

class Robot:

    all_names = []

    def __init__(self):
        self.name = self.gen_name()
        while self.name in self.all_names:
            self.name = self.gen_name()
        self.all_names.append(self.name)

    @staticmethod
    def gen_name():
        name = ''.join(random.choice(string.ascii_uppercase) for x in range(2))
        name += "".join(str(random.randint(0, 9)) for x in range(3))
        return name

    def reset(self):
        self.__init__()
