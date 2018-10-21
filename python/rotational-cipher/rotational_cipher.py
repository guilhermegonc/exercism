from string import ascii_letters, ascii_lowercase


def rotate(text, key):
    ascii_rotate = ['_' for _ in range(26)]

    for pos, ch in enumerate(ascii_lowercase):
        if pos - key <= 25:
            ascii_rotate[pos - key] = ch
        else:
            ascii_rotate[(pos - key) % 26] = ch

    ascii_rotate = ''.join(ascii_rotate) + ''.join(ascii_rotate).upper()
    dictionary = str.maketrans(ascii_letters, ascii_rotate)

    return str.translate(text, dictionary)
