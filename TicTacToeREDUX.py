import random

def choose_first():
    if random.randint(1,2) == 1:
    	return 'Player 1'
    else:
    	return 'Player 2'

def display_board(board):
	print("1-3", end=" ")
	print(board[1]+"|"+board[2]+"|"+board[3])
	print("4-6", end =" ")
	print(board[4]+"|"+board[5]+"|"+board[6])
	print("7-9", end =" ")
	print(board[7]+"|"+board[8]+"|"+board[9])

def player_input():
	marker = ''
	while not (marker=='X' or marker=='O'):
		marker = input("Player 1: Do you want to be X or O? ").upper()
	if marker == "X":
		return ("X","O")
	else:
		return ("O","X")

def player_choice(board):
	pos=0
	while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board, pos):
		pos = int(input("Please enter a numerical value from 1-9 for where you want your marker to be placed: "))
	return pos

def place_marker(board, marker, position):
    return board[position]=marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, len(board)):
        if space_check(board,i):
            return False
    return True

def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

print('Welcome to Tic Tac Toe!')
game_on=True
while True:
	game_board = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + " will go first.")
	while game_on==True:
		if turn == 'Player 1':
			display_board(game_board)
			pos = player_choice(game_board)
			place_marker(game_board,player1_marker, pos)

			if win_check(game_board, player1_marker):
				display_board(game_board)
				print("Congratulations! You won!")
				game_on=False
			else:
				if full_board_check(game_board):
					display_board(game_board)
					print("The game is a draw!")
					break
				else:
					turn = 'Player 2'
					continue
		else:
			display_board(game_board)
			pos = player_choice(game_board)
			place_marker(game_board,player2_marker, pos)

			if win_check(game_board, player2_marker):
				display_board(game_board)
				print("Congratulations! You won!")
				game_on=False
			else:
				if full_board_check(game_board):
					display_board(game_board)
					print("The game is a draw!")
					break
				else:
					turn = 'Player 1'
					continue
	if not replay():
		break
print("Thank you for playing!")