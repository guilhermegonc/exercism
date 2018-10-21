class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergies_index = [
            ['eggs', 1], ['peanuts', 2], ['shellfish', 4], ['strawberries', 8],
            ['tomatoes', 16], ['chocolate', 32], ['pollen', 64], ['cats', 128]
        ]

    def ignore_unknown_scores(self):  # Ignore part of the score that reaches or overpass 2 times the higher number.
        if self.score >= (self.allergies_index[-1][1] * 2):
            return self.score % (self.allergies_index[-1][1] * 2)
        return self.score

    def populate_list(self):
        allergies = []
        top_score = self.ignore_unknown_scores()

        if top_score == 0:
            return allergies

        for data in self.allergies_index[::-1]:  # Decreases the higher viable number from score and appends its value.
            if data[1] <= top_score:
                allergies.append(data[0])
                top_score -= data[1]
        return allergies

    def is_allergic_to(self, item):
        return item in self.populate_list()

    @property
    def lst(self):
        return self.populate_list()
