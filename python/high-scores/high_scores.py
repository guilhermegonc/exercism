class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        top_three_len = 3 if len(self.scores) >= 3 else len(self.scores)
        return sorted(self.scores, reverse=True)[:top_three_len]
