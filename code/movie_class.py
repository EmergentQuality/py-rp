"""

Jeffrey Liss
jeffrey.liss@gmail.com
2018-10-16T22:40:40.992Z
"""


class Movie(object):
    def __init__(self, movie_data):
        self.movie_title = movie_data['title']
        self.movie_rating = movie_data['rating']

    def get_title():
        return self.movie_title

    def get_rating():
        return self.movie_data

def main():

movie_record_1 = {'title': 'Jumanji', 'rating': 8}
movie1 = Movie(movie_record_1)
print(movie1.movie_title, movie1.movie_rating)

if __name__ == '__main__':
    """Main is the entry point into the program, and it calls
into the search or ratings functions depending on what the user decides to
do. """
    main()
