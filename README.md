# Sun Temple Game

## Introduction

Welcome to the Sun Temple Game! Your goal is to obtain the power of the sun by winning the game.

## Gameplay

- The game is for 2 players
- Players select their move from a list of available moves at the start of the game which are (0,1,1,2,2,3,3,4,4,5,5,6,6)
- Once a move (x) is selected, the player moves (x) spaces across the board and the move is removed from the list of available moves
- The board is filled with gems randomly placed across 39 spaces. There are 7 Rubies (R), 7 Emeralds (E), 7 Diamonds (D), 7 Sapphires (S) and 11 Glass Beads (G)
- As a player moves across the board, they collect gems from every space they move across, including the space where they end their moves on
- Upon completion of the game, points are awarded to players based on the number of gems they have collected, with each type of gem being tallied separately. The total number of points earned for a certain type of gem is calculated using the following formula: (n * (n + 1)) / 2, where n is the number of gems of that type collected.
- All gems have the same scoring system, and sum up to the final score. However, glass beads are counted as negative points.
- The game ends when a player reaches the final board space. The player with the most points is the winner.

## Installation

1. Download the `sun_temple.py` file
2. Install Python version 3.6 or later
3. In the command line, navigate to the directory where you downloaded the file and run `python sun_temple.py`

## Usage

1. Start the game by running `python sun_temple.py`
2. Follow the prompts to enter the names of the two players
3. Take turns selecting moves from the list of available moves
4. Collect gems as you move across the board
5. The game ends when a player reaches the final board space, and the player with the most points is declared the winner.

## Python version

This game requires Python version 3.6 or later to run.

## How to play

- After starting the game, it will prompt you to enter the name of the 2 players.
- Then it will show the board with randomly generated gems and the available moves left
- players will take turns to pick a move from available moves, and the game will display the updated board after each move.
- The game ends when a player reaches the final board space and the player with the most points is declared as the winner.

## Good luck and have fun!