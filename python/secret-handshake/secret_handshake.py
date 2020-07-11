def commands(number):
    return populate_list(number)[::-1] if needs_sort(number) else populate_list(number)


def populate_list(value):
    handshakes = [('wink', 1), ('double blink', 2), ('close your eyes', 4), ('jump', 8)]
    return [hs for hs, score in handshakes if score & value != 0]


def needs_sort(number):
    return number & 16 == 16
