from string import ascii_letters


def is_isogram(string):
    word = [c.lower() for c in string if c in ascii_letters]
    return len(word) == len(set(word))
