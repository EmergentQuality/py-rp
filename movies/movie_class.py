"""

Jeffrey Liss
jeffrey.liss@gmail.com
2018-10-16T22:40:40.992Z
"""


class Movie(object):
    def __init__(self, movie_data):
        self.movie_title = movie_data['title']
        self.movie_rating = movie_data['rating']

    def __str__(self):
        return f'An object of the {self.__class__.__name__} class.'

    def __repr__(self):
        return f'{self.__class__.__name__} -> {self.movie_title!r}, {self.movie_rating!r}'

    def get_title(self):
        return self.movie_title

    def get_rating(self):
        return self.movie_rating


def main():

    movie_row_1 = {'title': 'Jumanji', 'rating': 8}
    movie_row_2 = {'title': 'Spirited Away', 'rating': 10}
    movie1 = Movie(movie_row_1)
    print(movie1)




if __name__ == '__main__':
    """Main is the entry point into the program, and it calls
into the search or ratings functions depending on what the user decides to
do. """
    main()
