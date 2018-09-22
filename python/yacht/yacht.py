# Score categories
YACHT = lambda dice: 50 if sum(dice) == 5 * dice[0] else 0
ONES = lambda dice: dice.count(1) * 1
TWOS = lambda dice: dice.count(2) * 2
THREES = lambda dice: dice.count(3) * 3
FOURS = lambda dice: dice.count(4) * 4
FIVES = lambda dice: dice.count(5) * 5
SIXES = lambda dice: dice.count(6) * 6
FULL_HOUSE = lambda dice: sum(dice) if (2 <= dice.count(dice[0]) <= 3) and (len(set(dice)) == 2) else 0
CHOICE = lambda dice: sum(dice)
FOUR_OF_A_KIND = lambda dice: 4 * sorted(dice)[2] if dice.count(sorted(dice)[2]) >= 4 else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


def score(dice, category):
    return category(dice)
