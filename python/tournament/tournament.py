from collections import defaultdict


class Team:
    def __init__(self):
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0

    def __repr__(self):
        return f'{self.matches: >2} | {self.wins: >2} | {self.draws : >2} | {self.losses: >2} | {self.points: >2}'


def tally(rows):
    board = defaultdict(Team)
    parsed = [r.split(';') for r in rows]
    results = [(home, result) for home, _, result in parsed]
    results += [(away, convert_away(result)) for _, away, result in parsed]
    [update_team(board[team], res) for team, res in results]
    ranking = sort_ranking(board)
    return [f'Team {" " : <25} | MP |  W |  D |  L |  P'] + [f'{name: <30} | ' + f'{info}' for name, info in ranking]


def convert_away(home_result):
    if home_result in ['win', 'loss']:
        return 'loss' if home_result == 'win' else 'win'
    return 'draw'


def update_team(team, result):
    team.matches += 1
    if result == 'win':
        team.wins += 1
        team.points += 3
    elif result == 'draw':
        team.draws += 1
        team.points += 1
    else:
        team.losses += 1


def sort_ranking(table):
    table = sorted(table.items())
    return sorted(table, key=lambda team: team[1].points, reverse=True)
