
# Author: Jeffrey Liss
import pdb
mode = input("Enter mode (S/R): ").upper()
# The rating for 'Back to the Future' is 88.

# mode = random.choice([True, False])
print(f"The mode is {mode}")

valid_modes = ['ratings', 'search']
mode = valid_modes[0]

titles = ['Back to the Future', 'Spirited Away', 'Raiders of the Lost Ark']
ratings = [7, 10, 9]

movie_ratings = dict(zip(titles, ratings))


def print_rating(title):
    print(f"The rating for {title} is {rating}.")


def print_all_ratings():
    for t, r in movie_ratings:
        print(t, r)


def print_search_results():
    input = print("Enter a title: ")
    print(movie_ratings.get(term))


def main():
    if mode == "R":
        print_all_ratings()
    elif mode == "S":
        print_search_results()
    else:
        print("Don't be an ass.")


if __name__ == '__main__':
    main()
