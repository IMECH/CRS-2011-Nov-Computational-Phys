

def grid(size, fill=0):
    """
    Make a grid with 'size' rows and 'size' columns, with each space filled by 
    'fill'.

    >>> grid(3, 1)
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> grid(2, '*')
    [['*', '*'], ['*', '*']]
    """
    grid = []

    for i in range(size):
        row = [fill]*size               # row is a list with size copies of fill
        grid.append(row)

    return grid

def printgrid(grid):
    """
    Print out the grid represented in 'grid'.

    >>> printgrid([[1,0,1],[0,1,1],[0,0,1]])
     1  0  1
     0  1  1
     0  0  1
    >>> 
    """
    for row in grid:
        for space in row:
            print '%02s' % (space,),
        print

def readgrid(filename):
    """
    Reads the grid from the file.  The format is one row per line, each column
    separated by whitespace.

    >>> f = open('readgrid.test', 'w')
    >>> print >>f, '0 1 0\\n1 0 1\\n1 1 0\\n'
    >>> f.close()
    >>> readgrid('readgrid.test')
    [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
    """
    file = open(filename)
    grid = []

    for line in file:
        row = []
        for x in line.split():
            x = int(x)                  # make x an integer, rather than string
            row.append(x)                

        if row != []:                   # filter out empty lines
            grid.append(row)

    return grid

def visualize(flow_grid, input_grid):
    """
    Visualize the flow in flow_grid on input_grid with VPython, using gray 
    squares for blocked spaces (input_grid[i][j] = 1) and blue squares for
    spaces with flow (flow_grid[i][j] = '*').

    All objects in the scene will be removed prior to drawing.  The active 
    scene will be used.

    >>> visualize([['*','*',1],['*',1,1],['*',1,1]], [[0,0,1],[0,1,1],[0,0,1]])
    """
    from visual import box, display

    blue = (0, 0, 1)
    gray = (.5, .5, .5)
    black = (0.3, 0.3, 0.3)

    size = len(input_grid)
    total_size = size * size
    disp = display.get_selected()       # gets the active display
    if disp is None:                    # no display, so create one
        display(title="Percolation", autocenter=True)
    else:                               # display exists, empty it
        disp.autocenter = True          # autocenter for convenience
        # We only need to delete these boxes if there is a mismatch in the
        # number of boxes versus the number of grid cells. We assume that no
        # other objects are on the scene.
        if total_size != len(disp.objects):
            for object in disp.objects:
                object.visible = False  # make all objects in display invisible

    # redraw all of the grid, because of the size mismatch
    if total_size != len(disp.objects):
        for row in range(size):
            for col in range(size):
                # for blocked spaces, draw a gray box
                if input_grid[row][col]==1:
                    box(pos=(col, -row, 0), color=gray)
                # for spaces with flow, draw a blue box
                elif flow_grid[row][col]!=-1:
                    box(pos=(col, -row, 0), color=blue)
                else:
                    box(pos=(col, -row, 0), color=black)
    # or just change the colors, based on the grids given
    else:
        for object in disp.objects:
            x, y, _ = object.pos
            x, y = int(x), int(y)
            if flow_grid[-y][x] != -1:
                object.color = blue
            elif input_grid[-y][x] == 1:
                object.color = gray
            else:
                object.color = black

def random_grid(size, p, typerand = 1):
    """
    Generates a grid with 'size' rows and 'size' columns. Each grid space is 
    randomly filled with a zero with probability p or a one with probability
    (1-p).
    
    >>> random_grid(3, 1)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> random_grid(3, 0)
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    """
    from random import uniform

    g = grid(size, 1)
    
    if typerand == 1:
       for row in range(size):
           for col in range(size):
               if uniform(0,1) < p:        # true with probability p
                   g[row][col] = 0
    else:
       N = size*size
       order = [ 0 for i in range(N) ]
       for i in range(N):
           order[i] = i
       for i in range(N):
           j = int(i + (N - i) * uniform(0,1))
           temp = order[i]
           order[i] = order[j]
           order[j] = temp
       for i in range(int(round(N*p))):
           col = order[i]/size
           row = order[i]%size
           g[row][col] = 0

    return g


if __name__ == "__main__":
    import doctest
    doctest.testmod()

