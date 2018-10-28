def primitive_triplets(b_num):
    if invalid_b_input(b_num):
        raise ValueError('B input is invalid.')

    triplets = set()
    for m in range(1, (b_num // 2) + 1):
        n = b_num // (m * 2)

        if b_num % (m * 2) == 0 and m > n and are_coprime(m, n):
            sizes = sorted(define_abc_from_nm(m, n))
            triplets.add((sizes[0], sizes[1], sizes[2]))

    return triplets


def invalid_b_input(b):
    return b % 4 != 0


def are_coprime(m, n):
    for mmc in range(2, n + 1):
        if m % mmc == 0 and n % mmc == 0:
            return False
    return True


def define_abc_from_nm(m, n):
    return [m ** 2 + n ** 2,  m * n * 2, m ** 2 - n ** 2]


def triplets_in_range(start, end):
    triplets = set()

    for a in range(start, end + 1):
        for b in range(a, end + 1):
            for c in range(b, end + 1):

                if is_triplet([a, b, c]):
                    triplets.add((a, b, c))

    return triplets


def is_triplet(triplet):
    to_test = sorted(triplet)
    return to_test[0] ** 2 + to_test[1] ** 2 == to_test[2] ** 2
