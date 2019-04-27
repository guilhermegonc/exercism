import datetime
import calendar


def meetup_day(year, month, day_of_the_week, which):
    cal = calendar.Calendar(0)  # Start calendar with monday as first day of the week
    week_day_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                     'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    weekday = week_day_dict[day_of_the_week]

    if which == 'teenth':
        for d_w in cal.itermonthdays2(year, month):
            if 13 <= d_w[0] <= 19 and d_w[1] == weekday:
                day = d_w[0]
        return datetime.date(year, month, day)


class MeetupDayException():
    def __init__(self):
        pass
