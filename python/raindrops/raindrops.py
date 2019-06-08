def raindrops(number):
    criteria = zip((3, 5, 7), ('Pling', 'Plang', 'Plong'))
    text = [c[1] for c in criteria if number % c[0] == 0]

    if len(text) == 0:
        return str(number)
    return ''.join(text)
