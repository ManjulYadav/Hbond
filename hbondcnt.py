#!/usr/bin/env python3

import sys
import numpy as np

# FUNCTIONS
# ----------------------------------------


def vectorize_atom(A, B):
    """A and B are 2 numpy array representing the location of 2 atoms.
    This function returns A-B normalized"""
    temp = A-B
    norm = np.sqrt(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2])
    return temp/norm


def dist(A, B):
    """A and B are 2 numpy array representing the location of 2 atoms.
    This function returns the distance between A and B"""
    temp = A-B
    d = np.sqrt(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2])
    return d


def angle_rad(v, w):
    """v and w are 2 3D vectors normalized.
    This function returns the angle between v and w in radians"""
    tot = v[0]*w[0] + v[1]*w[1] + v[2]*w[2]
    return np.arccos(tot)


# FILE HANDLING
# ----------------------------------------
if len(sys.argv) != 2:
    print("Invalid input")
    sys.exit(1)

fname = sys.argv[1]

f = open(fname, 'r')
ln = f.readlines()
f.close()

# VARIABLE DEFN
# ----------------------------------------
num = len(ln)
num -=2
dist_cut = 3.0  # Distance cutoff of hbond
angl_cut_deg = 20.0  # Angle cutoff for hbond in degree
angl_cut = angl_cut_deg*2*np.pi/360.0  # Angle conversion to rad
num_hbond = 0  # Number of hydrogen bonds

# H-BOND CHECKER
# ----------------------------------------
for i in range(0, num, 1):
    if ln[i][13] != 'O':  # Check if atom is Oxygen(Donor)
        continue
    # Get the coordinates of Donor Oxygen
    dnr_O = np.array([float(ln[i][30:38]), float(ln[i][38:46]), float(ln[i][46:54])])
    # Get the coordinates of Donor Hydrogen (Assumption, it is the next one in the list)
    dnr_H = np.array([float(ln[i+1][30:38]), float(ln[i+1][38:46]), float(ln[i+1][46:54])])
    for j in range(0, num, 1):
        if ln[j][13] != 'O':  # Check if atom is Oxygen(Acceptor)
            continue
        if j==i:
            continue
        # Get the coordinates of acceptor Oxygen
        apt_O = np.array([float(ln[j][30:38]), float(ln[j][38:46]), float(ln[j][46:54])])
        if dist(dnr_O, apt_O) > dist_cut:
            continue

	    #Vectors to calculate HDA angle
        v = vectorize_atom(dnr_H, dnr_O)
        w = vectorize_atom(apt_O, dnr_O)

        """
        #Vectors to calculate DHA angle
        v = vectorize_atom(dnr_O,dnr_H)
        w = vectorize_atom(apt_O,dnr_H)
        """
        if angle_rad(v, w) <= angl_cut:
            num_hbond += 1

print(num_hbond)
