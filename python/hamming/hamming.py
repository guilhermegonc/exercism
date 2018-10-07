def distance(strand_a, strand_b):
    counter = 0

    if len(strand_a) != len(strand_b):
        raise ValueError('It is not possible to compare different string lengths.')

    for c in range(len(strand_a)):
        if strand_a[c] != strand_b[c]:
            counter += 1
    return counter
