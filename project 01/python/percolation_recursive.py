"""
Percolation_recursive.py: Solve Cluster Spanning problem by Recursive Exploration of the Grid
Based on http://secant.cs.purdue.edu/cs190c:project2\_09
         http://www.cnblogs.com/yuxc/category/296463.html

Zhou Lvwen, zhou.lv.wen@gmail.com
Physical Simulation: project 01
"""
from grid import *

def percolation_recursive(input_grid, short=False):
    """
    Determine whether or not a grid percolates, and which cells are filled.
    Like before, short is True if you want the algorithm to stop immediately
    when it percolates, rather than exploring the entire grid.
    """
    size = len(input_grid)
    flow_grid = grid(size, -1)

    #start exploration from each space in top (zeroth) row
    for col in range(size):
        if explore(input_grid, flow_grid, 0, col, short):
            return flow_grid, True

    #check last (size-1'th) row for full spaces
    for col in range(size):
        if flow_grid[size-1][col] == '*':
            return flow_grid, True

    #no full spaces in bottom row; doesn't percolate
    return flow_grid, False

def explore(input_grid, flow_grid, row, col, short):
    """Explore the grid, marking unblocked cells as full as they are explored"""
    size = len(input_grid)
    if input_grid[row][col] == 0:
        flow_grid[row][col] = '*'

        #explore neighboring cells

        if short:
            if row + 1 == size:
                return True

        # Look down
        if row + 1 < size:
            if input_grid[row+1][col] == 0 and flow_grid[row+1][col] == -1:
               explore(input_grid, flow_grid, row+1, col, short)
        # Look right
        if col + 1 < size:
            if input_grid[row][col+1] == 0 and flow_grid[row][col+1] == -1:
               explore(input_grid, flow_grid, row, col+1, short)
        # Look left
        if col - 1 >= 0:
            if input_grid[row][col-1] == 0 and flow_grid[row][col-1] == -1:
               explore(input_grid, flow_grid, row, col-1, short)
        # Look up
        if row - 1 >= 0:
            if input_grid[row-1][col] == 0 and flow_grid[row-1][col] == -1:
               explore(input_grid, flow_grid, row-1, col, short)

       
