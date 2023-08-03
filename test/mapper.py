import sys

for row in sys.stdin:
    col = row.strip().split(',')
    movieid = col[3]
    rating = col[1]
    print(f"{movieid}\t{rating}")
