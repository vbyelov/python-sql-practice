import pandas as pd

# Pandas — Basic practice
#
# Task: average_amount_per_category
#
# You are given a list of dictionaries with sales data:
# Each dictionary contains:
# - "category" : category name (string)
# - "amount"   : sale amount (integer)
#
# Steps:
# 1. Create a pandas DataFrame from the given data
# 2. Filter rows where amount > 150
# 3. Calculate the average amount per category
# 4. Print intermediate results and the final result
#
# Restrictions:
# - Do NOT use apply()
# - Use basic pandas operations only:
#   DataFrame, filtering, groupby, mean
#
# Goal:
# Understand how pandas groupby + mean replaces
# manual loops and dictionaries in pure Python.

data = [
    {"category": "A", "amount": 100},
    {"category": "A", "amount": 200},
    {"category": "B", "amount": 300},
    {"category": "B", "amount": 50},
    {"category": "C", "amount": 400},
]

df = pd.DataFrame(data)
print(df)

filtered_df = df[df["amount"] > 150]
print(filtered_df)

avg_per_category = df.groupby("category")["amount"].mean()
print(avg_per_category)