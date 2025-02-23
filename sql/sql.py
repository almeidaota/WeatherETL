import os
import sql.queries as q
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine, text



class SQL():
    def __init__(self):
        dotenv_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path)
        self.db_user = os.getenv('db_user')
        self.db_host = os.getenv('db_host')
        self.db_password = os.getenv('db_password')
        self.connection = create_engine(f"mysql+mysqlconnector://{self.db_user}:{self.db_password}@{self.db_host}/weatherapi").connect()
        

    def insert_forecast(self, df_forecast):
            query = text(q.INSERT_FORECAST_DATA)
            for row in df_forecast.itertuples(index=False):
                self.connection.execute(query, {"day": row.dt,
                                        "temp": row.temp,
                                        "feels_like": row.feels_like,
                                        "humidity": row.humidity,
                                        "dew_point": row.dew_point,
                                        "uvi": row.uvi,
                                        "clouds": row.clouds,
                                        "visibility": row.visibility})
                self.connection.commit()
            
    def insert_historical(self, df_historical):
            query = text(q.INSERT_HISTORICAL_DATA)
            for row in df_historical.itertuples(index=False):
                self.connection.execute(query, {"day": row.dt,
                                        "temp": row.temp,
                                        "feels_like": row.feels_like,
                                        "humidity": row.humidity,
                                        "dew_point": row.dew_point,
                                        "uvi": row.uvi,
                                        "clouds": row.clouds,
                                        "visibility": row.visibility,
                                        'wind_deg': row.wind_deg})
                self.connection.commit()
            