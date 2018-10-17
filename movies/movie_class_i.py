"""

Jeffrey Liss
jeffrey.liss@gmail.com
2018-10-16T22:40:40.992Z
"""
# import csv


class Movie(object):
    """Represents a single movie with some basic metadata:
        movie_title = title as released in the source country.
        movie_rating = an arbitrary (for now) int.
        release_year = year the title was released.
    Note that movie_title and release_year should be paired to uniquely identify a movie."""

    def __init__(self, movie_data):
        """Initializes movie_title, movie_rating, and release year from the title, rating, and year in a dict."""
        self.movie_title = movie_data['title']
        self.movie_rating = movie_data['rating']
        self.release_year = movie_data['year']

    def __str__(self):
        return f'An object of the {self.__class__.__name__} class.'

    def __repr__(self):
        return f'{self.__class__.__name__} object -> {self.movie_title!r}, {self.movie_rating!r}, {self.release_year!r}'

    def get_title(self):
        """Return the title of a Movie"""
        return self.movie_title

    def get_rating(self):
        """Return the (int) rating of a movie"""
        return self.movie_rating

    def get_year(self):
        """Return the (int) year of a movie's release"""
        return self.release_year

    def build_movie(self):
        """Returns the movie's title and release year in order to make a unique ID."""
        return f"{self.get_title()} - ({self.get_year()})"


class MovieRelease(object):
    """This class will (eventually) be used to differentiate between releases for the same title (e.g. on Netflix, to Blue-Ray, etc.) Or, it may be converted to a decorator if that makes more sense.
    """

    def __init__(self, movie, format):
        self.movie = movie,
        self.format = format
        print("This movie was released.")
        self.valid_formats = [Blue - Ray, DVD, iTunes, Netflix]

# Open a csv file and get a big list of movies.
# with... try...
# with open(movielist.csv) as movie_list:
#     data = movie_list.read()
#     for row in data:
#         try...
#           Create a Movie object for each row in the file.



movie_row_1 = dict(title='Jumanji', rating=7, year=1995,)
movie_row_2 = dict(title='Spirited Away', rating=10, year=2001)
movie_row_3 = dict(title='Animal House', rating=7, year=1978)

movie1 = Movie(movie_row_1)
movie2 = Movie(movie_row_2)
movie3 = Movie(movie_row_3)

for m in (movie1, movie2, movie3):
    print(m.build_movie)
