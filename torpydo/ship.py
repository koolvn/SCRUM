from enum import Enum


class Color(Enum):
    # TODO: Применить эти цвета
    CADET_BLUE = 1
    CHARTREUSE = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5


class Letter(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8


class Position(object):
    def __init__(self, column: Letter, row: int):
        self.column = column
        self.row = row

    def __eq__(self, other):
        """ Проверяет позицию на равенство other
        :param other: другая позиция
        :return: True/False
        """
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"{self.column.name}{self.row}"

    __repr__ = __str__


class Ship(object):
    def __init__(self, name: str, size: int, color: Color):
        self.name = name
        self.size = size
        self.color = color
        self.positions = []

    def add_position(self, position: str):
        # TODO: Корабль должен выставлятся согласно правил игры
        from torpydo.game_controller import GameController
        position = GameController.validate_position(position)

        letter = Letter[position.upper()[0]]
        number = int(position[1])
        self.positions.append(Position(letter, number))
        return position

    def __str__(self):
        return f"{self.color.name} {self.name} ({self.size}): {self.positions}"

    __repr__ = __str__
