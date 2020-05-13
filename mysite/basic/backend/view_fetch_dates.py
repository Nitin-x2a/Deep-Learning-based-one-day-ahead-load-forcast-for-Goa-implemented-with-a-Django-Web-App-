import pandas as pd

df = pd.read_csv(r'basic/data/megawatts.csv')

def start_limit():
  return df['datetime'].iloc[0]

def end_limit():
  return  df['datetime'].iloc[-1]
