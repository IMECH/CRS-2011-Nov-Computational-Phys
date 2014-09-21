"""
Percolation_hk.py: Apply the Hoshen-Kopelman Algorithm for Cluster Spanning
Based on http://www.ocf.berkeley.edu/~fricke/projects/hoshenkopelman/hoshenkopelman.html

Zhou Lvwen, zhou.lv.wen@gmail.com
Physical Simulation: project 01
"""

from grid import *



def percolation_hk(input_grid, short=False):
    size = len(input_grid)
    for i in range(size):
        for j in range(size):
            input_grid[i][j] = 1 - input_grid[i][j]
    n_labels = 0 # number of labels used so far

    labels = [0]*(size*size)

    for i in range(size):
        for j in range(size):
            if input_grid[i][j] == 1:
               # check the neighbors of this cell, up and to the left
               up = 0;
               left = 0;
               if i>0 :
                  up = input_grid[i-1][j]
               if j>0 :
                  left = input_grid[i][j-1] 

               if up==0 and left == 0: # new cluster
                  n_labels  = n_labels + 1
                  labels[n_labels] = n_labels
                  input_grid[i][j] = n_labels
               elif up==0 or left==0: # same cluster 
                  input_grid[i][j] = max(up,left)
               else: # two clusters 
                   # dereference the label until it points to itself
                   while labels[up]<up: 
                       up = labels[up]
                   while labels[left]<left:
                       left = labels[left]
                   input_grid[i][j]=min(up,left)
                   labels[max(up,left)] = min(up,left)
    # Renumber the labels so that they're continuous, and eliminate cluster aliases
    j = 0
    for i in range(n_labels):
        if labels[i]==i:
           labels[i] = j
           j+=1
        else:
           labels[i] = labels[labels[i]]
    # apply the relabeling to the input_grid
    for i in range(size):
        for j in range(size):
            input_grid[i][j] = labels[input_grid[i][j]]
    
    return input_grid, ifspanning(input_grid)



def ifspanning(input_grid):
    size = len(input_grid)
    n = 0
    label = max(input_grid[0])
    if label>0:
       for i in range(size):
            if input_grid[size-1][i] >0 and input_grid[size-1][i]<=label:
               return True
    return False


