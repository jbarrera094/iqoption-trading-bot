import os
import time
from datetime import datetime
from dotenv import load_dotenv
from frameworks.api.iqoption_connector import IQOptionConnector
from frameworks.database.mysql_connector import MySQLConnector
from app.interfaces.candle_controller import CandleController
from app.use_cases.create_candle import CreateCandleUseCase

# *Load the environment variables
load_dotenv()
db_host = os.getenv("DB_HOST")
db_database = os.getenv("DB_DATABASE")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
iq_email = os.getenv("IQ_EMAIL")
iq_password = os.getenv("IQ_PASSWORD")
iq_mode = os.getenv("IQ_MODE")
iq_period = int(os.getenv("IQ_PERIOD"))
delay = int(os.getenv("DELAY"))
print(f"Delay: {delay}")
print(f"Period: {iq_period}")

# Initialize depedencies
mysql_connector = MySQLConnector(
    host=db_host, user=db_user, password=db_password, database=db_database
)
create_candle_use_case = CreateCandleUseCase()
api_iqoption = IQOptionConnector(email=iq_email, password=iq_password)

# Conectar a la api de IQ Option y obtener los activos
actives = []
if api_iqoption.connect(mode=iq_mode):
    actives = api_iqoption.get_open_actives()
else:
    print("No se pudo conectar a la API de IQ Option")
    mysql_connector.close()
    exit()

# Inyectar las  dependencias
candle_controller = CandleController(create_candle_use_case)

while True:
    try:
        actives = api_iqoption.get_open_actives()

        for active in actives:
            # Obtener las velas de un activo
            candles = api_iqoption.get_candles(active, iq_period, 1, time.time())
            for candle in candles:
                # Simula una solicitud de registro de vela
                candle_created = candle_controller.create(
                    active=active,
                    start=candle["open"],
                    high=candle["max"],
                    low=candle["min"],
                    close=candle["close"],
                    volume=candle["volume"],
                    timestamp=datetime.utcfromtimestamp(candle["from"]).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                )

                # print(candle_created)
                # save candle
                mysql_connector.save_candle(candle_created)

        # hacer el Commit
        mysql_connector.commit()
        time.sleep(delay)
    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C)
        print("Interrupción del usuario. Saliendo...")
        break
    except Exception as e:
        print(f"Error: {e}")
        # Maneja otros errores y espera antes de intentar nuevamente
        time.sleep(10)

# Cerrar la conexión
mysql_connector.close()
