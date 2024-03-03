from iqoptionapi.stable_api import IQ_Option


class IQOptionConnector:
    def __init__(self, email, password):
        self.api = IQ_Option(email, password)

    def connect(self, mode="PRACTICE"):
        channel1, channel2 = self.api.connect()
        if channel1:
            self.api.change_balance(mode)
        return channel1

    def get_open_actives(self):
        actives_response = self.api.get_all_open_time()
        actives_binary_options = []

        # Recorrer la estructura de datos
        for category, actives in actives_response.items():
            if category == "binary":
                for active, details in actives.items():
                    if details.get("open", False):
                        actives_binary_options.append(active)

        return actives_binary_options

    def get_candles(self, active, interval, count, endtime):
        print("Getting candles for", active, "with interval", interval)
        candles = self.api.get_candles(active, interval, count, endtime)
        return candles

    # ! No funciona
    def get_last_candle(self, active, interval):
        print("Getting candles for", active, "with interval", interval)
        candles = self.api.get_realtime_candles(active, interval)
        print("Candles", len(candles))
        return candles
