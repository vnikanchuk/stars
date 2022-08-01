#!/usr/bin/env python3
# encoding: utf-8

from time import sleep, time
from random import randrange, randint
import math
import curses
from curses import wrapper


def check(data, nmin, nmax):
	variant = 1
	if variant == 1:
		n, dn = data
		if n >= nmax:
			n = nmax
			dn = -dn
		elif n < nmin:
			n = nmin
			dn = -dn
		if abs(dn) > 5:
			dn = dn / abs(dn)

	elif variant == 2:
		n, dn = data
		if n > nmax:
			n -= nmax
		elif n < nmin:
			n += nmax

	n = nmin if n < 0 else nmax if n > nmax else n
	return n, dn


def main(stdscr):
	X_MAX = 159
	Y_MAX = 48
	spaces = 125

	curses.initscr()
	stdscr.clear()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
	
	def prog(x, sx, y, sy, sym1, sym2):
		if x > X_MAX or sx > X_MAX or y > Y_MAX or sy > Y_MAX: return
		stdscr.addch(sy, sx, sym2)
		stdscr.addch(y, x, sym1)

	def check2(x, dx, y, dy):
		x, dx = check([x, dx], 0, X_MAX)
		y, dy = check([y, dy], 0, Y_MAX)
		return x, dx, y, dy

	def slsym(c):
		a = randint(0, X_MAX)
		b = randint(0, Y_MAX)
		d = randint(1, 7)
		stdscr.addstr(b, a, chr(c), curses.color_pair(d))

	def rr(): return (randint(1, 99) - 50) / 100000. if randint(1, 10000) < 10 else 0

	curses.curs_set(0)
	z = 10
	dz = 10

	x = []
	y = []
	dx = []
	dy = []
	sx = []
	sy = []

	for i in range(z):
		x.append(0)
		y.append(0)
		dx.append(0)
		dy.append(0)
		sx.append(0)
		sy.append(0)

	for i in range(z):
		x[i] = randrange(0,X_MAX)
		y[i] = randrange(0,Y_MAX)
		dx[i] = randrange(-1000, 1090) / 1000.
		dy[i] = randrange(-1000, 1100) / 1000.
		sx[i] = x[i]
		sy[i] = y[i]

	while True:
		sleep(math.log(z) / (z * dz))

		for i in range(z):
			if True : #randrange(1,1000) < 400:
				x[i] += dx[i]
				dx[i] += rr()
				y[i] += dy[i]
				dy[i] += rr()
				x[i], dx[i], y[i], dy[i] = check2(x[i], dx[i], y[i], dy[i])
				e = randrange(0, 47)
				prog(int(x[i]), int(sx[i]), int(y[i]), int(sy[i]), 'o', '.')


				for var_i in range(randint(1, spaces)): slsym(32)

				slsym(randint(33,127))

				sx[i] = x[i]
				sy[i] = y[i]

		stdscr.refresh()


wrapper(main)
