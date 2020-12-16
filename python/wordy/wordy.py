def answer(question):
    numbers, operations = parse_input(question)
    result = numbers[0]
    for ind, op in enumerate(operations):
        result = calculate(result, numbers[ind+1], op)
    return result


def parse_input(text):
    parsed = text.replace('What is ', '')
    parsed = parsed.replace('?', '')
    parsed = parsed.replace(' by', '')
    parsed = parsed.split()
    numbers = [int(n) for n in parsed[::2]]
    operations = parsed[1::2]
    return validate_input(numbers, operations)


def validate_input(numbers, operations):
    if len(numbers) <= len(operations):
        raise ValueError('Invalid Input')
    return numbers, operations


def calculate(result, n, method):
    if method == 'plus':
        return result + n
    elif method == 'minus':
        return result - n
    elif method == 'divided':
        return result / n
    elif method == 'multiplied':
        return result * n
    else:
        raise ValueError('Invalid Input')
