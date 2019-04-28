import datetime
import calendar


def meetup_day(year, month, day_of_the_week, which):
    cal = calendar.Calendar(0)  # Start calendar with monday as first day of the week

    weekday_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                    'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    which_type_dict = {'teenth': 0, '1st': 1, '2nd': 2, '3rd': 3,
                       '4th': 4, '5th': 5, 'last': 6}

    # Convert weekday and convertion type inputs
    weekday = weekday_dict[day_of_the_week]
    which_type = which_type_dict[which]

    day = False
    for d_w in cal.itermonthdays2(year, month):
        if which_type == 0 \
                and 13 <= d_w[0] <= 19 and d_w[1] == weekday:
            day = d_w[0]

        elif which_type in range(1, 6) \
                and 7 * which_type - 6 <= d_w[0] <= 7 * which_type and d_w[1] == weekday:
            day = d_w[0]

        elif which_type == 6 \
                and 21 <= d_w[0] <= 31 and d_w[1] == weekday:
            day = d_w[0]

    if not day:
        raise MeetupDayException('Invalid Date')

    return datetime.date(year, month, day)


class MeetupDayException(Exception):
    def __init__(self, message):
        self.message = message
