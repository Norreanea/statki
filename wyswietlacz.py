#!/usr/bin/python3

import sys
import time
global plansza
plansza = []



for line in sys.stdin:
  punkty=line

print(punkty)

for x in range(0,11):
    plansza.append(["o"] * 11)

def print_board(plansza):
    for row in plansza:
        str(row)
        print (" ".join(row))

def make_board():
  g=3
  k=5
  for x in range(0,11):
    for y in range(0,11):
      plansza[0][x]=x
      plansza[x][0]=x
      plansza[0][x]=str(plansza[0][x])
      plansza[x][0]=str(plansza[x][0])

  for x in range(0,10):
    l=[]
    l.append(plansza[x][0])
    l.append(" ")
    plansza[x][0]=''.join(l)

  for i in range(0,20):
    a=punkty[g][0][0]
    b=punkty[k][0][0]
    c=int(a)
    d=int(b)
    plansza[c][d]="X"
    g+=9
    k+=9

make_board()
print("Oto plansza:\n")
print_board(plansza)
