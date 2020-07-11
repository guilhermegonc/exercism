def say(number):
    if number == 0:
        return 'zero'

    if number < 0 or number > 999999999999:
        raise ValueError('Invalid number')

    chunks = split_value(number)
    chunks = add_labels(chunks)
    chunks = [describe_value(number) + ' ' + label for number, label in chunks]
    return ' '.join(chunks).strip()


def split_value(number):
    str_num = str(number)
    str_num = str_num.zfill(12)
    return [str_num[c: c+3] for c in range(0, 12, 3)]


def add_labels(numbers):
    inverted = numbers[::-1]
    labels = ['', 'thousand', 'million', 'billion']
    labeled_numbers = [(c, labels[ind]) for ind, c in enumerate(inverted) if c != '000']
    return labeled_numbers[::-1]


def describe_value(number):
    number = int(number)
    hundreds = number // 100
    h = describe_unit(hundreds)

    tens = number % 100 // 10
    t = describe_tens(tens)

    modulus = number % 100 if number % 100 <= 19 else number % 10
    m = describe_unit(modulus)

    return name_chunk(h, t, m)


def describe_unit(number):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    return units[number]


def describe_tens(number):
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    return tens[number]


def name_chunk(hundred, ten, unit):
    str_num = ''
    str_num += hundred + ' hundred' if hundred != '' else ''
    str_num += ' ' + ten if ten != '' else ''
    str_num += '-' + unit if ten != '' and unit != '' else ' ' + unit
    return str_num.strip()
