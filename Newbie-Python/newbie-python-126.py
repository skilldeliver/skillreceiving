from os import system
from os import name as sys_name
from time import sleep
from random import choice


try:
    from termcolor import colored
except ImportError:
    def colored(x):
        return x


class Move(object):
	def __init__(self, score, index):
		self.score = score
		self.index = index


def init_board():
	return [' ' for i in range(9)]


def init_mode():
	print(' Choose game mode:', ' 1 - PvP', ' 2 - PvC', ' 3 - CvC', sep='\n')
	return get_input(' Enter desired mode: ', 3)


def get_input(prompt=' Input integer: ', max_limit=0, exception_cmd='pass'):
	"""Getting input from user. Function checks it to be integer in
	specified range"""
	while True:
		try:
			value = int(input(prompt))
			if 0 < value <= max_limit:
				return value
			else:
				raise ValueError
		except ValueError:
			exec(exception_cmd)


def draw_board(board):
	print(' ╔═══╦═══╦═══╗\n\
 ║ {6} ║ {7} ║ {8} ║\n\
 ╠═══╬═══╬═══╣\n\
 ║ {3} ║ {4} ║ {5} ║\n\
 ╠═══╬═══╬═══╣\n\
 ║ {0} ║ {1} ║ {2} ║\n\
 ╚═══╩═══╩═══╝ '.format(*board))


def player_move(board):
	while True:
		player_move = get_input(' Input your move: ', 9,
                          'print(" Invalid move")') - 1
		if is_free(player_move, board):
			return player_move
		else:
			print(" Space is not free")


def is_free(move, board):
	return board[move] == ' '


def change_sign(sign):
	return 'x' if sign == 'o' else 'o'


def change_player(player):
	if mode == 1:
		return ' PLAYER X' if player == ' PLAYER O' else ' PLAYER O'
	elif mode == 2:
		return ' PLAYER X' if player == ' AI O' else ' AI O'
	else:
		return ' AI X' if player == ' AI O' else ' AI O'


def empty_indices(board):
	return [i for i in range(len(board)) if board[i] == ' ']


def win_check(sign, board):
	"""This function checks for a winner. Returns information needed to
	'win_light' function (next one)."""

	# Horizontal win check
	for i in range(0, 7, 3):
		if sign \
		   == board[i] \
		   == board[i + 1] \
		   == board[i + 2]:
			return 'h', i

	# Vertical win check
	for i in range(3):
		if sign \
		   == board[i] \
		   == board[i + 3] \
		   == board[i + 6]:
			return 'v', i

	# / diagonal win check
	if sign \
	   == board[0] \
	   == board[4] \
	   == board[8]:
		return 'dl', None

	# \ diagonal win check
	elif sign \
		== board[2] \
		== board[4] \
			== board[6]:
		return 'dr', None

	return False


def win_light(key, i, sign):
	"""Substitutes win combination with red symbols"""
	global light_board
	light_board = real_board.copy()
	color = colored(sign, 'red')
	if key == 'h':
		light_board[i] = color
		light_board[i + 1] = color
		light_board[i + 2] = color
	elif key == 'v':
		light_board[i] = color
		light_board[i + 3] = color
		light_board[i + 6] = color
	elif key == 'dl':
		light_board[0] = color
		light_board[4] = color
		light_board[8] = color
	elif key == 'dr':
		light_board[2] = color
		light_board[4] = color
		light_board[6] = color


def draw_win_board(player):
	try:
		brd = light_board
		while True:
			clear()
			print(player, 'WINS!')
			draw_board(brd)
			print(' Press *Ctrl-c* to proceed')
			brd = real_board if brd == light_board else light_board
			sleep(0.15)
	except KeyboardInterrupt:
		pass


