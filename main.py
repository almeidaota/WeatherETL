import pandas as pd 
import requests
from datetime import datetime 
import time
from sqlalchemy import create_engine, text
import queries as q

api_key = '' #insert api here
lat = '23.50' #sorocaba lat
lon = "-47.45" #sorocaba lon

def prev():
    answer = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,daily,alerts&appid={api_key}&lang=pt_br')
    if answer.status_code == 200:
        data = answer.json()
        df = data['hourly']
        df = pd.DataFrame(df)
        df = df[['dt', 'temp', 'feels_like', 'humidity', 'dew_point', 'uvi', 'clouds', 'visibility']]
        df['dt'] = df['dt'].apply(lambda x: datetime.utcfromtimestamp(int(x)).strftime('%Y-%m-%d %H:%M:%S'))
        df['temp'] = df['temp'].apply(lambda x: x - 273.15)
        df['feels_like'] = df['feels_like'].apply(lambda x: x - 273.15)
        df = df.tail(24) #pegando as últimas 24 horas
    else:
        print(answer)
    return df
        
def hist():
    now = time.time()
    df = []
    for idx in range(0, 24):
        time_to_be_used = int(now - (idx * 3600))
        answer = requests.get(f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time_to_be_used}&appid={api_key}')
        if answer.status_code == 200:
            data = answer.json()
            data = data['data']
            df.append(data[0])    
                
        else:
            print(answer)
    
    df = pd.DataFrame(df)
    df = df[['dt', 'temp', 'feels_like', 'humidity', 'dew_point', 'uvi', 'clouds', 'visibility', 'wind_deg']]
    df['dt'] = df['dt'].apply(lambda x: datetime.utcfromtimestamp(int(x)).strftime('%Y-%m-%d %H:%M:%S'))
    df['temp'] = df['temp'].apply(lambda x: x - 273.15)
    df['feels_like'] = df['feels_like'].apply(lambda x: x - 273.15)
    return df

            
def engine():
        return engine

def insert_forecast(df_forecast, connection):
        query = text(q.INSERT_FORECAST_DATA)
        for row in df_forecast.itertuples(index=False):
            connection.execute(query, {"day": row.dt,
                                       "temp": row.temp,
                                       "feels_like": row.feels_like,
                                       "humidity": row.humidity,
                                       "dew_point": row.dew_point,
                                       "uvi": row.uvi,
                                       "clouds": row.clouds,
                                       "visibility": row.visibility})
            connection.commit()
        
def connection():
    engine = create_engine(f"mysql+mysqlconnector://user:password@host/weatherapi") #trocar user, password e host
    return engine.connect()

def insert_historical(df_historical, connection):
        query = text(q.INSERT_HISTORICAL_DATA)
        for row in df_historical.itertuples(index=False):
            connection.execute(query, {"day": row.dt,
                                       "temp": row.temp,
                                       "feels_like": row.feels_like,
                                       "humidity": row.humidity,
                                       "dew_point": row.dew_point,
                                       "uvi": row.uvi,
                                       "clouds": row.clouds,
                                       "visibility": row.visibility,
                                       'wind_deg': row.wind_deg})
            connection.commit()
        
if __name__ == '__main__':
    df_forecast = prev()
    df_historical = hist()
    conn = connection()
    insert_forecast(df_forecast, conn)
    insert_historical(df_historical, conn)
    