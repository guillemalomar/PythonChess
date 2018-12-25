import time


class Timer:
    def __init__(self):
        self.start = 0
        self.current = 0
        self.total = 0.0

    def start_time(self):
        self.start = time.time()

    def pause_time(self):
        if self.start != 0:
            self.total += time.time() - self.start

    def format_time(self):

        hours = int(self.total / 3600)
        minutes = int((self.total - hours) / 60)
        seconds = int(self.total - minutes)
        milliseconds = self.total - int(self.total)

        hours = str(hours)
        minutes = str(minutes)
        seconds = str(seconds)
        milliseconds = str(milliseconds).split('.')[1]

        if len(hours) < 2:
            hours = '0' + hours
        if len(minutes) < 2:
            minutes = '0' + minutes
        if len(seconds) < 2:
            seconds = '0' + seconds

        return hours + ':' + minutes + ':' + seconds + ',' + milliseconds


black_timer = Timer()
white_timer = Timer()
