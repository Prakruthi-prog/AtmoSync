import pandas as pd

# Read the weather dataset
df = pd.read_csv("data/raw/weather_data.csv")

# First 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Last 5 rows
print("\nLAST 5 ROWS")
print(df.tail())

# Dataset shape
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns)

# Data types
print("\nDATA TYPES")
print(df.dtypes)

# Dataset information
print("\nDATA INFORMATION")
df.info()

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Basic statistics
print("\nBASIC STATISTICS")
print(df.describe())

# Average temperature
average_temperature = df["Temperature"].mean()

print("\nAVERAGE TEMPERATURE")
print(average_temperature)

# Average temperature by city
print("\nAVERAGE TEMPERATURE BY CITY")
city_temperature = df.groupby("City")["Temperature"].mean()
print(city_temperature)

# Average humidity by city
print("\nAVERAGE HUMIDITY BY CITY")
city_humidity = df.groupby("City")["Humidity"].mean()
print(city_humidity)

# Total rainfall by city
print("\nTOTAL RAINFALL BY CITY")
city_rainfall = df.groupby("City")["Rainfall"].sum()
print(city_rainfall)