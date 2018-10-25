"""

Jeffrey Liss
jeffrey.liss@gmail.com
2018-10-23T00:02:11.351Z
"""

import random

cards_in_deck = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    "jack",
    "queen",
    "king",
    "ace",
]

cards_dealt = []


def deal(deck):
    cards_dealt.append(random.choice(deck))
    cards_in_deck.pop()
    return deck


def main():
    print(cards_in_deck)
    print(next(deal(cards_in_deck)))
    print(cards_in_deck)
    print(cards_dealt)


if __name__ == '__main__':
    main()
