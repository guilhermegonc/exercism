def prime_factors(natural_number):
    divisor = 2
    prime_list = list()
    while True:
        if natural_number % divisor == 0:
            natural_number /= divisor
            prime_list.append(divisor)
        elif natural_number / divisor > 1:
            divisor += 1
        else:
            break
    return prime_list
