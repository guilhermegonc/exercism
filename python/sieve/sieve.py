def sieve(limit):
    natural_numbers = list(range(2, limit+1))
    prime_list = natural_numbers.copy()

    for prime in natural_numbers:
        end_position = (max(prime_list) // prime) + 1  # Avoid extra operations
        not_primes = [prime * i for i in prime_list[:end_position]]

        for value in not_primes:
            if value in prime_list:
                prime_list.remove(value)

    return prime_list
