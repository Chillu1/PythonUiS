from abc import abstractmethod, ABC

from Oving9.player import Player


class Square(ABC):
    __position: int

    def __init__(self, position: int):
        self.__position = position

    @abstractmethod
    def move(self, player: Player):
        return str(self.__position)

    @property
    def get_position(self):
        return self.__position


class NormalSquare(Square):

    #def __init__(self, position: int):
    #   super().__init__(position)

    def move(self, player: Player):
        old_position = player.points
        player.points = self.get_position
        return f"Player has moved to position {player.points}, from {old_position}\nNormalSquares position is {self.get_position}"


class BackToStartSquare(Square):

    def move(self, player: Player):
        old_position = player.points
        player.points = 0
        return f"Player has been moved back to position {player.points}, from {old_position}\nBackToStartSquare position is {self.get_position}"


class HindranceSquare(Square):

    def move(self, player: Player):
        return f"Player has been stopped at position {player.points}\nHindranceSquare position is {self.get_position}"
