import pandas as pd
import os

import kagglehub

# Download latest version
path = kagglehub.dataset_download("christopheiv/winemagdata130k")

csv_path = path + "/winemag-data-130k-v2.csv"

wine_reviews = pd.read_csv(csv_path, index_col=0)
reviews = pd.read_csv(csv_path, index_col=0)

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

# print(wine_reviews.country == 'Italy')
#
# print(wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90)])
#
# print(wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90)])
#
# print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])])

# print(wine_reviews.loc[wine_reviews.price.isnull()])

# print(reviews.points.describe())
# print(reviews.country.describe())
# print(reviews.designation.unique())
# print(reviews.country.value_counts())
#
# reviews['points_centered'] = reviews.points - reviews.points.mean()
# reviews['points_median'] = reviews.points.median()
#
# print(reviews[['points', 'points_centered', 'points_median']].head())
#
# def preobrazovator(points):
#     points = points/100
#     return points
#
# reviews['new_colomn'] = reviews.points.map(preobrazovator)
#
# print(reviews.new_colomn.describe())
# print(reviews.new_colomn.head())


#
# def stars(my_row):
#     if my_row.country == 'Canada':
#         return 3
#     elif my_row.points >= 95:
#         return 3
#     elif my_row.points > 85 and my_row.points < 95:
#         return 2
#     else:
#         return 1
#
#
# star_ratings = reviews.apply(stars, axis = 'columns')
# print(star_ratings)

# print(reviews.groupby('points').points.count())
#
# print(reviews.groupby('country').country.count())
#
# italywines = reviews.loc[reviews['country'] == 'Italy']
#
# print(italywines.groupby('points').points.count())


print(reviews.groupby(['country']).price.agg([len, min, max]))

best_wine_by_price = (
    reviews.groupby('price')
           .points
           .max()
           .sort_index()
)
print(best_wine_by_price)
