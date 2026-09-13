import pandas as pd
import matplotlib.pyplot as plt

# Read the weather dataset
df = pd.read_csv("data/raw/weather_data.csv")

# Calculate average temperature by city
average_temperature = df.groupby("City")["Temperature"].mean()

# Display the result
print("Average Temperature by City:")
print(average_temperature)

# Create a bar graph
average_temperature.plot(kind="bar")

# Add graph title and labels
plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Average Temperature (°C)")

# Make the graph easy to read
plt.xticks(rotation=0)

# Display the graph
plt.show()
plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Average Temperature (°C)")

plt.xticks(rotation=0)

plt.savefig("visualizations/average_temperature_by_city.png")

plt.show()
