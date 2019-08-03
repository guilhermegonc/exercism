def score(word):
    char_scores = [convert_values(c) for c in word]
    return sum(char_scores)


def convert_values(char):
    char = char.upper()
    if char in 'AEIOULNRST':
        return 1
    if char in 'DG':
        return 2
    if char in 'BCMP':
        return 3
    if char in 'FHVWY':
        return 4
    if char in 'K':
        return 5
    if char in 'JX':
        return 8
    if char in 'QZ':
        return 10
    pass
