'''
Tic Tac Toe game basic version
'''

import random #implementing random function

def check_winner(b,mark):    #how to check a winner 
    win_set=[[0,1,2],[3,4,5],[6,7,8], #row wise
            [0,3,6],[1,4,7],[2,5,8],  #coloumn wise
            [0,4,8],[2,4,6]]          #digonal wise 
    for combo in win_set:
        if(b[combo[0]]==mark and b[combo[1]]==mark and b[combo[2]]==mark):
            return True
    return False
        
board=["-","-","-","-","-","-","-","-","-"] #board for blank spaces 
def board_display(b):          #design of the board
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print("---+---+---")
board_display(board)
# dividing in functions to make it better replacement of while true loop 

def user_turn(a):    #user turn function
    while True:
        move=int(input("Enter your move ::"))
        if(move<0 or move>8):
            print("Re-enter your move ::")
        elif(board[move]!="-"):
            print("space ocupied re-enter ::")
        else:
            board[move]="X"
            break


def comp_turn(c):   #computer turn function
    while True:
        empty_opt=[]
        print("the comp played :")
        for i in range(0,9):
            if(board[i]=="-"):
                empty_opt.append(i)
        if(len(empty_opt)>0):
            compMOVE=random.choice(empty_opt)
            board[compMOVE]="O"
            break

while True:       #main while loop for game 
    user_turn(board)
    board_display(board)
    if check_winner(board,"X")== True:  #to check user's win
        print("User won")
        break
    if "-" not in board:   #to check tie 
        print("Tie")
    comp_turn(board)
    board_display(board)
    if check_winner(board,"O")==True:  #to check computer'victory
        print("YOU lose")
        break




