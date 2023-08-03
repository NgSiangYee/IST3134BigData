\#Mapper

import sys

for rows in sys.stdin:
    columns = rows.strip() # removing whitespace
    columns = columns.split(',') # spliting columns

    title = columns[5]
    rating = columns[1]

    print(f"{title}\t{rating}")
