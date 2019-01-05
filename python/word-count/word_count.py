from re import sub


def word_count(phrase):
    word_occurrence = {}
    words = create_list_of_words(phrase)

    for w in words:
        if w in word_occurrence:
            word_occurrence[w] += 1
        else:
            word_occurrence[w] = 1
    return word_occurrence


def create_list_of_words(text):
    text = sub('_', ' ', text)  # Translate underscore as whitespace
    text = sub(r'(\'t)+(\s|$)', '_t', text)  # Hold neg quotation
    text = sub(r'(\'s)+(\s|$)', '_s', text)  # Hold prop quotation

    text = sub(r'\W', ' ', text).lower()  # Replace not alpha and digits to whitespace

    # Restore property and negative quotations
    text = sub('_t', '\'t ', text)  # Translate neg to its initial format
    text = sub('_s', '\'s ', text)  # Translate prop to its initial format

    return text.split()
