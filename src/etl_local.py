import pandas as pd

df = pd.read_csv('src/sales_data.csv')
# Clean data: Remove any rows with NAs, fix data types, engineering features
df_clean = df.dropna()
df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'])
df_clean['day_of_week'] = df_clean['timestamp'].dt.day_name()

df_clean.to_csv('src/sales_data_clean.csv', index=False)
print("Made: src/sales_data_clean.csv")
