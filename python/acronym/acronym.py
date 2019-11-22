import re


def abbreviate(words):
    return ''.join([(w[0].upper()) for w in replace_chars(words).split()])


def replace_chars(word):
    return re.sub(r'-|_', ' ', word)
