def recite(start, take=1):
    num_bottles = start
    lst = []

    for i in range(take):

        part_1 = f'{num_bottles if num_bottles > 0 else "No more"} ' \
                 f'{"bottle" if num_bottles == 1 else "bottles"} of beer on the wall, ' \
                 f'{num_bottles if num_bottles > 0 else "no more"} ' \
                 f'{"bottle" if num_bottles == 1 else "bottles"} of beer.'
        num_bottles -= 1

        if num_bottles >= 0:
            part_2 = f'Take {"it" if num_bottles == 0 else "one"} down and pass it around, ' \
                     f'{num_bottles if num_bottles != 0 else "no more"} ' \
                     f'{"bottle" if num_bottles == 1 else "bottles"} of beer on the wall.'
        else:
            part_2 = 'Go to the store and buy some more, 99 bottles of beer on the wall.'
            num_bottles = 99

        lst.append(part_1)
        lst.append(part_2)

        if i < take - 1:
        
    return lst
