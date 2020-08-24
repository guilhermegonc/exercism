import re


def parse(markdown):
    lines = markdown.split('\n')
    text = [parse_line(i) for i in lines]
    text = ''.join(text)
    text = text.replace('</ul><ul>', '')
    return text


def parse_line(text):
    if re.match('###### (.*)', text) is not None:
        text = f'<h6>' + text[7:] + '</h6>'

    elif re.match('## (.*)', text) is not None:
        text = f'<h2>' + text[3:] + '</h2>'

    elif re.match('# (.*)', text) is not None:
        text = '<h1>' + text[2:] + '</h1>'

    elif re.match('\* (.*)', text) is not None:
        text = '<ul><li>' + text[2:] + '</li></ul>'

    else:
        text = '<p>' + text + '</p>'

    return style_text(text)


def style_text(text):
    txt = re.match('(.*)__(.*)__(.*)', text)
    if txt:
        text = txt.group(1) + '<strong>' + txt.group(2) + '</strong>' + txt.group(3)

    txt = re.match('(.*)_(.*)_(.*)', text)
    if txt:
        text = txt.group(1) + '<em>' + txt.group(2) + '</em>' + txt.group(3)

    return text
