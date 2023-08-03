import pandas as pd

data = pd.read_csv("../data/MovieRating.csv", header=None, names=['CustId', 'Rating', 'Date', 'MovieId', 'YearsOfReleased', 'MovieTitle'])

data = data[['MovieTitle', 'Rating']]
data['Count'] = 1

data_clean = data.groupby(['MovieTitle']).agg(
     Total_Rating = ('Rating','sum'),
     Total_Count = ('Count','sum'),
     ).reset_index()

data_clean['Average'] = round(data_clean['Total_Rating']/data_clean['Total_Count'], 2)

data_clean = data_clean.sort_values(by='Average', ascending=False)

data_top = data_clean.head(10)

for title, average in zip(data_top['MovieTitle'], data_top['Average']):
    print(title, ":", average)
