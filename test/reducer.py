import sys

cur_movie = None
cur_rating = 0

for row in sys.stdin:
    movieid, rating = row.strip().split('\t')
    try:
        rating = int(rating)
    except ValueError:
        continue

    if cur_movie == movieid:
        cur_rating += rating
        count += 1
    else:
        if cur_movie:
            avg = round(cur_rating/count, 2)
            print(f"{cur_movie}\t{avg}")
        cur_movie = movieid
        cur_rating = rating
        count = 1

avg = round(cur_rating/count, 2)
print(f"{cur_movie}\t{avg}")
