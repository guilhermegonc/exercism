class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergies_index = [
            ['eggs', 1], ['peanuts', 2], ['shellfish', 4], ['strawberries', 8],
            ['tomatoes', 16], ['chocolate', 32], ['pollen', 64], ['cats', 128]
        ]

    def populate_list(self):
        allergies = [alg[0] for alg in self.allergies_index if self.score & alg[1] != 0]
        return allergies

    def is_allergic_to(self, item):
        return item in self.populate_list()

    @property
    def lst(self):
        return self.populate_list()
