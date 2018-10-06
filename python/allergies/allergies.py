class Allergies(object):

    def __init__(self, score):
        allergies_dict = {
            'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
            'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128
        }

        self.score = score
        self.valid_allergies_score = score

        if self.score > 255:
            self.valid_allergies_score = self.score % 256

        self.allergies = []

        top_score = allergy_score = self.valid_allergies_score
        while True:
            if top_score == 0:
                break

            for name, score_value in allergies_dict.items():
                if score_value <= top_score:
                    allergy_score = score_value
                    valid_allergy = name

            self.allergies.append(valid_allergy)
            top_score -= allergy_score

    def is_allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
