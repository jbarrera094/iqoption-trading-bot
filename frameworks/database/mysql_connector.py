import mysql.connector


class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.connection.cursor()

    def execute(self, query, values=None):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def save_candle(self, candle):
        query = "INSERT INTO candles (active, start, high, low, close, volume, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (
            candle.active,
            candle.start,
            candle.high,
            candle.low,
            candle.close,
            candle.volume,
            candle.timestamp,
        )
        self.execute(query, values)
        self.commit()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
