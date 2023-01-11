#!/usr/bin/python3
# ICA 2
import random

# global variables
numberofplayers = 2  # number of players in the game
player_id = 1  # keep track of current player
temple_board = []  # board filled with gems and marker
rows, columns = 5, 8  # size of the board
# current and next position of the player
current_position, next_position = 0, 0
# possible moves at the start of the game
movesleft = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
current_move = -1  # track the current move
player_scores = [0, 0]  # store scores for each player
gem_collection = [[], []]  # store collection of gems for each player
Redundant = None

# game instructions
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
    players = []  # list to store player names
    taken_names = set()  # set to keep track of taken names

    for i in range(2):
        while True:
            # ask for player's name
            name = input(f"Enter your name player {i + 1}: ").strip()
            if not name:  # check for empty input
                print("\nplease enter a valid name!\n")
            elif name in taken_names:  # check if name is already taken
                print("\nname already taken!\n")
            else:
                taken_names.add(name)  # add the name to taken names set
                players.append(name)  # append the name to players list
                break
    return players


# randomly fill up board with gems and place marker ``*`` at beginning
def board_items():
    """
    This function sets up the game board by filling it with a set number of gems 
    (7 rubies, 7 emeralds, 7 diamonds, 7 sapphires, and 11 glass beads) in a random order.
    It also inserts a marker "*" at the beginning of the board to indicate the starting position of the players.
    """
    gems = ["R"]*7 + ["E"]*7 + ["D"]*7 + ["S"]*7 + ["G"]*11
    random.shuffle(gems)
    gems.insert(0, "*")
    return gems


def print_board():
    """
    This function prints the game board using the characters '|', '-' and '+'
    """
    # characters to use for drawing the board
    v = '|'  # character for vertical line
    h = "-"  # character for horizontal line
    c = "+"  # corner character

    # loop through rows of the board
    for row in range(rows):
        outline = ""  # Initialize outline string
        inside = ""   # Initialize inside string
        # loop through columns of the board
        for col in range(columns):
            outline += c + h * 3   # add corner and horizontal line to outline
            # add vertical line and board element to inside
            inside += f"{v} {temple_board[row * columns + col]} "
        outline += c  # add corner to the end of outline
        inside += v   # add vertical line to the end of inside
        print(outline)  # print the outline
        print(inside)  # print the inside
    print(outline)  # print the final outline


def activemove(players):
    """
    The function prompts the current player to make a move, and validates the input.
    It will keep prompting the player until a valid move is made.

    Parameters:
    players (List[str]): list of player names, with the current player in the first index

    Returns:
    int: current move made by the player
    """
    flag = False
    while not flag:
        # check if it is player 1's turn
        if player_id == 1:
            print("The available moves left are :", movesleft)
            my_move = input(
                "\n" + players[1] +
                " please choose a number from the available moves left displayed: ")
            try:
                current_move = int(my_move)
                flag = check_valid_playermove(current_move)
            except:
                print("Invalid choice - Please choose a move from: ", movesleft)
        else:
            print("These are the moves left :", movesleft)
            my_move = input(
                "\n" + players[0] +
                " please choose a number from the available moves left displayed: ")
            try:
                current_move = int(my_move)
                flag = check_valid_playermove(current_move)
            except:
                print("Invalid choice - Please choose a move from: ", movesleft)

    return current_move


def check_valid_playermove(current_move):
    """
    The function checks if the move made by the player is valid by checking if it is in the list of available moves

    Parameters:
    current_move (int): the move made by the player

    Returns:
    bool: True if the move is valid, False if the move is invalid.
    """
    if current_move in movesleft:
        movesleft.remove(current_move)
        print(movesleft)
        return True
    else:
        print("This is an invalid move. Please choose again: ", movesleft)
        return False


def update_variables(activeplayermove):
    """
    The function updates the player position and gems collected based on the move made.

    Parameters:
    activeplayermove (int): the move made by the player

    Returns:
    str: " " indicating the function is updating variables and not returning any value.
    """
    global current_position, next_position
    next_position = min(current_position + activeplayermove,
                        len(temple_board) - 1)  # ensures next position doesn't exceed the size of the board
    temple_board[current_position] = " "  # set the current position to empty
    current_position += 1
    # loop through the path the player took to their next position
    while current_position <= next_position:
        # append the gem collected by the player
        gem_collection[player_id].append(temple_board[current_position])
        temple_board[current_position] = " "  # set the path to empty
        current_position += 1
    temple_board[next_position] = "*"  # mark the next position on the board
    # print(gem_collection)
    return " "


# condition for ending the game


def is_game_on(current_position):
    """
    The function checks if the game is over by checking if the current position of the player has reached the end of the board.
    If the current position is greater than or equal to the maximum position of the board (39), the game is over.
    Otherwise, the game is still on.
    Parameters:
    current_position (int): the current position of the player on the board.
    Returns:
    bool: True if the game is on, False if the game is over.
    """
    if current_position >= 39:
        return False
    return True


# determine winner
def determine_winner(players, gem_collection, player_scores):
    """
    Calculate the scores of each player based on the gems they collected.
    Args:
        players: A list of names of the players
        gem_collection: A list of strings representing the collection of gems for each player.
            Each string is a collection of gems represented by the first letter of their name 
        player_scores: A list of integers representing the initial score of each player

    Returns: None, but prints the final scores and the winner of the game
    """
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


# main program
def start():
    global rows, columns, numberofplayers, player_id, temple_board
    global current_position, next_position
    global player_scores, gem_collection

    # display the application name
    print("""
                        +--+--+--+--+--+--+
                        | Sun Temple Game |
                        +--+--+--+--+--+--+
    """)

    print('Win to obtain the power of the sun:)')
    # check if player wants to see rules
    if input("do you want to see the rules? (y/N) ").strip().lower() in ('y', 'yes'):
        print(RULES)
    players = getplayers()  # get the number of players
    print("\n")
    temple_board = board_items()  # generate the board
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

        variables = update_variables(activeplayermove)
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

        game_is_running = is_game_on(current_position)

    determine_winner(players, gem_collection, player_scores)


# Handle keyboard interrupt and end of file errors
try:
    if __name__ == '__main__':
        start()
except (EOFError, KeyboardInterrupt):
    print('\nBye Bye.....U can always come back again:)')
    print('See you next time')
