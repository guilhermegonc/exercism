from random import randint
from string import ascii_uppercase

names_to_use = list()
for c in ascii_uppercase:
    for d in ascii_uppercase:
        for n in range(0, 1000):
            names_to_use.append(c + d + f'{n:03d}')


class Robot:
    def __init__(self):
        self.alpha = ascii_uppercase
        self.name = self.generator()

    def generator(self):
        global names_to_use
        if len(names_to_use) == 0:
            raise ValueError('No names available.')
        while True:
            ind = randint(0, len(names_to_use) - 1)
            name = names_to_use[randint(0, ind)]
            if name in names_to_use:
                break
        names_to_use.remove(name)
        return name

    def reset(self):
        global names_to_use
        to_add = self.name
        self.name = self.generator()
        names_to_use.append(to_add)
        return self.name
