#!/usr/bin/env python

# Command line script to calculate base frequency from a .fasta file

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

a_count = 0
c_count = 0
g_count = 0
t_count = 0
n_count = 0
total   = 0.0

with open(filename, 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            # Header line, skip it
            continue
        total += len(line.strip()) #count all the elements of the sequence including N elements
        a_count += line.count('A',0)
        c_count += line.count('C',0)
        g_count += line.count('G',0)
        t_count += line.count('T',0)
	n_count =+ line.count('N',0)

a_perc = (a_count/total)*100
c_perc = (c_count/total)*100
g_perc = (g_count/total)*100
t_perc = (t_count/total)*100
n_perc = (n_count/total)*100
gc_cont = ((g_count+c_count)/total)*100

print("Base counts for file %s:" % filename)
print("A: %d (%f%s)" % (a_count, a_perc, '%'))
print("C: %d (%f%s)" % (c_count, c_perc, '%'))
print("G: %d (%f%s)" % (g_count, g_perc, '%'))
print("T: %d (%f%s)" % (t_count, t_perc, '%'))
print("N: %d (%f%s)" % (n_count, n_perc, '%'))
print("GC content: %f%s" % (gc_cont, '%'))
