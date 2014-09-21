from pylab import *


def readfile(filename, blankline):
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
    n = 0
    data = []
    for line in file:
        n += 1 
        if n> blankline:
           m = 1
           for x in line.split():
               if len(data)<m:
                  data.append([])
               x = float(x)                  # make x an integer, rather than string
               data[m-1].append(x) 
               m = m + 1               

    return data

if __name__ == "__main__":
   data = readfile("funion50.time",3)
   
   OccuP = data[0]
   plot(OccuP, data[1], '.k', markersize = 15)
   plot(OccuP, data[1], '.r-', linewidth=1.5, markersize = 12, label='wave')
   plot(OccuP, data[2], '.k', markersize = 15)
   plot(OccuP, data[2], '.g-', linewidth=1.5, markersize = 12, label='recursive')
   plot(OccuP, data[3], '.k', markersize = 15)
   plot(OccuP, data[3], '.b-', linewidth=1.5, markersize = 12, label='hk')
   xlabel('p')
   ylabel('Running time (ms)', fontsize=13)
   legend(loc=2)
   show()
