# HORISONTAL = 0 JAKUB MROZ
# VERTIKAL = 1
from random import randint


class Skip:
    def __init__(self, start_x, start_y, retning, lengde):
        self.start_x = start_x
        self.start_y = start_y
        self.retning = retning
        self.lengde = lengde
        self.antall_treff = 0

    def __str__(self):
        return f"Skip med startkooridinater ({self.start_x}, {self.start_y}) med " \
            f"lengde {self.lengde}, som har tatt {self.antall_treff} treff."

    def treff(self):
        self.antall_treff += 1

    def er_senket(self):
        if self.antall_treff >= self.lengde:
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.number_of_shots = 0
        self.list_ships = []
        self.ship_number = 0
        self.ships_placed = 0

        # 10x10 matrix, map of shots
        list_inner = [False for x in range(10)]
        self.map_shots = [list_inner.copy() for x in range(10)]

        # 10x10, map of ships
        list_inner2 = [None for x in range(10)]
        self.map_ships = [list_inner2.copy() for x in range(10)]

    def is_within_bounds(self,start_x, start_y, length, direction):
        length_x = length-1 if direction == 0 else 0
        length_y = length-1 if direction == 1 else 0

        if start_x < 10 and start_y < 10 and start_x >= 0 and start_y >= 0 and start_x + length_x < 10 and start_y + length_y < 10:
            return True
        else:
            return False

    def is_position_taken(self, start_x, start_y, length, direction):
        self.count = 0

        for x in range(length):
            if direction == 0:
                if self.map_ships[start_y][start_x + x] is None:
                    self.count += 1

            elif direction == 1:
                if self.map_ships[start_y + x][start_x] is None:
                    self.count += 1

        if self.count == length:
            return True
        else:
            return False

    def place_ship(self, start_x, start_y, length, direction):
        if self.is_within_bounds(start_x, start_y, length, direction) == True and self.is_position_taken(start_x, start_y, length, direction) == True:
            self.list_ships.append(Skip(start_x, start_y, direction, length))

            if direction == 0:
                for x in range(length):
                    self.map_ships[start_y][start_x + x] = self.list_ships[self.ship_number]

            elif direction == 1:
                for x in range(length):
                    self.map_ships[start_y + x][start_x] = self.list_ships[self.ship_number]

            self.ship_number += 1
        else:
            return False

    def shoot(self, coord_x, coord_y):
        self.shotat = 0
        if self.map_shots[coord_y][coord_x] == False:
            if self.map_ships[coord_y][coord_x] is not None:
                self.map_ships[coord_y][coord_x].treff()
            self.map_shots[coord_y][coord_x] = True
            self.number_of_shots += 1
        else:
            #print("\nThis tile was already shot at.")
            self.shotat = 1

    def tile_status(self, x, y):
        if self.map_shots[y][x] == False:
            return 1 # not shot at

        elif self.map_shots[y][x] == True:
            if self.map_ships[y][x] == None:
                return 2 # shot at but empty

            elif self.map_ships[y][x] != None:
                if self.map_ships[y][x].er_senket() == True:
                    return 3 # shot at and sunk
                else:
                    return 4 # shot at but still alive
    def victory(self):
        if all(ship.er_senket() for ship in self.list_ships):
            #print(f"You have won with {self.number_of_shots} shots.")
            return True
        else:
            return False

    def random_ship(self, length, amount):
        while self.ship_number < self.ships_placed + amount:
            self.place_ship(randint(0, 9), randint(0, 9), length, randint(0, 1))
        self.ships_placed += amount
