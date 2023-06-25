import pandas as pd

from optimal_purchase import optimal_purchase

df = pd.read_csv("train_dataframe.csv")
prices = list(df['Цена на арматуру'])
bought, remained = optimal_purchase(prices, 10)
total_cost = sum([bought[i]*prices[i] for i in range(len(prices))])
print(total_cost)
