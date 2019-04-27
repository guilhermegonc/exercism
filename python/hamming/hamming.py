def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('It is not possible to compare different string lengths.')

    counter = [1 if a != b else 0 for a, b in zip(strand_a, strand_b)]
    return sum(counter)
