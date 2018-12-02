def recite(start_verse, end_verse):
    lyrics = []
    days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
            'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    gifts = ['a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens', 'four Calling Birds',
             'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking',
             'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

    for day in range(start_verse, end_verse + 1):
        gift = ', '.join(gifts[day - 1:0:-1])
        verse = f'On the {days[day - 1]} day of Christmas my true love gave to me: ' \
                f'{gift + ", and " + gifts[0] if day > 1 else gifts[0]}.'
        lyrics.append(verse)

    return lyrics
