#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdout
from time import sleep, time
from random import randrange
import math



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

  return n, dn



def output (cx, cy, cs):
  stdout.write('\033[' + str(cy) + ';' + str(cx) + 'H' + cs)



def main():

  def prog(x, sx, y, sy, sym1, sym2):
    #output(x, y, sym1)
    output(sx, sy, sym2)
    output(x, y, sym1)
  
  def check2(x, dx, y, dy):
    x, dx = check([x, dx], 1, 160)
    y, dy = check([y, dy], 1, 50)
    return x, dx, y, dy
    
  def slsym(c):
    a = randrange(1, 161)
    b = randrange(1, 50)
    d = randrange(31, 37)
    stdout.write('\033[01;' + str(d) + 'm')
    output(a, b, chr(c))

  def rr():
    if randrange(1, 10000) < 10:
        return (randrange(1, 99) - 50) / 100000.
    else:
        return 0

  stdout.write('\033[?25l')
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
    x[i] = randrange(0,160)
    y[i] = randrange(0,60)
    dx[i] = randrange(-1000, 1090) / 1000.
    dy[i] = randrange(-1000, 1100) / 1000.
    sx[i] = x[i]
    sy[i] = y[i]

  while 1:

    sleep(math.log(z) / (z * dz))

    for i in range(z):
      if 1 == 1: #randrange(1,1000) < 400:
        x[i] += dx[i]
        dx[i] += rr()
        y[i] += dy[i]
        dy[i] += rr()
        x[i], dx[i], y[i], dy[i] = check2(x[i], dx[i], y[i], dy[i])
        e = randrange(0, 47)
        #ss = randrange(32,5000)
        #if ss > 127:
        #  ss = 32
        prog(int(x[i]), int(sx[i]), int(y[i]), int(sy[i]), '\033[01;0mo', '\033[01;0m.')

        for j in range(randrange(1, 50)):
          slsym(32)
        for j in range(randrange(0, 2)):
          slsym(randrange(32,127))

        sx[i] = x[i]
        sy[i] = y[i]

    stdout.flush()
    
if __name__ == '__main__':
  try:
    main()
  except:
    stdout.write('\033[?25h')
    print ''
    raise
