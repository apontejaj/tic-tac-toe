board = [[0,0,0],[0,0,0],[0,0,0]]


def draw_board():
    print ("--1---2---3--")
    for x in range(0,3):
        line = str(x + 1)
        for y in range (0,3):
            line += " {} |".format(x_or_o(board[x][y]))
        print (line)
        print ("-------------")

def x_or_o(value):
    if value == 0:
        return " "
    elif value == 1:
        return "X"
    elif value == 2:
        return "O"

def is_there_winner():
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != 0:
            return True
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != 0:
            return True
    for x in range(0,3):
        if board[x][0] == board[x][1] == board[x][2]:
            if board[x][0] != 0:
                return True
        if board[0][x] == board[1][x] == board[2][x]:
            if board[0][x] != 0:
                return True

asking_user_name = lambda question: raw_input(question)

asking_play = lambda question: input(question)

valid_value = lambda num: num in range(0,3)

def playing():
    user_X = asking_user_name("What's the name of player X?")
    user_O = asking_user_name("What's the name of player O?")
    print ("Let's start")

    draw_board()
    player = 2
    count = 0
    while (not is_there_winner()) and (count < 9):
        if player == 1:
            player = 2
            name = user_O
        elif player == 2:
            player = 1
            name = user_X

        row = asking_play("{}, what's the row of your play?".format(name))-1
        column = asking_play("{}, what's the column of your play?".format(name))-1
        global board

        if valid_value(row) and valid_value(column):
            if is_empty(row, column):
                if player == 1:
                    board[row][column] = 1
                elif player == 2:
                    board[row][column] = 2
                count += 1
            else:
                print ("That espace has been taken. Play again somewhere else!")

            draw_board()
        else:
            print ("Remember that there is only three raws and three columns")

    winner(name)

def is_empty(row, column):
    return board[row][column] == 0

def winner(name):
    if is_there_winner():
        print ("{} WINS!".format(name))
    else:
        print ("Nobody wins")

playing()
