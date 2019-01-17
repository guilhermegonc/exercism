from re import sub, finditer
from collections import Counter


def word_count(phrase):
    words = create_list_of_words(phrase)
    return Counter(words)


def create_list_of_words(text):
    words = []
    text = sub(r'_', ' ', text)

    for match in finditer(r'((\w|\w\')+(\w)|(\d))', text):
        word = match.group().lower()
        words.append(word)

    return words
