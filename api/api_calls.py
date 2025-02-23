import requests
import time
import os
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timezone


class Api_calls():
    def __init__(self):
        dotenv_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path)
        self.api_key = os.getenv('api_key')
        self.lat = os.getenv('lat')
        self.lon = os.getenv('lon')

    def prev(self):
        answer = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&exclude=minutely,daily,alerts&appid={self.api_key}&lang=pt_br')
        if answer.status_code == 200:
            data = answer.json()
            df = data['hourly']
            df = pd.DataFrame(df)
            df = df[['dt', 'temp', 'feels_like', 'humidity', 'dew_point', 'uvi', 'clouds', 'visibility']]
            df['dt'] = df['dt'].apply(lambda x: datetime.fromtimestamp(int(x), tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
            df['temp'] = df['temp'].apply(lambda x: x - 273.15)
            df['feels_like'] = df['feels_like'].apply(lambda x: x - 273.15)
            df = df.tail(24) #pegando as últimas 24 horas
        else:
            print(answer)
        return df
        
    def hist(self):
        now = time.time()
        df = []
        for idx in range(0, 24):
            time_to_be_used = int(now - (idx * 3600))
            answer = requests.get(f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={self.lat}&lon={self.lon}&dt={time_to_be_used}&appid={self.api_key}')
            if answer.status_code == 200:
                data = answer.json()
                data = data['data']
                df.append(data[0])    
                
            else:
                print(answer)
    
        df = pd.DataFrame(df)
        df = df[['dt', 'temp', 'feels_like', 'humidity', 'dew_point', 'uvi', 'clouds', 'visibility', 'wind_deg']]
        df['dt'] = df['dt'].apply(lambda x: datetime.fromtimestamp(int(x), tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
        df['temp'] = df['temp'].apply(lambda x: x - 273.15)
        df['feels_like'] = df['feels_like'].apply(lambda x: x - 273.15)
        return df