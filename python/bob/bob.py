def hey(phrase):
    phrase = phrase.strip()

    if not phrase:
        return 'Fine. Be that way!'

    if phrase.isupper():
        if is_question(phrase):
            return 'Calm down, I know what I\'m doing!'
        return 'Whoa, chill out!'

    if is_question(phrase):
        return 'Sure.'
    return 'Whatever.'


def is_question(text):
    return text.endswith('?')
