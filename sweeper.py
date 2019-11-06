import curses
import time
import sys

def updateMatrix(m):
    m[1][1] = m[1][1] * 2
    return m

def printBoard(A, stdscr, currRow, currCol):
	maxY, maxX = stdscr.getmaxyx()

	x = maxX//2 - len(A) - len(A)//2
	y = maxY//2 - len(A)//2

	for i, row in enumerate(A):
		 for j, col in enumerate(row):
		 	if currRow == i and currCol == j:
		 		stdscr.attron(curses.color_pair(1))

		 	stdscr.addstr(y+i, x+j*3, A[i][j])
		 	stdscr.attroff(curses.color_pair(1))
	stdscr.refresh()

def main(stdscr):
	running = True
	arguments = len(sys.argv) - 1

	cols = int(sys.argv[1])
	rows = int(sys.argv[2])
	numBombs = int(sys.argv[3])

	board = [['[ ]' for x in range(cols)] for y in range(rows)]
	if numBombs > cols*rows:
		timer = 5
		while timer > 0:
			stdscr.addstr (0, 0, 'Cannot have more bombs than cells.... Try Again in %is' % (timer))
			stdscr.refresh()
			time.sleep(1)
			timer -= 1

		running = False

	curses.curs_set(0)
	curses.noecho()
	curses.cbreak()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	#stdscr.attron(curses.color_pair(1))
	stdscr.keypad(True)

	currRow = 0
	currCol = 0
	currCell = board[currRow][currCol]
	while running:

		stdscr.addstr (0, 0, "Columns %i: %s" % (1, sys.argv[1]))
		stdscr.addstr (1, 0, "Rows %i: %s" % (2, sys.argv[2]))
		stdscr.addstr (2, 0, "Bombs %i: %s" % (2, sys.argv[2]))
		printBoard(board, stdscr, currRow, currCol)

		key = stdscr.getch()

		if key == curses.KEY_UP:
			if currRow <= 0:
				currRow = currRow
			else: 
				currRow -= 1
			currCell = board[currRow][currCol]
		elif key == curses.KEY_DOWN:
			if currRow >= rows-1:
				currRow = currRow
			else: 
				currRow += 1
			currCell = board[currRow][currCol]
		elif key == curses.KEY_LEFT:
			if currCol <= 0:
				currCol = currCol
			else: 
				currCol -= 1
			currCell = board[currRow][currCol]
		elif key == curses.KEY_RIGHT:
			if currCol >= cols-1:
				currCol = currCol
			else: 
				currCol += 1
			currCell = board[currRow][currCol]
		elif key == ord('q'):
			exit()

		stdscr.refresh()

curses.wrapper(main)
