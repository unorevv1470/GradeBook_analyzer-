import pandas as pd
import numpy as np

df = pd.read_csv("weather.csv")

date_col = df.columns[0]
temp_col = df.columns[1]
rain_col = df.columns[2]
hum_col = df.columns[3]

df = df[[date_col, temp_col, rain_col, hum_col]]
df.columns = ["date", "temperature", "rainfall", "humidity"]

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

for col in ["temperature", "rainfall", "humidity"]:
    df[col] = df[col].fillna(df[col].mean())

df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

temps = df["temperature"].values
print("Temperature Statistics:")
print("Mean:", np.mean(temps))
print("Min:", np.min(temps))
print("Max:", np.max(temps))
print("Std Dev:", np.std(temps))

monthly_mean = df.groupby("month")["temperature"].mean()
yearly_mean = df.groupby("year")["temperature"].mean()
print("\nMonthly Mean Temperature:\n", monthly_mean)
print("\nYearly Mean Temperature:\n", yearly_mean)

season_map = {12:"Winter",1:"Winter",2:"Winter",
              3:"Spring",4:"Spring",5:"Spring",
              6:"Summer",7:"Summer",8:"Summer",
              9:"Autumn",10:"Autumn",11:"Autumn"}
df["season"] = df["month"].map(season_map)
season_stats = df.groupby("season")[["temperature","rainfall","humidity"]].mean()
print("\nSeasonal Average Stats:\n", season_stats)

df.to_csv("cleaned_weather_data.csv", index=False)

report_text = f"""
Weather Data Analysis Report

Daily, monthly, and yearly temperature statistics computed.
Missing values handled.
Seasonal averages calculated.

Temperature Mean: {np.mean(temps):.2f}
Temperature Min: {np.min(temps):.2f}
Temperature Max: {np.max(temps):.2f}
Temperature Std Dev: {np.std(temps):.2f}

Monthly Mean Temperature:
{monthly_mean.to_string()}

Yearly Mean Temperature:
{yearly_mean.to_string()}

Seasonal Average Stats:
{season_stats.to_string()}

Files Exported:
- cleaned_weather_data.csv
- weather_report.md
"""

with open("weather_report.md", "w") as f:
    f.write(report_text)

print("\nProject completed successfully! Check cleaned CSV and report.")
