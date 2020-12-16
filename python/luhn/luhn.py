import re


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')[::-1]

    def valid(self):
        if self.card_num.isdigit() and len(self.card_num) > 1:
            odd_pos_numbers = [int(n) for n in self.card_num[::2]]
            pair_pos_numbers = [self.double_digit(n) for n in self.card_num[1::2]]
            total = sum(odd_pos_numbers + pair_pos_numbers)
            return total % 10 == 0
        return False

    def double_digit(self, n):
        value = int(n) * 2
        return value if value <= 9 else value - 9

