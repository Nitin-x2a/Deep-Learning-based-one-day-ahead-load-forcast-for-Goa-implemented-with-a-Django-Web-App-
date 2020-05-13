import pandas as pd

df = pd.read_csv(r'basic/data/festival.csv')

def start_limit():
  return df['date'].iloc[0]

def end_limit():
  return  df['date'].iloc[-1]
