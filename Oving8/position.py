from Oving8.ship import Ship


class Position:
    shot: bool
    __ship: Ship

    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.shot = False
        self.__ship = None

    @property
    def is_taken(self):
        return self.__ship is not None

    def shoot(self):
        if self.shot:
            return False  # Trying to shoot the place twice
        self.shot = True
        if self.is_taken:
            self.__ship.hit()
        return True

    def set_ship(self, ship: Ship):
        self.__ship = ship

    def enemy_status(self):
        if self.shot and self.is_taken and self.__ship.is_sunk():
            return "Ø"
        if self.shot and self.is_taken:
            return "S"
        if self.shot:
            return "o"
        return "~"

    def __str__(self):
        if self.shot and self.is_taken and self.__ship.is_sunk():
            return "Ø"
        if self.shot and self.is_taken:
            return "S"
        if self.shot:
            return "o"
        if self.is_taken:
            return "M"
        return "~"
