def hey(phrase):
    phrase = escape_special_chars(phrase).strip()

    if len(phrase) == 0:
        return 'Fine. Be that way!'

    if phrase.isupper():
        if is_question(phrase):
            return 'Calm down, I know what I\'m doing!'
        return 'Whoa, chill out!'
    else:
        if is_question(phrase):
            return 'Sure.'
        return 'Whatever.'


def escape_special_chars(text):
    text = text.replace(r'\n', '')
    text = text.replace(r'\t', '')
    return text


def is_question(text):
    return text[-1] == '?'
