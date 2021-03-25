import copy
import numpy

from Oving8.position import Position
from Oving8.ship import *


class Board:
    battleships: list
    placed_battleships: list
    positions: numpy
    shots_amount: int = 0

    def __init__(self, battleships):
        self.battleships = battleships
        self.placed_battleships = list()
        self.positions = numpy.ndarray((10, 10), dtype=Position)  # .arange(100).reshape(10, 10)

        for y in range(10):
            for x in range(10):
                self.positions[y, x] = Position(x, y)

    def draw_player_board(self):
        print(" ", end='')
        for i in range(10):
            print(" ", i, end='')
        print()

        for i in range(10):
            print(i, end="")
            for j in range(10):
                print(" ", self.positions[i, j], end='')
            print()

    def draw_enemy_board(self):
        print(" ", end='')
        for i in range(10):
            print(" ", i, end='')
        print()

        for i in range(10):
            print(i, end="")
            for j in range(10):
                print(" ", self.positions[i, j].enemy_status(), end='')
            print()

    def all_ships_destroyed(self):
        return all(ship.is_sunk() for ship in self.placed_battleships)

    def get_ship_indexes(self):
        return len(self.battleships)

    def print_available_ships(self):
        i: int = 0
        for ship in self.battleships:
            print(f"Index: {i}, {ship}\t Length: {int(ship.ship_type)}")
            i += 1
        i -= 1  # Remove last index change (5)
        return i

    def all_ships_placed(self):
        return len(self.placed_battleships) >= 5

    def try_to_place_ship(self, x_position, y_position, ship: Ship, direction: Direction):
        if self.__is_ship_placed(ship.ship_type):
            return False

        x_length = int(ship.ship_type) if direction == Direction.Horizontal else 1
        y_length = int(ship.ship_type) if direction == Direction.Vertical else 1

        if not self.__is_position_correct(x_position, y_position, x_length, y_length):
            return False

        if self.__is_place_taken(x_position, y_position, x_length, y_length):
            return False

        self.__place_ship(x_position, y_position, ship, x_length, y_length)

        return True

    def shoot_position(self, x_position, y_position):
        if self.positions[y_position, x_position].shoot():
            self.shots_amount += 1
            return True
        print("Position already shot, try again")
        return False

    def __place_ship(self, x_position, y_position, ship: Ship, x_length, y_length):
        ship_copy = copy.copy(ship)

        for y in range(y_position, y_position + y_length):
            for x in range(x_position, x_position + x_length):
                self.positions[y, x].set_ship(ship_copy)

        self.placed_battleships.append(ship_copy)
        self.battleships.remove(ship)

    def __is_ship_placed(self, ship_type: ShipType):
        if ship_type in self.placed_battleships:
            print("Ship already placed")
            return True

        return False

    @staticmethod
    def __is_position_correct(x_position, y_position, x_length, y_length):
        if x_position >= 0 and y_position >= 0 and 10 >= x_position + x_length >= 0 and 10 >= y_position + y_length >= 0:
            return True

        print("Out of bounds ship, try again")
        return False

    def __is_place_taken(self, x_position, y_position, x_length, y_length):
        for y in range(y_position, y_position + y_length):
            for x in range(x_position, x_position + x_length):
                if self.positions[y, x].is_taken:
                    print(f"Position {y, x} is taken, try again")
                    return True
        return False
