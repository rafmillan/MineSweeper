import curses
import time
import sys
import random

def printBoard(A, stdscr, currRow, currCol):
	maxY, maxX = stdscr.getmaxyx()

	x = maxX//2 - len(A[0]) - len(A[0])//2
	y = maxY//2 - len(A)//2

	for i, row in enumerate(A):
		 for j, col in enumerate(row):
		 	if A[i][j] == '[1]':
		 		stdscr.attron(curses.color_pair(2))
		 	if A[i][j] == '[2]':
		 		stdscr.attron(curses.color_pair(3))
		 	if A[i][j] == '[3]':
		 		stdscr.attron(curses.color_pair(4))
		 	if A[i][j] == '[4]':
		 		stdscr.attron(curses.color_pair(5))
		 	if A[i][j] == '[5]':
		 		stdscr.attron(curses.color_pair(6))
		 	if A[i][j] == '[6]':
		 		stdscr.attron(curses.color_pair(7))
		 	if A[i][j] == '[7]':
		 		stdscr.attron(curses.color_pair(8))
		 	if A[i][j] == '[8]':
		 		stdscr.attron(curses.color_pair(9))
		 	if A[i][j] == '[X]':
		 		stdscr.attron(curses.color_pair(10))
		 	if currRow == i and currCol == j:
		 		stdscr.attron(curses.color_pair(1))

		 	stdscr.addstr(y+i, x+j*3, A[i][j])
		 	stdscr.attroff(curses.color_pair(1))
		 	stdscr.attroff(curses.color_pair(2))
		 	stdscr.attroff(curses.color_pair(3))
		 	stdscr.attroff(curses.color_pair(4))
		 	stdscr.attroff(curses.color_pair(5))
		 	stdscr.attroff(curses.color_pair(6))
		 	stdscr.attroff(curses.color_pair(7))
		 	stdscr.attroff(curses.color_pair(8))
		 	stdscr.attroff(curses.color_pair(9))
		 	stdscr.attroff(curses.color_pair(10))
	stdscr.refresh()
def printHiddenBoard(A, stdscr):
	maxY, maxX = stdscr.getmaxyx()

	x = 0
	y = maxY - len(A)

	for i, row in enumerate(A):
		 for j, col in enumerate(row):
		 	if A[i][j] == '[1]':
		 		stdscr.attron(curses.color_pair(2))
		 	if A[i][j] == '[2]':
		 		stdscr.attron(curses.color_pair(3))
		 	if A[i][j] == '[3]':
		 		stdscr.attron(curses.color_pair(4))
		 	if A[i][j] == '[4]':
		 		stdscr.attron(curses.color_pair(5))
		 	if A[i][j] == '[5]':
		 		stdscr.attron(curses.color_pair(6))
		 	if A[i][j] == '[6]':
		 		stdscr.attron(curses.color_pair(7))
		 	if A[i][j] == '[7]':
		 		stdscr.attron(curses.color_pair(8))
		 	if A[i][j] == '[8]':
		 		stdscr.attron(curses.color_pair(9))
		 	if A[i][j] == '[X]':
		 		stdscr.attron(curses.color_pair(10))
		 	stdscr.addstr(y+i, x+j*3, A[i][j])
		 	stdscr.attroff(curses.color_pair(2))
		 	stdscr.attroff(curses.color_pair(3))
		 	stdscr.attroff(curses.color_pair(4))
		 	stdscr.attroff(curses.color_pair(5))
		 	stdscr.attroff(curses.color_pair(6))
		 	stdscr.attroff(curses.color_pair(7))
		 	stdscr.attroff(curses.color_pair(8))
		 	stdscr.attroff(curses.color_pair(9))
		 	stdscr.attroff(curses.color_pair(10))

	stdscr.refresh()
def printArgs(stdscr):
	stdscr.addstr (0, 0, "Rows: %s" % (sys.argv[1]))
	stdscr.addstr (1, 0, "Columns: %s" % (sys.argv[2]))
	stdscr.addstr (2, 0, "Bombs: %s" % (sys.argv[3]))
	if len(sys.argv) == 5:
		stdscr.addstr (3, 0, "Seed: %s" % (sys.argv[4]))
def setCurses(stdscr):
	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(2, curses.COLOR_BLUE, 0)
	curses.init_pair(3, curses.COLOR_GREEN, 0)
	curses.init_pair(4, curses.COLOR_RED, 0)
	curses.init_pair(5, curses.COLOR_MAGENTA, 0)
	curses.init_pair(6, curses.COLOR_YELLOW, 0)
	curses.init_pair(7, curses.COLOR_CYAN, 0)
	curses.init_pair(8, curses.COLOR_BLACK, 0)
	curses.init_pair(9, curses.COLOR_WHITE, 0)
	curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_RED)
	stdscr.keypad(True)
