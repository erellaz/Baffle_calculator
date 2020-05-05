from __future__ import division
# Calculate the positions and size of a set of baffles for refractor

# A function to calculate the intersection of 2 segments, solving the 2x2 system
# Each line is a 2x2 matrix 

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
#______________________________________________________________________________
# All units need to be consistent (eg all inch or all mm)
# Example Wollensak doublet of 127mm of clear aperture, 145mm od OD and 1200mm of focal length
# Using an aluminum tube of 6"OD, 0.125" wall thickness and a total length of 48 " with a 2" focuser
Dl=5 # Clear diameter of the front lens
d=2  # Focuser diameter
dt=5.75 # Inside diameter of the tube
lt=44.5 # length of tube between the 2 stops
bstop=8
#______________________________________________________________________________

# Invariant point, on the focuser side, x =0
ftop=[0,d/2]
fbot=[0,-1*d/2]

# This will vary from baffle to baffle, start up with the lens
btop=[lt,dt/2]
bbot=[lt,Dl/2]

    
L1 = line(ftop,bbot) #this line is invariant
L2 = line(fbot,btop)
R=(lt, Dl/2)

# start a line collection to plot the rays
lines=[]
colors=[]
# Enter focuser
lines.append([(0,-1*d/2),(0,d/2)])
colors.append([1, 1, 0, 1])

# Enter half lens
lines.append([(lt,-1*Dl/2),(lt,Dl/2)])
colors.append([1, 1, 0, 1])

# Enter L1
lines.append([(ftop[0],ftop[1]),(bbot[0],bbot[1])])
colors.append([1, 0, 0, 1])
lines.append([(ftop[0],-1*ftop[1]),(bbot[0],-1*bbot[1])])
colors.append([1, 0, 0, 1])
# Enter L2
lines.append([(fbot[0],fbot[1]),(btop[0],btop[1])])
colors.append([1, 0,1, 1])

# Enter tube
lines.append([(0,dt/2),(lt,dt/2)])
colors.append([0, 0,0, .5])
lines.append([(0,-1*dt/2),(lt,-1*dt/2)])
colors.append([0, 0,0, .5])

# Calculating baffle so no part of the tube is visible (best baffle, not minimum baffle)
while R[0]>bstop:
    R = intersection(L1, L2)
    print("Baffle position, radius",R)
    btop=[R[0],dt/2]
    bbot=[R[0],R[1]]
    L2 = line(fbot,btop)
    # append the ray
    lines.append([(fbot[0],fbot[1]),(btop[0],btop[1])])
    colors.append([0, 1, 0, 1])
    #append the baffle
    lines.append([(bbot[0],bbot[1]),(btop[0],btop[1])])
    colors.append([0, 0, 0, 1])
#______________________________________________________________________________
# plot that stuff
import pylab as pl
import numpy as np
from matplotlib import collections  as mc

col=np.array(colors)
lc = mc.LineCollection(lines,colors=col)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.set_aspect(1)
#ax.autoscale()
ax.margins(0.1)
fig.set_figwidth(25)


