import curses
import time
import sys

def updateMatrix(m):
    m[1][1] = m[1][1] * 2
    return m

def printBoard(A, stdscr):
	maxY, maxX = stdscr.getmaxyx()

	x = maxX//2 - len(A) - len(A)//2
	y = maxY//2 - len(A)//2

	for row in A:
		stdscr.addstr(y, x, '\n'.join([''.join(['{:3}'.format(item) for item in row])]))
		y += 1
		

    	

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

	curses.curs_set(2)
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

	while running:
		stdscr.addstr (0, 0, "Columns %i: %s" % (1, sys.argv[1]))
		stdscr.addstr (1, 0, "Rows %i: %s" % (2, sys.argv[2]))
		stdscr.addstr (2, 0, "Bombs %i: %s" % (2, sys.argv[2]))

		printBoard(board, stdscr)
		stdscr.refresh()

	running = False

curses.wrapper(main)
