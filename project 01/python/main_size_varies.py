"""
main_size_varies.py: main script to test different size systems

Zhou Lvwen, zhou.lv.wen@gmail.com
Physical Simulation: project 01
"""
from percolation_wave import *
from percolation_recursive import *
from percolation_hk import *
from sys import *
step = 0.01
trial_count = 1000000
sizes = [10, 25, 50, 75, 100]

n = 0
results=[]
P = []
for size in sizes:
    p = 0.01
    results.append([])
    print 'Running for size =', size
    while p < 1:
        
        stdout.write("-")
        stdout.flush()
        
        perc_count = 0

        for k in range(trial_count):
            g = random_grid(size, p, 2)
            flow,perc = percolation_hk(g,True)
            if perc:
                perc_count += 1
            #endif
        #endfor
        prob = float(perc_count)/trial_count
        #print 'percolation q=',prob        
        results[n].append(prob)
        P.append(p)
        p += step

    #endwhile
    stdout.write(">|" + "\n")
    n += 1
#endfor

data = open("percolation.data", 'w')
data.write("Occupation \t\t spanning probability\n")
data.write("probability \t")
for sizei in sizes:
    data.write("size ="+repr(sizei)+"\t")
#endfor
data.write("\n")

for i in range(len(results[0])):
    data.write("\n")
    data.write("%f\t" % P[i])
    for j in range(len(sizes)):
        data.write("%f\t" % results[j][i]) 
    #endfor
#endfor
data.close()




