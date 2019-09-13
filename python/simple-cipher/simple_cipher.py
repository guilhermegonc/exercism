from string import ascii_lowercase


class Cipher:
    def __init__(self, key='a' * len(ascii_lowercase)):
        self.key = key.lower()
        self.chars = list(ascii_lowercase)
        self.positions = [ind for ind in range(len(self.chars))]

    def encode(self, text):
        act_positions = [self.get_position(k) for k in text]
        new_positions = [self.get_position(t) for t in self.key]

        return ''.join([self.get_char(act_positions[ind] + new_positions[ind % len(self.key)])
                        for ind in range(len(text))])

    def decode(self, text):
        act_positions = [self.get_position(k) for k in text]
        old_positions = [self.get_position(t) for t in self.key]

        return ''.join([self.get_char(act_positions[ind] - old_positions[ind % len(self.key)])
                        for ind in range(len(text))])

    def get_char(self, position):
        return dict(zip(self.positions, self.chars))[position % len(self.chars)]

    def get_position(self, char):
        return dict(zip(self.chars, self.positions))[char]
