""" Script to print the title year and tagline for movies in category.

Jeffrey Liss
jeffrey.liss@gmail.com
2018-10-09T20:22:49.836Z
"""

romantic_movie1 = ("The Princess Bride", 1987, 98, "The story of a man and a"
                   " woman who lived happily ever after.",
                   ["Buttercup", "Wesley", "Fezzik", "Inigo Montoya",
                    "Vizzini"])
romantic_movie2 = ("Groundhog Day", 1993, 101, "He's having the day of his"
                   " life… over and over again.", ["Phil Connors"])
romantic_movie3 = ("Amélie", 2001, 122, "One person can change your life"
                   " forever.", ["Amélie Poulain", "Nino Quincampoix",
                                 "The Garden Gnome"])

movie_collection = romantic_movie1, romantic_movie2, romantic_movie3


def retrieve_movie_info(movie):
    return list((movie[0], movie[1], movie[3]))


for m in romantic_movie1, romantic_movie2, romantic_movie3:
    summary = retrieve_movie_info(m)
    print(f"IN A WORLD... {m[0]} ({m[1]}): {m[3]}")
