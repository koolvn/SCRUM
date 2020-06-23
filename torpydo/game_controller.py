import random

from torpydo.ship import Color, Letter, Position, Ship


class GameController(object):
    def check_is_hit(ships: list, shot: Position):
        if ships is None:
            raise ValueError('ships is null')

        if shot is None:
            raise ValueError('shot is null')

        for ship in ships:
            for position in ship.positions:
                if position == shot:
                    return True

        return False

    def initialize_ships():
        return [
            Ship("Aircraft Carrier", 5, Color.CADET_BLUE),
            Ship("Battleship", 4, Color.RED),
            Ship("Submarine", 3, Color.CHARTREUSE),
            Ship("Destroyer", 3, Color.YELLOW),
            Ship("Patrol Boat", 2, Color.ORANGE)]

    def is_ship_valid(ship: Ship):
        is_valid = len(ship.positions) == ship.size

        return is_valid

    def get_random_position(size: int):
        letter = random.choice(list(Letter))
        number = random.randrange(size)
        position = Position(letter, number)

        return position

    def validate_position(position):
        while True:
            if position.upper()[0] not in Letter._member_names_:
                print('Sorry this LETTER is not available in this game.\n')
                position = input('Please try again:\n')

            elif len(position) != 2 or not position[0].isalpha() or not position[1].isdigit():
                print('Sorry but you have to input only two symbols,'
                      ' so the position should contain column LETTER and row NUMBER. E.g. A5\n')
                position = input('Please try again:\n')
            else:
                break
        return position