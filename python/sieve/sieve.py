def sieve(limit):
    int_range = [n for n in range(2, int(limit ** 0.5) + 1)]
    boolean_list = [True for _ in range(2, limit + 1)]

    for index, n in enumerate(int_range):

        if boolean_list[index] is True:
            i = 0

            while (n ** 2) + (n * i) <= limit:
                value = (n ** 2) + (n * i)
                i += 1
                boolean_list[value - 2] = False

    return [prime + 2 for prime, boolean in enumerate(boolean_list) if boolean is True]
