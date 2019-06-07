def raindrops(number):
    criteria = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    string = ''
    for c in criteria.items():
        if number % c[0] == 0:
            string += c[1]

    if len(string) == 0:
        return str(number)
    return string
