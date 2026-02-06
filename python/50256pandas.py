import pandas as pd
import os

import kagglehub

# Download latest version
path = kagglehub.dataset_download("christopheiv/winemagdata130k")

csv_path = path + "/winemag-data-130k-v2.csv"

wine_reviews = pd.read_csv(csv_path, index_col=0)

pd.set_option('display.max_rows', 25)
# print(wine_reviews.shape)
# print(wine_reviews.head())
#
# print(wine_reviews.country.unique())
# print(wine_reviews.isnull().sum())

# print(wine_reviews['country'][3:-5])
# print(wine_reviews.iloc[:-2])
# print(wine_reviews.loc[wine_reviews['province']])

print(wine_reviews.iloc[0,1])

# print(wine_reviews.loc[wine_reviews['country'] == 'Italy'], ['country', 'province', 'points'])
#
# print(
#     wine_reviews.loc[
#         wine_reviews['country'] == 'Italy',
#         ['country', 'province', 'points']
#     ]
# )

print(wine_reviews.country == 'Italy')

print(wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90)])

print(wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90)])

print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])])

print(reviews.loc[reviews.price.notnull()])