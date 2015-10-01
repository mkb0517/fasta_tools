#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys

a_count = 0
c_count = 0
g_count = 0
t_count = 0
total   = 0.0

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        total += len(line.strip())
        a_count += line.count('A',0)
        c_count += line.count('C',0)
        g_count += line.count('G',0)
        t_count += line.count('T',0)

a_perc = (a_count/total)*100
c_perc = (c_count/total)*100
g_perc = (g_count/total)*100
t_perc = (t_count/total)*100

print("Base counts for file %s:" % sys.argv[1])
print("A: %d (%d%s)" % (a_count, a_perc, '%'))
print("C: %d (%d%s)" % (c_count, c_perc, '%'))
print("G: %d (%d%s)" % (g_count, g_perc, '%'))
print("T: %d (%d%s)" % (t_count, t_perc, '%'))
