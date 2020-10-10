from datetime import timedelta, datetime
from random import randint

users = ['Danielle', 'Mayara', 'Juliana', 'Débora', 'Guilherme']
created = datetime(2020, 1, 1, 0, 0, 0)

begin = 'INSERT into serie_watched VALUES \n'
with open('/Users/guilherme/Downloads/to_update.csv', 'w+') as file:
    file.write(begin)

for i in range(2000):
    user_id = randint(0, 4)
    series_id = randint(1, 5611)

    h = randint(0, 23)
    m = randint(0, 59)
    s = randint(0, 59)
    created += timedelta(hours=h, minutes=m, seconds=s)

    input_string = '(' + str(user_id) + ',' + str(series_id) + ',\'' + str(created) + '\',\'' + str(created) + '\')' + ',\n'

    with open('/Users/guilherme/Downloads/to_update.csv', 'a') as file:
        file.write(input_string)

with open('/Users/guilherme/Downloads/to_update.csv', 'a') as file:
    file.write(input_string)
