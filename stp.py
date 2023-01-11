#!/usr/bin/python3
# ICA 2
import random

# global variables
numberofplayers = 2
player_id = 1
temple_board = []
rows, columns = 5, 8
current_position, next_position = 0, 0
movesleft = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
current_move = -1
player_scores = [0, 0]
gem_collection = [[], []]

Redundant = None

RULES = """\
RULES OF THE GAME
=================

[*] This is a two player game

[*] Players select their move from a list of available moves

[*] The available moves at the start of the game are (0,1,1,2,2,3,3,4,4,5,5,6,6)

[*] Once a move (x) is selected, the player moves (x) spaces across the board
        and the move is removed from the list of available moves

[*] The board is filled with gems randomly placed across 39 spaces. There are:
        - 7 Rubies (R),
        - 7 Emeralds (E),
        - 7 Diamonds (D)
        - 7 Sapphires (S)
        - and 11 Glass Beads (G)

[*] As a player moves across the board, he collects gems from every space they
        move across, including the space where they end their moves on

[*] Upon completion of the game, points are awarded to players based on the
        number of gems they have collected, with each type of gem being tallied
        separately.

        The total number of points earned for a certain type of gem is calculated
        using the following formula: (n * (n + 1)) / 2, where n is the number of
        gems of that type collected.

        For example:
        ------------

        If a player collects 1 gem of a certain type, they earn 1 point.
        If a player collects 2 gems of the same type, they earn 3 points (1 + 2)
        If a player collects 3 gems of the same type, they earn 6 points (1 + 2 + 3)
        If a player collects 4 gems of the same type, they earn 10 points (1 + 2 + 3 + 4)
        and so on.

        This means that for every additional gem of the same type that a player
        collects, they will earn (n+1) more points, where n is the number of gems
        already collected of that type.

[*] All gems have the same scoring system, and sum up to the final score.
        However glassbeads are counted as negative points.

        For example
        -----------

        If a player has 3 diamonds, 2 glass beads and 1 rubies:
        - their diamonds are worth 6 points
        - their glassbeads are worth -3 points
        - and their rubies are worth 1 point.

        Giving a total score of 4 points. Glass beads are negative so they subtract
        from a players total score rather than add to it.

[*] The game ends when a player reaches the final board space.
        The player with the most points is the winner.
"""


# store player names
def getplayers():
    players = []
    taken_names = set()

    for i in range(2):
        while True:
            name = input(f"Enter your name player {i + 1}: ").strip()
            if not name:
                print("\nplease enter a valid name!\n")
            elif name in taken_names:
                print("\nname already taken!\n")
            else:
                taken_names.add(name)
                players.append(name)
                break
    return players


# randomly fill up board with gems and place marker ``*`` at beginning
def board_items():

    Rubies = "R" * 7
    Emeralds = "E" * 7
    Diamonds = "D" * 7
    Sapphires = "S" * 7
    Glass_Beads = "G" * 11
    gems = Rubies + Emeralds + Diamonds + Sapphires + Glass_Beads
    for i in range(len(gems)):
        temple_board.append(gems[i])
    random.shuffle(temple_board)
    temple_board.insert(0, "*")
    return temple_board


def print_board():
    v = '|'
    h = "-"
    c = "+"  # corner character

    for row in range(rows):
        outline = ""
        inside = ""
        for col in range(columns):
            outline += c + h * 3
            inside += f"{v} {temple_board[row * columns + col]} "
        outline += c
        inside += v
        print(outline)
        print(inside)
    print(outline)

# move player position across board


def activemove(players):
    flag = False
    while not flag:
        if player_id == 1:
            print("The available moves left are :", movesleft)
            my_move = input(
                "\n" + players[1] +
                " please choose a number from the available moves left displayed: ")
            try:
                current_move = int(my_move)
                flag = playermovevalid(current_move)
            except:
                print("Invalid choice - Please choose a move from: ", movesleft)
        else:
            print("These are the moves left :", movesleft)
            my_move = input(
                "\n" + players[0] +
                " please choose a number from the available moves left displayed: ")
            try:
                current_move = int(my_move)
                flag = playermovevalid(current_move)
            except:
                print("Invalid choice - Please choose a move from: ", movesleft)

    return current_move


