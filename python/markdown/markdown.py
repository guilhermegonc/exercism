import re


def parse(markdown):
    lines = markdown.split('\n')

    text = [parse_line(i) for i in lines]
    text = ''.join(text)
    text = text.replace('</ul><ul>', '')

    return text


def parse_line(text):
    heading = re.match('^#{1,6}', text)

    if heading is not None:
        size = len(heading.group())
        text = f'<h{size}>' + text[size + 1:] + f'</h{size}>'

    elif re.match('\* (.*)', text) is not None:
        text = '<ul><li>' + text[2:] + '</li></ul>'

    else:
        text = '<p>' + text + '</p>'

    return style_text(text)


def style_text(text):
    text = str.replace(text, '__', '</strong>')
    text = str.replace(text, '</strong>', '<strong>', 1)
    text = str.replace(text, '_', '</em>')
    text = str.replace(text, '</em>', '<em>', 1)
    return text
