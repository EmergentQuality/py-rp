""" Script used to retrieve data regarding Movies.
Modes:
    `search`: Will search for movies based on a given string
    `ratings`: Will return ratings for movies
Author: Robby Grodin
"""

valid_modes = ['ratings', 'r', 'search', 's']
mode = valid_modes[0]

mode_prompt = "Would you like to 'search' or retrieve 'ratings'?"
mode_reprompt = "Please enter either 'search' or 'ratings'."

default_movie_titles = ["Back to the Future", "Blade", "Spirited Away"]

movie_rating = 8


def print_search_results(movie_titles):
    # Loop through list of titles and print them (indented with 4 spaces).
    for title in movie_titles:
        print(title)

def print_rating(movie_title):
    # Print the whole formatted string
    print("The rating for", movie_title, "is", movie_rating)

def print_all_ratings(movie_titles):
    # Print all great ratings for a movie list
    for movie in movie_titles:
        print_rating(movie)

# Request input from the user to set the mode
def prompt_user_for_mode():
    user_input = input(mode_prompt)
    while user_input not in valid_modes:
        user_input = input(mode_reprompt)
    return user_input

# Create one main function which will call everything else
def main():
    while True:
        # Set the mode variable with user input
        mode = prompt_user_for_mode()

        # Use the `mode` variable to determine which function to call
        if mode == 'search':
            print_search_results(default_movie_titles)
        elif mode == 'ratings':
            print_all_ratings(default_movie_titles)
        else:
            print('Invalid value for mode!')


# This line tells Python to run main() when it first opens.
if __name__ == "__main__":
    main()
