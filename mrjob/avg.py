from mrjob.job import MRJob

class MRAverageRating(MRJob):
    def mapper(self, _, rows):
        rows = rows.strip()
        movie = rows.split(',')
        yield movie[5], movie[1]

    def reducer(self, movie, rating):

        rating_list =[]

        for rate in rating:
            try:
                rate = int(rate)
            except ValueError:
                continue
            rating_list.append(rate)

        total_rating = sum(rating_list)
        count = len(rating_list)

        average = total_rating/count if count > 0 else 0
        average = round(average, 2)
        yield movie, average

if __name__ == '__main__':
   MRAverageRating.run()
