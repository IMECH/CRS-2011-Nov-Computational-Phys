"""
ising.py: 2D Monte Carlo Simulation of Ising Model
Zhou Lvwen, zhou.lv.wen@gmail.com
10/02/2011
Physical Simulation: project 02

The model consists of discrete variables called spins that can 
be in one of two states. The spins are arranged in a lattice, 
and each spin interacts at most with its nearest neighbors. 

This program has two output files:

     "SpinArray"     Contains 4 snapshots of the spin lattice at
                     of each temperature run.

     "EnergyMagnet"  Contains six columns: each temperature, the
                     average energy at that temp, the ave energy 
                     squared at that temp, the average magnetization 
                     at that temp, the ave magnetizaion squared at 
                     that temp, the heat capacity, and the 
                     susceptibility.
"""

from random import *
from math import *
from sys import *
#########################################################
def initialize(Lx, Ly, ConfigType):
#initialize the spin
   spin = []
   if (ConfigType == 'random'):
      for i in range(0,Lx):
          spin.append([])
          for j in range(0,Ly):
              spin[i] = spin[i] + [choice((-1,1))]
          ##endfor
      ##endfor
   ##endif

   if (ConfigType == 'checkerboard'):
      spinij = 1
      for i in range(0,Lx):
          spin.append([])
          for j in range(0,Ly):
              spin[i] = spin[i] + [-spinij]
              spinij = - spinij
          ##endfor
          spinij = -spinij
      ##endfor
   ##endif

   if (ConfigType == 'interface'):
      for i in range(0,Lx):
          spin.append([])
          for j in range(0,Ly):
              if (i > Lx/2):
                 spin[i] = spin[i] + [ 1]
              else:
                 spin[i] = spin[i] + [-1]
              ##endif
          ##endfor
      ##endfor
   ##endif
   return spin
   
##end def

#########################################################

def CalculateEnergy(spin, Lx, Ly):
#calculate the initial energy 
   E = 0.0
   for i in range(0,Lx):
       for j in range(0,Ly):
           E = E - spin[i][j]*(  \
                                 spin[(i-1)%Lx][j]\
                +spin[i][(j-1)%Ly]               +spin[i][(j+1)%Ly]\
                                +spin[(i+1)%Lx][j] )
       ##endfor
   ##endfor
   return E/2
##end def

#########################################################

def DeltaEnergy(spin, Lx, Ly, i, j):
#calculate the energy difference
    deltaE = 2.0*spin[i][j]*(  \
                               spin[(i-1)%Lx][j]\
                +spin[i][(j-1)%Ly]               +spin[i][(j+1)%Ly]\
                              +spin[(i+1)%Lx][j] )
    return deltaE
##end def

#########################################################

def CalculateMagnet(spin, Lx, Ly):
#calculate the Magnet
   M = 0.0
   for i in range(0,Lx):
       for j in range(0,Ly):
           M = M + spin[i][j]
       ##endfor
   ##endfor
   return M
#end def
#########################################################

Lx = 20; Ly = 20           #number of spins in x and y
N = Lx*Ly                  #total number of spins
Temp = [1+0.1*x for x in range(0,41)] +[2.26918531] 
Temp.sort()                # Temperature
MAXITS=N*200              #simulation steps
WARM = N*100             #equilibrium steps
sample = int(0.333*MAXITS)
data = open("ising.data", 'w')
data.write("Temp"     + "\t" +   
           "Energy"   + "\t" +  
           "Energy^2" + "\t" + 
           "Magnet"   + "\t" + 
           "Magnet^2" + "\t" +    
           "C_v"      + "\t" +     
           "susceptibility"+ "\n")

array = open("ising.spin", 'w')

print("Two-dimensional Ising Model - Metropolis simulation")
print("---------------------------------------------------")
for T in Temp:
    EnergyAve = 0.0
    MagnetAve = 0.0
    Energy2Ave = 0.0
    Magnet2Ave = 0.0
    n = 0
    # Initialize Type = {'random', 'checkerboard', 'interface'}
    spin = initialize(Lx,Ly,'checkerboard') 
    Energy = CalculateEnergy(spin,Lx, Ly) # Initialize energy
    print "Running program for T =", T;

    array.write("-----------" + "temperture = " + repr(T) + "-----------" + "\n")
    for its in range (0,MAXITS):

        # choose a random spin (i,j)
        i = randint(0,Lx-1)
        j = randint(0,Ly-1)

        deltaE = DeltaEnergy(spin, Lx, Ly, i, j)

        # Accept or refuse the change based on Metropolis criterion
        if (exp(-deltaE/T)>random()):
           spin[i][j] = -spin[i][j]
           Energy +=  deltaE
        ##endif    

        Magnet = CalculateMagnet(spin, Lx, Ly) 
        if (its >= WARM):
           EnergyAve += Energy/N
           Energy2Ave += (Energy/N)**2
           MagnetAve += Magnet/N
           Magnet2Ave += (Magnet/N)**2
        ##endif
        if (its == n*sample):
           array.write("nsteps = " + repr(its) + "\t" + "Energy = "+ repr(Energy/N) + "\n")
           array.write(repr(spin) + "\n")
           n += 1
        ##endif

        if (its%int(0.02*MAXITS)==0): 
            stdout.write("-")
            stdout.flush()
    stdout.write(">|" + "\n")
    array.write("\n")
    EnergyAve  /= (MAXITS-WARM)
    Energy2Ave /= (MAXITS-WARM)
    MagnetAve  /= (MAXITS-WARM)
    Magnet2Ave /= (MAXITS-WARM)
    Cv = (Energy2Ave - EnergyAve**2)/T**2
    susceptibility = (Magnet2Ave - MagnetAve**2)/T
    data.write(repr(T)             + "\t" + 
               repr(EnergyAve)     + "\t" +  
               repr(Energy2Ave)    + "\t" + 
               repr(abs(MagnetAve))+ "\t" + 
               repr(Magnet2Ave)    + "\t" + 
               repr(Cv)            + "\t" + 
               repr(susceptibility)+ "\n")
#end for
data.close()
array.close()

print(" M/spin and E/spin values written in ising.data")
print(" spin array written in ising.spin")
print(" Done ... Performing production steps ...")
