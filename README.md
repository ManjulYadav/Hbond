# Hbond
hbondcnt.py - count number of hydrogen bonds from the towhee output PDB file, given it, satisfies two conditions.
    1. distance between donor and acceptor is less than 3.0 Armstrong.
    2. the angle formed by (H--O-H) is less than 20 degrees.
    
loopercn.sh - loop hbondcnt.py over all the pdb files from 30000 to 200000 steps.
