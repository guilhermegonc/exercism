def prime_factors(natural_number):
    prime_list = []
    divisor = 2

    while natural_number > 1:

        if natural_number % divisor == 0:
            natural_number /= divisor
            prime_list.append(divisor)

        else:
            divisor += 1

    return prime_list
