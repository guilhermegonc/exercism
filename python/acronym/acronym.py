import re


def abbreviate(words):
    return ''.join([(w[0].upper()) for w in list_words(words)])


def list_words(phrase):
    return re.findall(r'[A-Z|a-z|\']+', phrase)
