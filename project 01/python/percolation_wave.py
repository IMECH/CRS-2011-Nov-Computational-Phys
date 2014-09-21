"""
Percolation_wave.py: Solve percolation using the idea of expanding wavefronts.
Based on http://secant.cs.purdue.edu/cs190c:project2\_09
         http://www.cnblogs.com/yuxc/category/296463.html

Zhou Lvwen, zhou.lv.wen@gmail.com
Physical Simulation: project 01
"""
from grid import *

def percolation_wave(input_grid, short=False):
    """
    Percolation algorithm by wave. Uses input_grid to determine where flow is
    allowed, trace to determine whether or not to visualize it graphically,
    and short to determine whether or not to exit early. Essentially, if your
    algorithm exits early, the code inside the 'if short' condition is what
    your code might look like.
    """
    flow_grid = grid(len(input_grid), -1)
    next_wave = []
    
    # Populate the inital wave from the top row
    for k in range(len(input_grid[0])):
        if input_grid[0][k] == 0:
            flow_grid[0][k] = 1
            next_wave.append((0,k))

    while next_wave:

        if short:
            row = len(flow_grid) - 1
            for k in range(len(flow_grid[0])):
                if flow_grid[row][k] != -1:
                    return flow_grid, True

        next_wave = gen_next_wave(input_grid, flow_grid, next_wave)

    # Check if we made it to the bottom
    row = len(flow_grid) - 1
    percolates = False
    for k in range(len(flow_grid[0])):
        if flow_grid[row][k] != -1:
            percolates = True

    return flow_grid, percolates

def gen_next_wave(input_grid, flow_grid, current):
    next = []

    for row, col in current:
        wave = flow_grid[row][col] + 1

        # Look down
        if row + 1 < len(input_grid):
            if input_grid[row+1][col] == 0 and flow_grid[row+1][col] == -1:
                flow_grid[row+1][col] = wave
                next.append((row+1, col))

        # Look right
        if col + 1 < len(input_grid[0]):
            if input_grid[row][col+1] == 0 and flow_grid[row][col+1] == -1:
                flow_grid[row][col+1] = wave
                next.append((row, col+1))

        # Look left
        if col - 1 >= 0:
            if input_grid[row][col-1] == 0 and flow_grid[row][col-1] == -1:
                flow_grid[row][col-1] = wave
                next.append((row, col-1))

        # Look up
        if row - 1 >= 0:
            if input_grid[row-1][col] == 0 and flow_grid[row-1][col] == -1:
                flow_grid[row-1][col] = wave
                next.append((row-1, col))

    return next
