def raindrops(number):
    string = ''
    if number % 3 == 0:
        string += 'Pling'

    if number % 5 == 0:
        string += 'Plang'

    if number % 7 == 0:
        string += 'Plong'

    if len(string) == 0:
        return str(number)

    return string
