class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        top_three = []
        values_to_check = self.scores.copy()

        loop_size = 3 if len(values_to_check) >= 3 else len(values_to_check)
        for i in range(loop_size):
            top_value = max(values_to_check)
            top_three.append(top_value)
            values_to_check.remove(top_value)
        return top_three
