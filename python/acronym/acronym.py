import re


def abbreviate(words):
    return ''.join([first_char(w) for w in list_words(words)])


def list_words(phrase):
    return re.findall(r'[A-Z|a-z|\d|\']+', phrase)


def first_char(word):
    return word[0].upper()
