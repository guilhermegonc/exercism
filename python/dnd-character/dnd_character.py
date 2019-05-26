from random import sample


class Character:
    def __init__(self):
        ability_values = [self.ability() for _ in range(6)]
        self.strength, self.dexterity, self.constitution,\
        self.intelligence, self.wisdom, self.charisma = ability_values
        self.hitpoints = 10 + modifier(self.constitution)

    def __repr__(self):
        return f'Strength: {self.strength}\n' \
               f'Dexterity: {self.dexterity}\n' \
               f'Constitution: {self.constitution}\n' \
               f'Intelligence: {self.intelligence}\n' \
               f'Wisdom: {self.wisdom}\n' \
               f'Charisma: {self.charisma}\n\n' \
               f'Hitpoints: {self.hitpoints}'

    def ability(self):
        values = sample(range(1, 6), 4)
        return sum(values) - min(values)


def modifier(num):
    return (num - 10) // 2
