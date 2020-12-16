from operator import attrgetter


class Team:
    def __init__(self, name):
        self.name = name
        self.matches = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.points = 0

    def __repr__(self):
        return f'{self.name: <30} | {self.matches: >2} | {self.wins: >2} | '\
            f'{self.draws : >2} | {self.losses: >2} | {self.points: >2}'


def tally(rows):
    parsed = [r.split(';') for r in rows]
    results = [(home, result) for home, _, result in parsed]
    results += [(away, convert_away(result)) for _, away, result in parsed]
    teams = [team for team, _ in results]
    teams = [Team(t) for t in set(teams)]
    [update_stats(team, res, teams) for team, res in results]
    ranking = sort_ranking(teams)
    return [f'Team {" " : <25} | MP |  W |  D |  L |  P'] + [str(team) for team in ranking]


def convert_away(home_result):
    if home_result in ['win', 'loss']:
        return 'loss' if home_result == 'win' else 'win'
    return 'draw'


def update_stats(team_name, result, table):
    [update_team(team, result) for team in table if team.name == team_name]
    pass


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
    pass


def sort_ranking(table):
    table = sorted(table, key=attrgetter('name'))
    return sorted(table, key=attrgetter('points'), reverse=True)
