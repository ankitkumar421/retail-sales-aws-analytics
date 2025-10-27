import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

products = ['Bootleg Red', 'Chardonnay', 'Merlot', 'Cabernet', 'Pinot Noir']
num_rows = 10000
start_date = datetime(2022, 1, 1)

data = []

for i in range(num_rows):
    sale_id = i + 1
    timestamp = start_date + timedelta(minutes=random.randint(0, 100000))
    product = random.choice(products)
    quantity = random.randint(1, 5)
    price = round(random.uniform(10, 100), 2)
    data.append([sale_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), product, quantity, price])

df = pd.DataFrame(data, columns=['sale_id', 'timestamp', 'product', 'quantity', 'price'])
df.to_csv('src/sales_data.csv', index=False)
print("Data generated: src/sales_data.csv")
