
"""
Created on Wed Aug 10 13:34:21 2011

"""

from percolation_wave import *
from percolation_recursive import *
from percolation_hk import *
import time
import sys

step = 0.05
trial_count = 100000
size = 100


def test_time(func):
    p = 0
    results = []
    old_clock = time.clock()

    print 'testing', func, '...'

    while p < 1:

        perc_count = 0
        for k in range(trial_count):
            g = random_grid(size, p)
            flow,perc = func(g)
        new_clock = time.clock()
        results.append((new_clock - old_clock)*1000/trial_count)
        old_clock = new_clock
        p += step
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write(">|\n")
    return results

if __name__ == '__main__':
    
    sys.setrecursionlimit(250000)
    
    res1 = test_time(percolation_wave)
    res2 = test_time(percolation_recursive)
    res3 = test_time(percolation_hk)
    data = open("funion100.time", 'w')
    data.write("Occupation \t wave fun \t recursive fun \t\n")
    data.write("probability \t time use\t time use\t\n")
    for i in range(len(res1)):
        data.write(("\n"+"%f\t"*4) % (step*i, res1[i], res2[i], res3[i]))
    #endfor
    data.close()

