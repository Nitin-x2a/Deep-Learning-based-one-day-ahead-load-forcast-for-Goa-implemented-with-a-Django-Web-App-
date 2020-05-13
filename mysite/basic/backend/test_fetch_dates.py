import pandas as pd
import datetime

df = pd.read_csv(r'basic/data/megawatts.csv')
df['datetime'] = pd.to_datetime(df['datetime'])

def start_limit():
  return datetime.datetime.strftime(df['datetime'].iloc[0] + datetime.timedelta(minutes=15*(12*7*96+15*96+8)), format='%Y-%m-%d %H:%M')

def end_limit():
  return  datetime.datetime.strftime(df['datetime'].iloc[-1], format='%Y-%m-%d %H:%M')
