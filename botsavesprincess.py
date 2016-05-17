#!/bin/python
## https://www.hackerrank.com/challenges/saveprincess
def displayPathtoPrincess(n,grid):
    for col, row in enumerate(grid):
        if 'p' in row:
            her = (col, row.index('p'))
        if 'm' in row:
            me = (col, row.index('m'))
    difrows = her[0] - me[0]
    difcols = her[1] - me[1]
    
    return ''.join([
            'UP\n' * abs(difrows) if difrows < 0 else 'DOWN\n' * difrows,
            'LEFT\n' * abs(difcols) if difcols < 0 else 'RIGHT\n' * difcols            
        ])
m = input()
grid = []
for i in xrange(0, m):
  grid.append(raw_input().strip())

print displayPathtoPrincess(m,grid)
