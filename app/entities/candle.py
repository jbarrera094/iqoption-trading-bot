class Candle:
    def __init__(self, active, start, high, low, close, volume, timestamp):
        self.active = active
        self.start = start
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.active} - {self.start} - {self.high} - {self.low} - {self.close} - {self.volume} - {self.timestamp}"
