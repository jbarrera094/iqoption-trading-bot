from app.use_cases.create_candle import CreateCandleUseCase


class CandleController:
    def __init__(self, candle_use_case):
        self.candle_use_case = candle_use_case

    def create(self, active, start, high, low, close, volume, timestamp):
        ## llamar al caso de uso para crear una vela
        candle = self.candle_use_case.execute(
            active, start, high, low, close, volume, timestamp
        )

        ## en un caso real enviaria el correo de notificacion

        return candle
