def primitive_triplets(number_in_triplet):
    validate_b_input(number_in_triplet)
    triplets = set()
    for n in range(1, number_in_triplet):
        for m in range(n, number_in_triplet):
            if m * n * 2 == number_in_triplet and mn_coprime(m, n):
                a, b, c = define_abc_from_nm(m, n)
                if a % 2 != 0 and c % 2 != 0:
                    sizes = sorted([a, b, c])
                    triplet = (sizes[0], sizes[1], sizes[2])
                    triplets.add(triplet)
    return triplets


def triplets_in_range(range_start, range_end):
    triplets = set()
    for a in range(range_start, range_end + 1):
        for b in range(a, range_end + 1):
            for c in range(b, range_end + 1):
                if is_triplet((a, b, c)):
                    triplets.add((a, b, c))
    return triplets


def is_triplet(triplet):
    to_test = sorted(triplet)
    return to_test[0] ** 2 + to_test[1] ** 2 == to_test[2] ** 2


def validate_b_input(b):
    if b % 4 == 0:
        return
    raise ValueError('B input is invalid.')


def mn_coprime(m, n):
    for mmc in range(2, min(m, n) + 1):
        if m % mmc == 0 and n % mmc == 0 and m > n > 0:
            return False
    return True


def define_abc_from_nm(m, n):
    a = m ** 2 + n ** 2
    b = m * n * 2
    c = m ** 2 - n ** 2
    return a, b, c
