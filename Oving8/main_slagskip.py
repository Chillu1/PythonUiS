import os
import random

from Oving8.board import *


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def setup_ships():
    battleships_setup = list()

    battleships_setup.append(Ship(ShipType.Carrier))
    battleships_setup.append(Ship(ShipType.Battleship))
    battleships_setup.append(Ship(ShipType.Cruiser))
    battleships_setup.append(Ship(ShipType.Submarine))
    battleships_setup.append(Ship(ShipType.Destroyer))
    return battleships_setup


if __name__ == "__main__":
    board = Board(setup_ships())
    game_is_playing = True

    while not board.all_ships_placed():
        #break
        clear_console()
        board.draw_player_board()
        max_index = board.print_available_ships()
        print("Place a ship on the board")
        try:
            index = int(input("Give a ship index: "))
            if index < 0 or index > max_index:
                continue

            pos_x = int(input("Give position x: "))
            pos_y = int(input("Give position y: "))
            direction: Direction = Direction(int(input("Give direction, 0 = Horizontal, 1 = Vertical: ")))

            if board.try_to_place_ship(pos_x, pos_y, board.battleships[index], direction):
                print("Ship placed successfully")
            else:
                print("Ship could not be placed successfully, press enter to continue")
                input()

        except ValueError:
            print("Wrong number, press enter to continue")
            input()
            continue

    enemy_board = Board(setup_ships())

    while not enemy_board.all_ships_placed():
        index = random.randrange(0, enemy_board.get_ship_indexes())
        pos_x = random.randrange(0, 10)
        pos_y = random.randrange(0, 10)
        direction = random.choice([Direction.Horizontal, Direction.Vertical])
        enemy_board.try_to_place_ship(pos_x, pos_y, enemy_board.battleships[index], direction)

    while not enemy_board.all_ships_destroyed():
        clear_console()
        #enemy_board.draw_player_board() # For testing
        enemy_board.draw_enemy_board()
        print("Pick coordinates to shoot: ")
        try:
            pos_x = int(input("Give position x: "))
            pos_y = int(input("Give position y: "))
        except ValueError:
            continue

        if pos_x < 0 or pos_x > 9 or pos_y < 0 or pos_y > 9:
            continue

        if (enemy_board.shoot_position(pos_x, pos_y)):
            pass
        else:
            input("Press enter to continue")

    #pos: Position
    #test = sum([pos.shot == True for pos in enemy_board.positions)#Couødn't figure this out
    # test = sum(map(lambda pos : pos.shot, enemy_board.positions))
    # test = numpy.sum(enemy_board.positions.sum()
    clear_console()
    enemy_board.draw_enemy_board()
    print(f"Congratulations, you won. In {enemy_board.shots_amount} shots")
