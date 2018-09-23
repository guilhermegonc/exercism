from random import sample, randint
from string import ascii_uppercase

names_to_use = dict()


class Robot:
    def __init__(self):
        self.alpha = ascii_uppercase
        self.name = self.generator()

    def generator(self):
        if len(names_to_use) == 26 * 26 * 1000:
            raise ValueError('No names available.')
        while True:
            name = f'{"".join(sample(ascii_uppercase, 2))}{randint(0, 999):03d}'
            if name not in names_to_use:
                break
        names_to_use[name] = True
        return name

    def reset(self):
        reset = self.name
        self.name = self.generator()
        del names_to_use[reset]
        return self.name
