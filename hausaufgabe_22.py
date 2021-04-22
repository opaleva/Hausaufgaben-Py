class Time:
    def __init__(self, hours, minutes, seconds):
        assert 0 <= minutes < 60, 'Некорректное значение'
        assert 0 <= seconds < 60, 'Некорректное значение'
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def add_time(self, hours2, minutes2, seconds2):
        total_seconds = (self.hours + hours2) * 3600 + (self.minutes + minutes2) * 60 + self.seconds + seconds2
        self.minutes, self.seconds = divmod(total_seconds, 60)
        self.hours, self.minutes = divmod(self.minutes, 60)
        return f'{self.hours:d}:{self.minutes:02d}:{self.seconds:02d}'

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds


def main():
    x = Time(5, 38, 47)
    print(x)
    print(x.add_time(0, 75, 35))


if __name__ == '__main__':
    main()