def minimax(sign, board, is_max_sign=True, depth=0):
	"""Return a best move for a sign in a board."""
	depth += 1
	new_board = board.copy()
	empty_spots = empty_indices(new_board)
	if is_max_sign:
		max_sign = sign
		min_sign = change_sign(sign)
	else:
		max_sign = change_sign(sign)
		min_sign = sign

	# Check for base case
	if win_check(max_sign, new_board):
		score = Move(100 - depth, None)
		return score
	elif win_check(min_sign, new_board):
		score = Move(depth - 100, None)
		return score
	elif len(empty_spots) == 0:
		score = Move(0, None)
		return score

	moves = []
	for i in empty_spots:
		move = Move(None, i)
		new_board[i] = sign
		if is_max_sign:
			result = minimax(min_sign, new_board, False, depth)
		else:
			result = minimax(max_sign, new_board, True, depth)
		move.score = result.score
		new_board[i] = ' '   # Revert changes made to board
		moves.append(move)

	if is_max_sign:
		best_score = -1000
		for i in range(len(moves)):
			if moves[i].score > best_score:
				best_move = i
				best_score = moves[i].score
	else:
		best_score = 1000
		for i in range(len(moves)):
			if moves[i].score < best_score:
				best_move = i
				best_score = moves[i].score

	return moves[best_move]   # Return index of best move for passed board


# Clear screen procedure depends on OS type
if sys_name == 'posix':
	def clear():
		system('clear')
elif sys_name == 'nt':
	def clear():
		system('cls')

# START MESSAGE
clear()
print(' Welcome to the TicTacToe!')
draw_board([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(' To win, you have to place 3 "x" or "o" in a row.\n',
	  'To make a move, you have to enter a corresponding',
	  'number on your NumPad.\n',
	  'If you are still confused, look at the key map above.\n\n',
	  'Press any key to proceed...')
input()

# START
clear()
mode = init_mode()
while True:
	clear()
	real_board = init_board()
	clear()
	if mode == 1:
		current_player = ' PLAYER X'
		current_sign = 'x'
		while True:
			print(current_player)
			draw_board(real_board)
			move = player_move(real_board)
			real_board[move] = current_sign
			win = win_check(current_sign, real_board)
			if win:
				win_light(*win, current_sign)
				draw_win_board(current_player)
				break
			elif not empty_indices(real_board):
				clear()
				print(' IT IS A DRAW!')
				draw_board(real_board)
				break
			else:
				clear()
				current_sign = change_sign(current_sign)

	if mode == 2:
		current_player = choice([' AI O', ' PLAYER X'])
		current_sign = 'o' if current_player == ' AI O' else 'x'
		first_move = True if current_sign == 'o' else False
		while True:
			clear()
			print(current_player)
			draw_board(real_board)
			if current_sign == 'x':
				move = player_move(real_board)
			elif first_move:
				move = choice(range(1, 9))
				first_move = False
			else:
				move = minimax(current_sign, real_board, True).index
			real_board[move] = current_sign
			win = win_check(current_sign, real_board)
			if win:
				clear()
				win_light(*win, current_sign)
				draw_win_board(current_player)
				break
			elif not empty_indices(real_board):
				clear()
				print(' IT IS A DRAW!')
				draw_board(real_board)
				break
			current_sign = change_sign(current_sign)
			current_player = change_player(current_player)

	if mode == 3:
		current_player = ' AI X'
		current_sign = 'x'
		first_move = True
		print(current_player)
		draw_board(real_board)
		input(' Press any key...')
		while True:
			if first_move:
				move = choice(range(1, 9))
				first_move = False
			else:
				move = minimax(current_sign, real_board, True).index
			real_board[move] = current_sign
			win = win_check(current_sign, real_board)
			if win:
				clear()
				win_light(*win, current_sign)
				draw_win_board(current_player)
				break
			elif not empty_indices(real_board):
				clear()
				print(' IT IS A DRAW!')
				draw_board(real_board)
				break
			current_player = change_player(current_player)
			clear()
			print(current_player)
			draw_board(real_board)
			input(' Press any key...')
			current_sign = change_sign(current_sign)

	play_wish = input(' Do you want to play again? [Y/n]: ')
	if not (play_wish.lower() in ['y', 'yes', '']):
		break
