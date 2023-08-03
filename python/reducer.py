#Reducer

import sys

current_movie = None
current_rating = 0


for rows in sys.stdin:
    columns = rows.strip() # removing whitespace
    movie, rating = columns.split('\t') # spliting columns

    try:
        rating = int(rating)
    except ValueError:
        continue

    if current_movie == movie:
        current_rating += rating
        count += 1
    else:
        if current_movie:
            average = round(current_rating/count, 2)
            print(f"{current_movie}\t{average}")

        current_movie = movie
        current_rating = rating
        count = 1

#for last row

average = round(current_rating/count, 2)
print(f"{current_movie}\t{average}")
