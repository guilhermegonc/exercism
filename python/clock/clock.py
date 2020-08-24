class Clock:
    def __init__(self, hour, minute):
        time_delta = divmod(minute, 60)
        self.minute = time_delta[1]
        self.hour = divmod(hour + time_delta[0], 24)[1]

    def __repr__(self):
        return '{:0>2}:{:0>2}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return self.__add__(minutes * -1)
