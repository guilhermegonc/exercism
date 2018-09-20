from string import ascii_lowercase

def is_pangram(sentence):
    alphabet = list()
    for c in sentence:
        if c.isalpha():
            alphabet.append(c.lower())
    return ''.join(sorted(set(alphabet))) == ascii_lowercase

