def recite(start, take=1):
    num_bottles = start
    lst = []

    for i in range(take):

        if num_bottles > 1:
            part_1 = f'{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.'
        elif num_bottles == 1:
            part_1 = f'{num_bottles} bottle of beer on the wall, {num_bottles} bottle of beer.'
        else:
            part_1 = f'No more bottles of beer on the wall, no more bottles of beer.'
        lst.append(part_1)
        num_bottles -= 1

        if num_bottles > 1:
            part_2 = f'Take one down and pass it around, {num_bottles} bottles of beer on the wall.'
        elif num_bottles == 1:
            part_2 = f'Take one down and pass it around, {num_bottles} bottle of beer on the wall.'
        elif num_bottles == 0:
            part_2 = 'Take it down and pass it around, no more bottles of beer on the wall.'
        else:
            part_2 = 'Go to the store and buy some more, 99 bottles of beer on the wall.'
            num_bottles = 99
        lst.append(part_2)

        if i < take - 1:
        
    return lst