def isMine(row, col, board):
	if board[row][col] == '[X]':
		return True
	else:
		return False
def placeBombs(board):
	row = random.randint(0, len(board)-1)
	col = random.randint(0, len(board[0])-1)

	currentRow = board[row]
	if not currentRow[col] == '[X]':

		currentRow[col] = '[X]'
	else:
		placeBombs(board)
def fillBoard(board):
	bombCount = 0
	for i, row in enumerate(board):
		for j, col in enumerate(row):
			if not board[i][j] == '[X]':
				#check 8 adjacent cells and count numbombs
				#North [i-1][j]
				if not i == 0:
					if isMine(i-1, j, board):
						bombCount += 1

				#North East [i-1][j+1]
				if not i == 0 and not j == len(board[i])-1:
					if isMine(i-1, j+1, board):
						bombCount += 1

				#East [i][j+1]
				if not j == len(board[i])-1:
					if isMine(i, j+1, board):
						bombCount += 1

				#South East [i+1][j+1]
				if not i == len(board)-1 and not j == len(board[i])-1:
					if isMine(i+1, j+1, board):
						bombCount += 1

				#South [i+1][j]
				if not i == len(board)-1:
					if isMine(i+1, j, board):
						bombCount += 1;

				#South West [i+1][j-1]
				if not i == len(board)-1 and not j == 0:
					if isMine(i+1, j-1, board):
						bombCount += 1

				#West [i][j-1]
				if not j == 0:
					if isMine(i, j-1, board):
						bombCount += 1

				#North West [i-1][j-1]
				if not i == 0 and not j == 0:
					if isMine(i-1, j-1, board):
						bombCount += 1
				str = "[%i]" % bombCount
				board[i][j] = str
				bombCount = 0
def checkBomb(board, myBoard, row, col):
	myBoard[row][col] = board[row][col]
	if isMine(row, col, board):
		return True;
	else: return False
def GameOver(stdscr):
	stdscr.erase()
	label  = ['GAME OVER.', 'press [Q] to quit...']
	maxY, maxX = stdscr.getmaxyx()

	for i, row in enumerate(label):
		x = maxX//2 - len(row)//2
		y = 1+i
		stdscr.addstr(y, x, row)



def main(stdscr):

	setCurses(stdscr)
	arguments = len(sys.argv) - 1

	rows = int(sys.argv[1])
	cols = int(sys.argv[2])
	numBombs = int(sys.argv[3])

	bombProb = numBombs/(rows*cols)
	stdscr.addstr(4,0,"bombProb: %.2f" % (bombProb))

	if len(sys.argv) == 5:
		seed = int(sys.argv[4])
	else:
		seed = 'none'
		random.seed()

	if numBombs > cols*rows:
		timer = 5
		while timer > 0:
			stdscr.addstr (0, 0, 'Cannot have more bombs than cells.... Try Again in %is' % (timer))
			stdscr.refresh()
			time.sleep(1)
			timer -= 1
		running = False

	board = [['[ ]' for x in range(cols)] for y in range(rows)]
	myBoard = [['[ ]' for x in range(cols)] for y in range(rows)]


	for n in range(0, numBombs):
		if seed == 'none':
			random.seed()
		else:
			random.seed(seed)
		placeBombs(board)

	fillBoard(board)

	currRow = 0
	currCol = 0
	currCell = myBoard[currRow][currCol]

	running = True
	gameOver = False
	while running:

		printArgs(stdscr)
		printBoard(myBoard, stdscr, currRow, currCol)
		printHiddenBoard(board, stdscr)

		key = stdscr.getch()

		if key == curses.KEY_UP and not gameOver:
			if currRow <= 0:
				currRow = currRow
			else: 
				currRow -= 1
			currCell = myBoard[currRow][currCol]
		elif key == curses.KEY_DOWN and not gameOver:
			if currRow >= rows-1:
				currRow = currRow
			else: 
				currRow += 1
			currCell = myBoard[currRow][currCol]
		elif key == curses.KEY_LEFT and not gameOver:
			if currCol <= 0:
				currCol = currCol
			else: 
				currCol -= 1
			currCell = myBoard[currRow][currCol]
		elif key == curses.KEY_RIGHT and not gameOver:
			if currCol >= cols-1:
				currCol = currCol
			else: 
				currCol += 1
			currCell = myBoard[currRow][currCol]
		elif key == ord('q') or key == ord('Q'):
			exit()
		elif key == ord('z') or key == ord('Z') and not gameOver:
			if checkBomb(board, myBoard, currRow, currCol):
				gameOver = True

		if gameOver:
			GameOver(stdscr)
			keyLock = True

		stdscr.refresh()

curses.wrapper(main)
