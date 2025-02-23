from api.api_calls import Api_calls 
from sql.sql import SQL

api_calls = Api_calls()
sql = SQL()
df_forecast = api_calls.prev()
df_historical = api_calls.hist()
sql.insert_forecast(df_forecast)
sql.insert_historical(df_historical)
    