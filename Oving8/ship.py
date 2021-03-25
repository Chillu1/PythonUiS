from enum import Enum, IntEnum


class Direction(Enum):
    Horizontal = 0
    Vertical = 1


class ShipType(IntEnum):
    Null = 0
    Destroyer = 2
    Submarine = 3  # Right now we only support alias on enum, so two submarines, that's fine for now
    Cruiser = 3
    Battleship = 4
    Carrier = 5


class Ship:
    ship_type: ShipType
    hit_amount: int

    def __init__(self, ship_type: ShipType):
        self.ship_type = ship_type
        self.hit_amount = 0

    def __str__(self):
        return f"ShipType: {self.ship_type.name}"

    def status(self):
        return f"{self}, which has taken {self.hit_amount} hits."

    def hit(self):
        self.hit_amount += 1

    def is_sunk(self):
        return self.hit_amount >= self.ship_type
