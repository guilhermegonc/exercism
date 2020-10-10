import pandas as pd


def tally(rows):
    header = [f'Team {" " : <25} | MP |  W |  D |  L |  P']
    board = pd.DataFrame()

    for r in rows:
        board = board.append(tabulate_data(r))

    board = parse_data(board) if rows != [] else rows
    return header + board


def tabulate_data(game):
    game = game.split(';')
    result = game[2]

    home = {
        'team': game[0],
        'matches': 1,
        'win': 1 if result == 'win' else 0,
        'draw': 1 if result == 'draw' else 0,
        'loss': 1 if result == 'loss' else 0
    }

    away = {
        'team': game[1],
        'matches': 1,
        'win': 1 if result == 'loss' else 0,
        'draw': 1 if result == 'draw' else 0,
        'loss': 1 if result == 'win' else 0
    }

    return pd.DataFrame([home, away])


def parse_data(df):
    df = df.groupby('team').sum()
    df = df.reset_index()
    df['points'] = df['win'] * 3 + df['draw']
    df = df.sort_values(by=['points', 'team'], ascending=[False, True])

    srs = df.apply(format_result, axis=1)
    return srs.tolist()


def format_result(srs):
    return f'{srs["team"]: <30} | {srs["matches"]: >2} | {srs["win"]: >2} | ' \
           f'{srs["draw"] : >2} | {srs["loss"]: >2} | {srs["points"]: >2}'
