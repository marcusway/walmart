import pandas as pd
import os 

key_df = pd.read_csv(os.path.join("data", "key.csv"))
train_df = pd.read_csv(os.path.join("data", "train.csv"), parse_dates=[0])
weather_df = pd.read_csv(os.path.join("data", "weather.csv"), parse_dates=[1])
new_df = train_df.merge(key_df, on="store_nbr")
massive_df = new_df.merge(weather_df, on="station_nbr")
massive_df.to_csv(os.path.join("data", "merged.csv"))
