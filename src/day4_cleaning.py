import pandas as pd

# -----------------------------------
# STEP 1: Read the raw dataset
# -----------------------------------

df = pd.read_csv("data/raw/weather_data.csv")

print("Original Dataset:")
print(df)

# -----------------------------------
# STEP 2: Check dataset information
# -----------------------------------

print("\nDataset Information:")
print(df.info())

# -----------------------------------
# STEP 3: Check missing values
# -----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------
# STEP 4: Check duplicate rows
# -----------------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# -----------------------------------
# STEP 5: Convert Date column
# -----------------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# -----------------------------------
# STEP 6: Convert numeric columns
# -----------------------------------

numeric_columns = [
    "Temperature",
    "Humidity",
    "Rainfall",
    "Wind_Speed",
    "Pressure"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# -----------------------------------
# STEP 7: Remove duplicate rows
# -----------------------------------

df = df.drop_duplicates()

# -----------------------------------
# STEP 8: Remove rows with missing values
# -----------------------------------

df = df.dropna()

# -----------------------------------
# STEP 9: Validate weather values
# -----------------------------------

df = df[
    (df["Humidity"] >= 0) &
    (df["Humidity"] <= 100) &
    (df["Rainfall"] >= 0) &
    (df["Wind_Speed"] >= 0) &
    (df["Pressure"] > 0)
]

# -----------------------------------
# STEP 10: Save cleaned dataset
# -----------------------------------

df.to_csv(
    "data/processed/cleaned_weather_data.csv",
    index=False
)

# -----------------------------------
# STEP 11: Display final dataset
# -----------------------------------

print("\nCleaned Dataset:")
print(df)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nCleaning completed successfully!")

print("\nSaved file:")
print("data/processed/cleaned_weather_data.csv")
df.to_csv("data/processed/cleaned_weather_data.csv", index=False)