#!/bin/python
### https://www.hackerrank.com/challenges/saveprincess2
### r and c is bot

def nextMove(n,r,c,grid):
    for col, row in enumerate(grid):
        if 'p' in row:
            her = (col, row.index('p'))
    if her[0] < r:
        return "UP"
    if her[0] > r:
        return "DOWN"
    if her[1] > c:
        return "RIGHT"
    if her[1] < c:
        return "LEFT"

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())
print nextMove(n,r,c,grid)
