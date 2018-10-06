import pandas as pd

class Allergies:

    def __init__(self, score):
        self.allergies_index = [
            ['eggs', 1], ['peanuts', 2], ['shellfish', 4], ['strawberries', 8],
            ['tomatoes', 16], ['chocolate', 32], ['pollen', 64], ['cats', 128]
        ]
        self.score = score
        self.restrict_known_scores()
        self.populate_list_of_allergies()

    def restrict_known_scores(self):
        if self.score > 255:
            return self.score % 256
        return self.score

    def populate_list_of_allergies(self):
        allergies = []
        top_score = self.restrict_known_scores()

        while True:
            if top_score == 0:
                break
            for data in self.allergies_index[::-1]:  # Loop the scores to find the max viable
                if data[1] <= top_score:
                    allergies.append(data[0])
                    top_score -= data[1]
        return allergies

    def is_allergic_to(self, item):
        return item in self.populate_list_of_allergies()

    @property
    def lst(self):
        return self.populate_list_of_allergies()
