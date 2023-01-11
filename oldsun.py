# ICA 2
import random

# global vars
row = 5
column = 8
line = "|"
dots = "---"
cells = "." * 3
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


# print game rules
def rules():
    TEXT = (
        "\nRULES OF THE GAME \n" + "1) This is a two player game \n" +
        "2) Players select their move from a move list which allows them traverse 40 spaces on the board \n"
        + "3) The available moves are (0,1,1,2,2,3,3,4,4,5,5,6,6) \n" +
        "4) The board is filled with gems randomly placed across 39 spaces. There are 7 Rubies (R), 7 Emeralds (E), 7 Diamonds (D), 7 Sapphires (S), and 11 Glass Beads "
        "(G)\n" +
        "5) Once a move (x) is selected, the player moves (x) spaces across the board and the move is removed from the move list for the remainder of the game\n"
        +
        "6) As the player moves across the board, they collects gems from every space they move accross, including the space they end their move on.\n"
        +
        "7) When the game is finished, players calculate their scores as follows:\n - Firstly, count the number of gems each player has collected of each type\n"
        +
        " - Players gain points for collections of gems as follows: \n - 1 gem of one type = 1 point; \n - 2 gems of a type = 3 points [1 + 2]; \n"
        +
        " - 3 gems of a type = 6 points [3 + 3];\n - 4 gems of a type = 10 points [6 + 4] etc \n"
        +
        "All gems have the same scoring system, and sum up to the final score. However glassbeads are counted as negative points\n\n"
        +
        "For example if a player has 3 diamonds, 2 glass beads and 1 rubies, their diamonds are worth 6 points, their glassbeads are worth -3 points and their rubies are "
        "worth 1 point.\n Giving a total score of 4 points.\n" +
        "Glass beads are negative so they subtract from a players total score rather than add to it.\n"
        +
        "The game ends when a player reaches the final board space. The player with the most points is the winner.\n\n"
    )
    print(TEXT)


# store player names
def getplayers(num):
    playerlist = []
    playerlist.append(input("Enter your name Player 1: "))
    playerlist.append(input("Enter your name Player 2: "))
    return playerlist


# randomly fill up board with gems and place marker at beginning
def board_items(track):
    gems = "RRRRRRREEEEEEEDDDDDDDSSSSSSSGGGGGGGGGGG"
    print("gems:", len(gems))
    for i in range(len(gems)):
        track.append(gems[i])
    random.shuffle(track)
    track.insert(0, "*")
    return track


# draw board
def game_board(board, nrow, ncolumn):
    for row in range(nrow):
        outline = ""
        inside = ""
        for col in range(ncolumn):
            outline = outline + line + dots
            cells = row * column + col
            inside = inside + line + " " + track[cells] + " "
        outline += line
        inside += line
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
def update_vars(curr_post, gem_collection):

    next_post = min(curr_post + activeplayermove, len(track) - 1)
    track[curr_post] = " "
    curr_post += 1
    # print("update_vars(): ", activeplayermove, curr_post, next_post)
    while curr_post <= next_post:

        gem_collection[playerno].append(track[curr_post])

        track[curr_post] = " "
        curr_post += 1
    track[next_post] = "*"
    # print(gem_collection)

    return " "


# condition for ending the game
def gameover(curr_post):
    if curr_post >= 39:
        return False
    else:
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
print("Sun Temple Game")  # display the application name
print("********************************")
rules()
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
