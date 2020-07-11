def say(number):
    chunks = split_value(number)
    # if number == 0:
    #     return 'zero'
    #
    # if 0 < number <= 19:
    #     return return_units(number)
    #
    # elif 19 < number <= 999:
    #     hundreds = number // 100
    #     tens = number % 100 // 10
    #     units = number % 10
    #
    #     h = say(hundreds) if hundreds != 0 else ''
    #     t = return_tens(tens)
    #     u = say(units) if units != 0 else ''
    #     return name_chunk(h, t, u)
    #
    # elif 999 < number <= 999999999999:
    #     chunks = break_chunks(number)
    #     return name_thousands(chunks)
    #
    # else:
    #     raise ValueError('Invalid Number')

def split_values():
    return

def return_units(number):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    return units[number]


def return_tens(number):
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    return tens[number]


def split_value(number):
    str_num = str(number)
    len_num = len(str_num)
    mod = len_num % 3

    if mod != 0:
        fill = len_num - mod + 3
        str_num = str_num.zfill(fill)

    return [int(str_num[c: c+3]) for c in range(0, len_num, 3)]


def name_thousands(chunks):
    chunk_names = ['', 'thousand', 'million', 'billion']
    str_num = ''
    for ind, c in enumerate(chunks):
        name_pos = len(chunks) - 1 - ind
        str_num += say(c) + ' ' + chunk_names[name_pos] + ' ' if c != 0 else ''
    return str_num.strip()


def name_chunk(hundred, ten, unit):
    str_num = ''
    str_num += hundred + ' hundred' if hundred != '' else ''
    str_num += ' ' + ten if ten != '' else ''
    str_num += '-' + unit if ten != '' and unit != '' else ' ' + unit
    return str_num.strip()
