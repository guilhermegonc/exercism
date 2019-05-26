class Phone(object):
    def __init__(self, phone_number):
        extract_numbers = [n for n in phone_number if n.isnumeric()]
        pure_number = ''.join(extract_numbers)

        # Determine full phone number
        if len(pure_number) == 10:
            self.number = pure_number
        elif len(pure_number) == 11 and pure_number[0] == '1':
            self.number = pure_number[1:]
        else:
            raise ValueError('Invalid number, check your input.')

        #  Split Code area
        if self.number[0] not in '01':
            self.area_code = self.number[:3]
        else:
            raise ValueError('Invalid code area.')

        # Split Exchange number
        if self.number[3] not in '01':
            self.exchange = self.number[3:6]
        else:
            raise ValueError('Invalid exchange number.')

    def __repr__(self):
        return self.number

    def pretty(self):
        return f'({self.area_code}) {self.exchange}-{self.number[6:]}'
