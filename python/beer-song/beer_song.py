def recite(start, take=1):
    bottles = start
    lst = []

    for i in range(take):

        if bottles > 1:
            part_1 = f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.'
        elif bottles == 1:
            part_1 = f'{bottles} bottle of beer on the wall, {bottles} bottle of beer.'
        else:
            part_1 = f'No more bottles of beer on the wall, no more bottles of beer.'
        lst.append(part_1)
        bottles -= 1

        if bottles > 1:
            part_2 = f'Take one down and pass it around, {bottles} bottles of beer on the wall.'
        elif bottles == 1:
            part_2 = f'Take one down and pass it around, {bottles} bottle of beer on the wall.'
        elif bottles == 0:
            part_2 = 'Take it down and pass it around, no more bottles of beer on the wall.'
        else:
            part_2 = 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        lst.append(part_2)

        if i != take - 1:
            lst.append('')

    return lst
