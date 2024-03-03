from app.entities.candle import Candle


class CreateCandleUseCase:
    def execute(self, active, start, high, low, close, volume, timestamp):
        # * TODO: Implementar la lógica de negocio
        candle = Candle(active, start, high, low, close, volume, timestamp)
        return candle
