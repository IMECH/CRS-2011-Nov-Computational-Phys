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
   data = readfile("percolation.data",3)
   OccuP = data[0]
   plotstr = ['.g', '.c', '.m', '.r', '.b']
   plotlab = ['size =  10 X 10', 'size =  25 X 25', 'size =  50 X 50', 'size =  75 X 75' , 'size = 100X100']
   for i in range(len(data)-1):
       plot(OccuP, data[i+1], plotstr[i]+'-', linewidth=2,markersize = 14, label = plotlab[i])
       plot(OccuP, data[i+1], '.k', markersize = 14)
       plot(OccuP, data[i+1], plotstr[i], markersize = 10)

   legend(loc =2)
   xlabel('p')
   ylabel('Percolation Probability', fontsize=13)
   title('Probability of Percolation', fontsize=13)
   grid()
   show()
