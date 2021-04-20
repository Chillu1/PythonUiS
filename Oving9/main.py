import random

from Oving9.dice import Dice
from Oving9.square import *  # NormalSquare, BackToStartSquare, Square, HindranceSquare

game_is_over = False
dev_mode = False

if __name__ == "__main__":
    squares = list()
    for position in range(20):
        random_number = random.randrange(0, 101)
        square: Square
        if random_number <= 70:  # 70%
            square = NormalSquare(position)
        elif random_number <= 90:  # 20%
            square = HindranceSquare(position)
        else:  # 10%
            square = BackToStartSquare(position)
        squares.append(square)
        if dev_mode:
            print(square.__class__.__name__)

    dice = Dice()
    players = list()
    players.append(Player("Tom"))
    players.append(Player("Jeff"))
    players.append(Player("Garry"))
    players.append(Player("Adam"))
    round: int = 0

    while not game_is_over:
        round += 1
        print(f"\n\n\nRound {round}\n\n\n")
        for player in players:
            print(player)
            rolled_number = dice.throw()
            print(f"Rolled {rolled_number}")
            if rolled_number + player.points >= 20:
                game_is_over = True
                print(f"Congratulations {player.info()}, you won!")
                input()
                break
            print(squares[rolled_number + player.points].move(player)+"\n")

        input("Enter to continue")
