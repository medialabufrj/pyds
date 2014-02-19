#
# merge.py
# ========
# create a file from 2 files merged
# ---------------------------------
# usage 1: python merge.py
# usage 2: python merge.py file1.csv file2.csv merged.csv
#

import sys

if( len(sys.argv) == 4 ):
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	file3 = sys.argv[3]
else:
	file1 = raw_input("first file: ")
	file2 = raw_input("second file: ")
	file3 = raw_input("new file: ")

fout = open(file3,"w")

for line in open(file1):
    fout.write(line)

fout.write('\n')

for line in open(file2):
    fout.write(line)

print 'done!'
