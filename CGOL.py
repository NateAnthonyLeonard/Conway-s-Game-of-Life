#!/usr/bin/env 
#(c)

import time
import os
from copy import deepcopy

ROWS = 10
COLUMNS = 10
ALIVE = chr(0x2588)
DEAD = 0

def make_grid():
    grid = []
    for n in range(ROWS):
        rgrid = []
        for i in range(COLUMNS):
            rgrid.append(DEAD)
        grid.append(rgrid)
    return grid

def space(grid):
    for row in grid:
        s_row = map(str, row)
        print (" ".join(s_row))

#various patterns to place on the grid
def place_stillife(grid):
    grid[7][7] = ALIVE
    grid[6][7] = ALIVE
    grid[6][6] = ALIVE
    grid[7][6] = ALIVE

def place_stilldisrupt(grid):
    grid[6][6] = ALIVE
    grid[5][6] = ALIVE
    grid[5][5] = ALIVE
    grid[6][5] = ALIVE

    
def place_nxtstill(grid):
    grid[9][9] = ALIVE
    grid[8][9] = ALIVE
    grid[8][8] = ALIVE
    grid[9][8] = ALIVE

    
def place_oscill(grid):
    grid[3][2] = ALIVE
    grid[3][3] = ALIVE
    grid[3][4] = ALIVE



#Purpose is to accurately check for alive cells
def get_n(grid, row, col):
    total = 0
    # check top left
    if (row>=1) and (col>=1) and (grid[row-1][col-1] == ALIVE):
        total += 1

    # check top
    if (row>=1) and (grid[row-1][col] == ALIVE):
        total += 1

    # check top right
    if (row>=1) and (col<COLUMNS-1) and (grid[row-1][col+1] == ALIVE):
       total += 1

    # check left
    if (col>=1) and (grid[row][col-1] == ALIVE):
        total += 1

    # check right
    if (col<COLUMNS-1) and (grid[row][col+1] == ALIVE):
        total += 1

    # check bottom left
    if (row < ROWS-1) and (col>=1) and (grid[row+1][col-1] == ALIVE):
        total += 1

    # check bottom
    if (row<ROWS-1) and (grid[row+1][col] == ALIVE):
        total += 1

    # check bottom right
    if (row < ROWS-1) and (col<COLUMNS-1) and (grid[row+1][col+1] == ALIVE):
        total += 1

    return total

#Evolve patterns across grid or as they interact
def evolve(grid):
    gcopy = deepcopy(grid)
    for row in range(ROWS):
        for col in range(COLUMNS):
            
            cell = gcopy[row][col]
            total = get_n(gcopy, row, col)
            
            #check cell overall(condition 4)
            if ((total == 2) or (total == 3)) and cell == ALIVE:
                grid[row][col] = ALIVE # cell is alive
            elif ((total == 3) and cell == DEAD):
                grid[row][col] = ALIVE
            else:
                grid[row][col] = DEAD

          
def main():
    choice = input("Choose game_demo or pattern_example:")
    if choice == str("game_demo") or choice == str("game demo") or choice == str("demo") or choice == str("game"):
        grid = make_grid()
        place_stilldisrupt(grid)
        place_oscill(grid)
        for n in range(12):
            os.system("clear")
            print('\n'*50)
            space(grid)
            evolve(grid)
            time.sleep(0.5)
    elif choice == str("pattern_example") or choice == str("pattern example") or choice == str("pattern") or choice == str("example"):
        grid = make_grid()
        place_stillife(grid)
        place_oscill(grid)
        place_nxtstill(grid)
        for n in range(100):
            os.system("clear")
            print('\n'*50)
            space(grid)
            evolve(grid)
            time.sleep(0.5)
    else:
        print("Invalid input! Can't run!")

if __name__ == '__main__':
    main()
    
