import random
import colorama
from colorama import Fore, Back, Style
from torpydo.ship import Color, Letter, Position, Ship
from torpydo.game_controller import GameController

myFleet = []
enemyFleet = []
player = None


def main():
    colorama.init(convert=True)
    print(Fore.YELLOW + r"""
                                    |__
                                    |\/
                                    ---
                                    / | [
                             !      | |||
                           _/|     _/|-++'
                       +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                        Welcome to Battleship                         BB-61/
 \_________________________________________________________________________|""" + Style.RESET_ALL)

    initialize_game()
    start_game()


def show_rules():
    # TODO: написать правила игры
    print('''
    ''')


def show_grid(shots_and_pos):
    # TODO: Переделать в класс. Нужно запоминать и отрисовывать выстрелы и расстановку кораблей.
    print('''
       |   |   |   |   |   |   |   |   | 
    ___|_A_|_B_|_C_|_D_|_E_|_F_|_G_|_H_|___
    _1_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _2_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _3_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _4_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _5_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _6_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _7_|{}|{}|{}|{}|{}|{}|{}|{}|___
    _8_|{}|{}|{}|{}|{}|{}|{}|{}|___
       |   |   |   |   |   |   |   |   |
    '''.format(*shots_and_pos))


def start_game():
    global myFleet, enemyFleet

    print(r'''
    #### WARSHIPS ####
    ##### SCRUM #####
    #### BATTLE #####
        *         __
      *    *     /|| \
           .-.  |  o |
       _.-'  \  | Oo |
    .-'       \  \__/
   /  SUSHA   _/
   |      _  /
   |     /_\
    \    \_/
     """"""""
     ________________
     ver. 0.1
     ''')

    while True:
        # TODO: Избавится от бесконечного цикла
        print("It's your turn,", Fore.CYAN + f"{player}" + Style.RESET_ALL)
        show_grid(
            [Fore.GREEN + '_X_' + Style.RESET_ALL if (x // 2 == 0) else Fore.RED + '_X_' + Style.RESET_ALL for x in
             range(100, 164)])
        position = parse_position(input("Enter coordinates for your shot :"))
        is_hit = GameController.check_is_hit(enemyFleet, position)
        if is_hit:
            print(Fore.LIGHTRED_EX + r'''
                \          .  ./
              \   .:"";'.:..""   /d
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''' + Style.RESET_ALL)

        print("Yeah ! Nice hit !" if is_hit else Fore.LIGHTBLACK_EX + "Miss" + Style.RESET_ALL)

        position = get_random_position()
        is_hit = GameController.check_is_hit(myFleet, position)
        print()
        print(
            f"Computer shoot in {position.column.name}{position.row} and {'hit your ship!' if is_hit else Fore.LIGHTBLUE_EX + 'miss' + Style.RESET_ALL}")
        if is_hit:
            print(Fore.MAGENTA + r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''' + Style.RESET_ALL)


def parse_position(position: str):
    """ Проверяет позицию """
    # TODO: Нельзя стрелять дважды в одну и ту же клетку
    # TODO: Показывать выбранную клетку на карте
    position = GameController.validate_position(position)

    letter = Letter[position.upper()[0]]
    number = int(position[1])
    position = Position(letter, number)

    return position


def get_random_position():
    # TODO: Docstring
    rows = 8
    lines = 8

    letter = Letter(random.randint(1, lines))
    number = random.randint(1, rows)
    position = Position(letter, number)

    return position


def initialize_game():
    # TODO: Докстринг
    global player
    player = input('Enter your name: ')
    initialize_myFleet()

    initialize_enemyFleet()


def initialize_myFleet():
    # TODO: Докстринг
    # TODO: Корабли должны выставлятся согласно правил игры
    global myFleet

    myFleet = GameController.initialize_ships()
    show_grid([Back.BLUE + Fore.BLACK + '___' + Style.RESET_ALL for x in range(64)])
    show_grid([Fore.GREEN + '_X_' + Style.RESET_ALL if (x % 2 == 0) else Fore.RED + '_X_' + Style.RESET_ALL for x in
               range(100, 164)])

    print("Please position your fleet (Game board has size from A to H and 1 to 8) :")

    for ship in myFleet:
        print()
        print(Fore.BLUE + f"Please enter the positions for the {ship.name} (size: {ship.size})" + Style.RESET_ALL)

        for i in range(ship.size):
            position_input = input(f"Enter position {i} of {ship.size} (i.e A3):")

            ship.add_position(position_input)
    print([_ship.positions for i, _ship in enumerate(myFleet)])


def initialize_enemyFleet():
    # TODO: Корабли противника должны выставлятся случайным образом
    # TODO: Докстринг
    global enemyFleet
    import numpy as np
    col_mapper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    ivn_col_mapper = {v: k for k, v in col_mapper.items()}

    def add_ship_position(size: int, ship=Ship) -> None:
        for i in range(size):
            col_letter = lambda x: ivn_col_mapper[np.random.randint(1, 9, x)[0]]
            row_num = lambda x: np.random.randint(1, 9, x)[0]
            rand_col = Letter.__dict__['_member_map_'][col_letter(1)]
            rand_row = row_num(1)
            ship.positions.append(Position(rand_col, rand_row))
        return None

    enemyFleet = GameController.initialize_ships()
    [add_ship_position(ship.size, ship) for ship in enemyFleet]

    # print('DEBUG:', [(_ship.name, _ship.positions) for _ship in enemyFleet])


if __name__ == '__main__':
    main()
