class Allergies:
    def __init__(self, score):
        self.score = [int(i) for i in list(f'{score:b}')[::-1]]
        self.allergies_index = [
            ['eggs', 1], ['peanuts', 2], ['shellfish', 4], ['strawberries', 8],
            ['tomatoes', 16], ['chocolate', 32], ['pollen', 64], ['cats', 128]
        ]

    def populate_list(self):
        allergies = []

        for ind, al in enumerate(self.score):
            if al == 1 and ind < len(self.allergies_index):
                allergies.append(self.allergies_index[ind][0])

        return allergies

    def is_allergic_to(self, item):
        return item in self.populate_list()

    @property
    def lst(self):
        return self.populate_list()
