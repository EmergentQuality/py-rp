"""

Jeffrey Liss
jeffrey.liss@gmail.com
2018-10-23T00:02:11.351Z
"""

import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace", ]


def deal(deck):
    for i in random.choices(deck, k=5):
        yield([i].pop())


def main():

    random.shuffle(cards)
    print(cards)
    print(next(deal(cards)))


if __name__ == '__main__':
    main()
