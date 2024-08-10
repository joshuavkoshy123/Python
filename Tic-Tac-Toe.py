# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:21:57 2024

@author: justi
"""

from random import randrange

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
playing = True

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+\n"
            "|       |       |       |\n"
            "|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |\n"
            "|       |       |       |\n"
            "+-------+-------+-------+\n"
            "|       |       |       |\n"
            "|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |\n"
            "|       |       |       |\n"
            "+-------+-------+-------+\n"
            "|       |       |       |\n"
            "|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |\n"
            "|       |       |       |\n"
            "+-------+-------+-------+\n")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    move = input("Enter a move: ")
    while(int(move) not in range(1, 10) and move not in board):
        move = input("Enter a valid move: ")
        
    for row, col in make_list_of_free_fields(board):
        if(board[row][col] == move):
            board[row][col] = 'O'
            
    display_board(board)
    victory_for(board, 'O')


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    free_spots = []
    
    for row in range(3):
        for col in range(3):
            if(board[row][col] != 'X' and board[row][col] != 'O'):
                free_spots.append((row, col))
                
    return free_spots


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    global playing
    for row in range(3):
        if(board[row][0] == sign and board[row][1] == sign and board[row][2] == sign):
            if(sign == 'X'):
                print("The computer won :(")
            else:
                print("You won!!!")
            replay = input("Would you like to play again? (Yes or No): ")
            if(replay == "No"):
                playing = False
            else:
                reset_board(board)
                display_board(board)
                
    for col in range(3):
        if(board[0][col] == sign and board[1][col] == sign and board[2][col] == sign):
            if(sign == 'X'):
                print("The computer won :(")
            else:
                print("You won!!!")
            replay = input("Would you like to play again? (Yes or No): ")
            if(replay == "No"):
                playing = False
            else:
                reset_board(board)
                display_board(board)
                
    if (board[0][0] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[2][0] == 'X'):
        print("The computer won :(")
        replay = input("Would you like to play again? (Yes or No): ")
        if(replay == "No"):
            playing = False
        else:
            reset_board(board)
            display_board(board)
        

def draw_move(board):
    # The function draws the computer's move and updates the board.
    board_coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    while(True):
        computer_move = randrange(8) + 1
        pair = board_coordinates[computer_move-1]
        if(str(computer_move) == board[pair[0]][pair[1]]):
            break
        print(computer_move)
        
    for row, col in make_list_of_free_fields(board):
        if(board[row][col] == str(computer_move)):
            print(board[row][col])
            board[row][col] = 'X'
            
    display_board(board)
    victory_for(board, 'X')
    
def reset_board(board):
    board[0][0] = '1'
    board[0][1] = '2'
    board[0][2] = '3'
    board[1][0] = '4'
    board[1][1] = 'X'
    board[1][2] = '6'
    board[2][0] = '7'
    board[2][1] = '8'
    board[2][2] = '9'

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
 
 
print(fun(0, 3))
display_board(board)
while(playing):
    enter_move(board)
    draw_move(board)
    