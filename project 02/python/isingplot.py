from matplotlib.pyplot import *
import sys
import string

def getNumArrFromFile(filename):
    arr = []
    a_file = open(filename,mode='r')
    filestr = a_file.readline()
    filestr = a_file.readline()
    n = 0
    while filestr:
       arr.append([])
       linearr = filestr.split('\n')
       for line in linearr:
           numarr = line.split()
           for numstr in numarr:
               arr[n] = arr[n] +[string.atof(numstr)]
       n += 1
       filestr = a_file.readline()
    return arr
#end def
        
data = getNumArrFromFile('ising.data') 

T = []
Energy= []
Energy2 = []
Magnet = []
Magnet2 = []
Cv = []
susceptibility = []
for i in range(0,len(data)):
    T += [data[i][0]]
    Energy += [data[i][1]]
    Energy2 += [data[i][2]]
    Magnet += [data[i][3]]
    Magnet2 += [data[i][4]]
    Cv += [data[i][5]]
    susceptibility += [data[i][6]]

subplot(221)
plot(T,Energy,'.-', markersize = 13)
grid()
xlabel('Temperature')
ylabel('Energy')

subplot(222)
plot(T,Magnet,'.-', markersize = 13)
grid()
xlabel('Temperature')
ylabel('Magnetization')

subplot(223)
plot(T,Cv,'.-', markersize = 13)
grid()
xlabel('Temperature')
ylabel('Specific heat')

subplot(224)
plot(T,susceptibility,'.-', markersize = 13)
grid()
xlabel('Temperature')
ylabel('Susceptibility')
show()
