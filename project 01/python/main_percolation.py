"""
main_percolation.py: main script to test percolation system

Zhou Lvwen, zhou.lv.wen@gmail.com
Physical Simulation: project 01
"""

from percolation_wave import *
from percolation_recursive import *
from percolation_hk import *
from sys import *
step = 0.01
trial_count = 20
size = 20

p = 0
print 'Running for size =', size
data = open("percolation.data", 'w')
data.write("--------size = %d--------\n" %size)
data.write("Occupation \t spanning\n")
data.write("probability \t probability\n")
while p < 1:
    stdout.write("-")
    stdout.flush()
    perc_count = 0
    for k in range(trial_count):
        g = random_grid(size, p, 2)
        #flow,perc = percolation_wave(g)
        #flow,perc = percolation_recursive(g)
        flow,perc = percolation_hk(g)
        if perc:
           perc_count += 1

    prob = float(perc_count)/trial_count
    data.write("%f\t %f\n" % (p, prob))       
    p += step
stdout.write(">|" + "\n")
data.close()
