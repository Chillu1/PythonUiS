import os

from card import Card
from card_deck import CardDeck
from player import Player
from kabal import Kabal


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    kabal = Kabal()

    game_is_playing = True
    while game_is_playing:
        if kabal.is_game_over():
            game_is_playing = False
            break
        print(kabal.write_status())
        try:
            index_one = int(input("Give one index: "))
            index_two = int(input("Give another index: "))
            index_three = int(input("Give optional another index (-1 for skip): "))
        except ValueError:
            clear_console()
            print("Wrong index value, try again\n")
            continue
        # TODO, refactor
        if index_one > 8 or index_two > 8 or index_one < 0 or index_two < 0 or index_one == index_two \
                or index_three < -1 or index_three > 8 or index_three == index_one or index_three == index_two:
            clear_console()
            print("Wrong index value, try again\n")
            continue

        # Correct numbers, continue the game
        if index_three > -1:
            kabal.place_three_cards(index_one, index_two, index_three)
        else:
            kabal.place_two_cards(index_one, index_two)

        index_three = -1
        input("Enter to continue")
        clear_console()