# checks if move is available on the movesleft
def playermovevalid(current_move):

    if current_move in movesleft:
        movesleft.remove(current_move)
        print(movesleft)
        return True
    else:
        print("This is an invalid move. Please choose again: ", movesleft)
        return False


# update player position and gems collected
def update_vars(activeplayermove):
    global current_position, next_position
    next_position = min(current_position + activeplayermove,
                        len(temple_board) - 1)
    temple_board[current_position] = " "
    current_position += 1
    # print("update_vars(): ", activeplayermove, current_position, next_position)
    while current_position <= next_position:

        gem_collection[player_id].append(temple_board[current_position])

        temple_board[current_position] = " "
        current_position += 1
    temple_board[next_position] = "*"
    # print(gem_collection)

    return " "

# condition for ending the game


def gameover(current_position):
    if current_position >= 39:
        return False
    return True


# determine winner
def final_scores(players, gem_collection, player_scores):
    #   print(gem_collection)
    print("\nGame Over")
    print("*" * 30 + "\n")
    for i in range(2):
        rubies = gem_collection[i].count("R")
        emeralds = gem_collection[i].count("E")
        diamonds = gem_collection[i].count("D")
        sapphires = gem_collection[i].count("S")
        glassbeads = gem_collection[i].count("G")
        rubies = rubies / 2 * (rubies + 1)
        emeralds = emeralds / 2 * (emeralds + 1)
        diamonds = diamonds / 2 * (diamonds + 1)
        sapphires = sapphires / 2 * (sapphires + 1)
        glassbeads = glassbeads / 2 * (glassbeads + 1)
        player_scores[i] += rubies + emeralds + \
            diamonds + sapphires - glassbeads
        print(f"{players[i]}'s Score is {player_scores[i]}")
    print("\n" + "*" * 30 + "\n")
    if player_scores[0] == player_scores[1]:
        print("Draw")
    if player_scores[0] > player_scores[1]:
        print(players[0], "is the winner")
    else:
        print(players[1], "is the winner")


# main program #
def start():
    global rows, columns, numberofplayers, player_id, temple_board
    global current_position, next_position
    global player_scores, gem_collection
    print("""
                        +--+--+--+--+--+--+
                        | Sun Temple Game |
                        +--+--+--+--+--+--+
    """)  # display the application name
    print('Win to obtain the power of the sun:)')
    if input("do you want to see the rules? (y/N) ").strip().lower() in ('y', 'yes'):
        print(RULES)
    players = getplayers()
    print("\n")
    temple_board = board_items()
    print_board()

    game_is_running = True
    while game_is_running:

        # determine active player
        player_id = (player_id + 1) % 2
        print("\nIt is ", players[player_id] + "'s turn \n")

        # now get a valid player move
        activeplayermove = activemove(players)
        print("\nYou chose to move", activeplayermove, "Spaces")

        next_position = current_position + activeplayermove

        variables = update_vars(activeplayermove)
        print(variables)

        print_board()
        print("\nPlayer Gems are: ")
        print(f" {players[0]}: {gem_collection[0]}")
        margin = len(players[0])
        divider = len(gem_collection[0]) * 5
        print(
            f"{'-' * (margin // 2)}{'-' * (divider // 2)}>><<{'-' * (divider // 2)}{'-' * (margin // 2)}")
        print(f" {players[1]}: {gem_collection[1]}")

        current_position = next_position

        game_is_running = gameover(current_position)

    final_scores(players, gem_collection, player_scores)


try:
    if __name__ == '__main__':
        start()
except (EOFError, KeyboardInterrupt):
    print('\nBye Bye.....U can always come back again:)')
    print('See you next time')
