
def hey(phrase):
    phrase = phrase.strip()
    escape_special_chars(phrase)
    print(phrase)
    if phrase.isspace() or phrase == '':
        return 'Fine. Be that way!'
    elif phrase.isupper() and '?' in phrase[-1]:
        return 'Calm down, I know what I\'m doing!'
    elif '?' in phrase[-1]:
        return 'Sure.'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'


def escape_special_chars(text):
    text = text.replace(r'\n', '')
    text = text.replace(r'\t', '')
    return text
