#!/usr/bin/python3
# ICA 2
import random

# global vars
row = 5
column = 8
numberofplayers = 2
playerno = 1
track = []
game_run = True
playerlist = []
curr_post = 0
next_post = 0
movelist = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
curr_move = -1
player_score = [0, 0]
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
def getplayers(num=Redundant):
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


# randomly fill up board with gems and place marker at beginning
def board_items(track):

    Rubies = "R" * 7
    Emeralds = "E" * 7
    Diamonds = "D" * 7
    Sapphires = "S" * 7
    Glass_Beads = "G" * 11
    gems = Rubies + Emeralds + Diamonds + Sapphires + Glass_Beads
    for i in range(len(gems)):
        track.append(gems[i])
    random.shuffle(track)
    track.insert(0, "*")
    return track


def game_board(track=track, nrow=row, ncol=column):
    v = '|'
    h = "-"
    c = "+"  # corner character

    for row in range(nrow):
        outline = ""
        inside = ""
        for col in range(ncol):
            outline += c + h * 3
            inside += f"{v} {track[row * ncol + col]} "
        outline += c
        inside += v
        print(outline)
        print(inside)
    print(outline)

# move player position across board


def activemove(playerlist):
    flag = False
    while not flag:
        if playerno == 1:
            print("The available moves left are :", movelist)
            my_move = input(
                "\n" + playerlist[1] +
                " Please choose a number from the available move list displayed: ")
            try:
                curr_move = int(my_move)
                flag = playermovevalid(curr_move)
            except:
                print("Invalid choice - Please choose a move from: ", movelist)
        else:
            print("The available moves left are :", movelist)
            my_move = input(
                "\n" + playerlist[0] +
                " please choose a number from the available move list displayed: ")
            try:
                curr_move = int(my_move)
                flag = playermovevalid(curr_move)
            except:
                print("Invalid choice - Please choose a move from: ", movelist)

    return curr_move


# checks if move is available on the movelist or invalid entry
def playermovevalid(curr_move):

    if curr_move in movelist:
        movelist.remove(curr_move)
        print(movelist)
        return True
    else:
        print("This is not a valid move. Please choose a move from: ", movelist)
        return False


# update player position and gems collected
def update_vars(current_position, gem_collection):

    next_position = min(current_position + activeplayermove, len(track) - 1)
    track[current_position] = " "
    current_position += 1
    # print("update_vars(): ", activeplayermove, current_position, next_position)
    while current_position <= next_position:

        gem_collection[playerno].append(track[current_position])

        track[current_position] = " "
        current_position += 1
    track[next_position] = "*"
    # print(gem_collection)

    return " "

# condition for ending the game


def gameover(curr_post):
    if curr_post >= 39:
        return False
    return True


# determine winner
def final_scores(gem_collection, player_score):
    print(gem_collection)
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
        player_score[i] += rubies + emeralds + \
            diamonds + sapphires - glassbeads
        print(str(playerlist[i]) + "'s Score is " + str(player_score[i]))
    print("*" * 30 + "\n")
    if player_score[0] == player_score[1]:
        print("Draw")
    if player_score[0] > player_score[1]:
        print(playerlist[0], "Wins")
    else:
        print(playerlist[1], "Wins")


# main program #
print("""
                    +--+--+--+--+--+--+
                    | Sun Temple Game |
                    +--+--+--+--+--+--+
""")  # display the application name
if input("do you want to see the rules? (y/N) ").strip().lower() in ('y', 'yes'):
    print(RULES)
playerlist = getplayers(numberofplayers)
print("\n")
track = board_items(track)
game_board(track, row, column)

game_run = True
while game_run:

    # determine active player
    playerno = (playerno + 1) % 2
    print("\nIt is ", playerlist[playerno] + "'s turn \n")

    # now get a valid player move
    activeplayermove = activemove(playerlist)
    print("\nYou chose to move", activeplayermove, "Spaces")

    next_post = curr_post + activeplayermove

    variables = update_vars(curr_post, gem_collection)
    print(variables)

    game_board(track, row, column)

    print("\nPlayer Gems are: ", "\n", playerlist[0], gem_collection[0], "\n",
          playerlist[1], gem_collection[1])

    curr_post = next_post

    game_run = gameover(curr_post)

final_scores(gem_collection, player_score)
