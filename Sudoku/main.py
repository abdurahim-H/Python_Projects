import random

def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - - ")

		for j in range(len(board[i])):
			if j % 3 == 0 and j != 0:
				print("|", end=" ")

			if board[i][j] == 0:
				print("x", end=" ")
			else:
				print(str(board[i][j]), end=" ")

			if j == 8:
				print()


def is_valid(board, row, col, num):
	# Check row
	for i in range(9):
		if board[row][i] == num:
			return False

	# Check column
	for i in range(9):
		if board[i][col] == num:
			return False

	# Check 3x3 grid
	start_row, start_col = 3 * (row // 3), 3 * (col // 3)
	for i in range(start_row, start_row + 3):
		for j in range(start_col, start_col + 3):
			if board[i][j] == num:
				return False

	return True


def find_empty_location(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return i, j
	return None


def solve_sudoku(board):
	empty_location = find_empty_location(board)
	if not empty_location:
		return True

	row, col = empty_location
	for num in range(1, 10):
		if is_valid(board, row, col, num):
			board[row][col] = num

			if solve_sudoku(board):
				return True

			board[row][col] = 0

	return False


def create_empty_board():
	return [[0 for _ in range(9)] for _ in range(9)]


def start_game():
	# Generate a complete Sudoku board
	board = create_empty_board()
	solve_sudoku(board)

	# Create the puzzle by replacing some numbers with 'X'
	for _ in range(40):  # Change this number to adjust the difficulty of the puzzle
		row = random.randint(0, 8)
		col = random.randint(0, 8)
		while board[row][col] == 'X':
			row = random.randint(0, 8)
			col = random.randint(0, 8)
		board[row][col] = 'X'

	print("Welcome to Sudoku!")
	print_board(board)

	while True:
		row = int(input("Enter row (1-9, or 0 to exit): ")) - 1
		if row == -1:
			print("Exiting game...")
			break

		col = int(input("Enter column (1-9): ")) - 1
		num = int(input("Enter number (1-9): "))

		if board[row][col] == 'X' and is_valid(board, row, col, num):
			board[row][col] = num
			print_board(board)

			if not any('X' in row for row in board):
				print("Congratulations! You've solved the Sudoku!")
				break
		else:
			print("Invalid move. Try again.")

start_game()