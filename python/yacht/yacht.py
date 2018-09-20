# Score categories
YACHT = 'YA'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FH'
CHOICE = 'CH'
FOUR_OF_A_KIND = 'FOAK'
LITTLE_STRAIGHT = 'LS'
BIG_STRAIGHT = 'BS'


def score(dice, category):
    if category is YACHT:
        return yacht(dice, category)
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return sum_per_category(dice, category)
    elif category in (FULL_HOUSE, CHOICE):
        return sum_all_dices(dice, category)
    elif category is FOUR_OF_A_KIND:
        return four_of_a_kind(dice)
    elif category in (LITTLE_STRAIGHT, BIG_STRAIGHT):
        return straight(dice, category)


def yacht(dice, category):
    value = dice[0]
    for c in dice:
        if c != value:
            return 0
    return 50


def sum_per_category(dice, category):
    sum = 0
    for c in dice:
        if c == category:
            sum += category
    return sum


def sum_all_dices(dice, category):
    sum = 0
    for c in dice:
        sum += c
        if (dice.count(c) == 1 or dice.count(c) >= 4) and category == FULL_HOUSE:
            return 0
    return sum


def four_of_a_kind(dice):
    for c in range(1, 7):
        if dice.count(c) >= 4:
            return 4 * c
    return 0

def straight(dice, category):
    test = str()
    dice = sorted(dice, reverse=False)
    for c in dice:
        test += str(c)
    if (test == '12345' and category == LITTLE_STRAIGHT) or (test == '23456' and category == BIG_STRAIGHT):
        return 30
    return 0
