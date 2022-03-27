import random
def display_board(board):
    print('\n' * 100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ")


    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return(player1, player2)

#player1_marker, player2_marker = player_input()
#print(player1_marker, player2_marker)

def place_marker(board, marker, position):
    board[position] = marker

#place_marker(test_board, "$", 8)
#display_board(test_board)

def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


#if win_check(test_board, "X") == True:
    #print("You Win!")
def choose_first():
    player1 = "Player 1"
    player2 = "Player 2"
    player1_draw = random.randint(1, 10)
    if player1_draw % 2 == 0:
        return player1
    else:
        return player2

print(choose_first())

def space_check(board, position):
    return board[position] == " "



def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True



def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7 , 8, 9] or not space_check(board, position):
        position = int(input("Choose next position (1-9): "))
    return position



def replay():
    h = input("Would you like to play again? ").upper()
    if h == "YES":
        return True


print("Welcome to Tic Tac Toe!")

# while True:
while True:
    board = [" "] * 10
    p1, p2 = player_input()
    first = choose_first()
    print("It's ", first, "turn!")
    # Set the game up here
    # pass

    play_game = input("Would you like to play? (YES OR NO): ").upper()
    if play_game == "YES":
        game_on = True
    else:
        game_on = False


    # while game_on:
        # Player 1 Turn
    while game_on == True:
        if first == "Player 1":
            display_board(board)
            pos = player_choice(board)
            place_marker(board, p1, pos)
            if win_check(board, p1) == True:
                display_board(board)
                print("You Won!")
                game_on = False
            else:
                if full_board_check(board) == True:
                    display_board(board)
                    print("You drew! :(")
                    break
                else:
                    first = "Player 2"

        # Player2's turn.
        if first == "Player 2":
            display_board(board)
            pos = player_choice(board)
            place_marker(board, p2, pos)
            if win_check(board, p2) == True:
                display_board(board)
                print("You Won!")
                game_on = False
            else:
                if full_board_check(board) == True:
                    display_board(board)
                    print("You drew! :(")
                    break
                else:
                    first = "Player 1"

    if not replay():
        break
