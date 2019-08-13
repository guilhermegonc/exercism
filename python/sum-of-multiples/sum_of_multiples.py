def sum_of_multiples(limit, multiples):
    values = values_to_sum(limit, multiples)
    return sum_list(values)


def values_to_sum(limit, multiples):
    natural_numbers = range_natural_numbers(limit)
    natural_multiples = list_natural(multiples)
    return loop_multiples(natural_numbers, natural_multiples)


def range_natural_numbers(limit):
    return range(1, limit)


def list_natural(multiples):
    return [m for m in multiples if m > 0 and isinstance(m, int)]


def loop_multiples(values_rng, natural_multiples):
    return [find_multiples(values_rng, n_m) for n_m in natural_multiples]


def find_multiples(values_rng, multiple):
    return [v for v in values_rng if v % multiple == 0]


def sum_list(all_multiples):
    return sum(filter_distinct(all_multiples))


def filter_distinct(values):
    return set(flatten_list(values))


def flatten_list(list_of_lists):
    return [v for values in list_of_lists for v in values]
