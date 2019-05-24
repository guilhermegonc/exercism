def is_paired(input_string):
    bracs_dict = {'{': '}', '[': ']', '(': ')'}
    bracs = []

    for ind, char in enumerate(input_string):

        if char in '{[(':
            bracs.append(bracs_dict[char])

        elif char in ')]}' and len(bracs) > 0:
            if char == bracs[-1]:
                bracs.pop()
            else:
                return False

        elif char in ')]}':
            return False

    return len(bracs) == 0
