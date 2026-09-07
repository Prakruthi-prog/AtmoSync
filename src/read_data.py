import pandas as pd

df = pd.read_csv("data/raw/weather_data.csv")

print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

average_temperature = df["Temperature"].mean()

print("\nAverage Temperature:")
print(average_temperature)