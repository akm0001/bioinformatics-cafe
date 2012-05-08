#!/home/berald01/.local/bin/python

import sys

if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    sys.exit("""
    Reformat a space or tab separated file to have each column aligned by inserting the
    appropriate number of spaces
    
    E.g. from
    fc.enriched.bed 314660500       mc.enriched.bed 49501300        18811600        5.98    295848900       94.02
    hmc.enriched.bed        319880500       fc.enriched.bed 314660500       167726500       52.43   152154000       47.57
    
    TO:
    fc.enriched.bed   314660500  mc.enriched.bed 49501300   18811600   5.98   295848900  94.02
    hmc.enriched.bed  319880500  fc.enriched.bed 314660500  167726500  52.43  152154000  47.57
    
    USAGE
        format_table.py <table-file> <min-space>
    <table-file>: File to format. Use - to read from stdin (e.g. less myfile | format_table.py -)
    <min-space>:  Minimum number of spaces to separate the columns. Default: 4

    TODO:
        - Read CSV files: Now a column is split at every space (tab or space, one or more times).
        - Allow custom separator (pass to line.split())
        - Allow rugged files.
            """)

if len(sys.argv) == 3:
    spacer= ' ' * int(sys.argv[2])
else:
    spacer= ' '*4
if sys.argv[1] == '-':
    fh= sys.stdin
else:
    fh= open(sys.argv[1])

table= []
maxcols= 0
for line in fh:
    line= line.strip().split()
    if len(line) > maxcols:
        maxcols= len(line)
    table.append(line)

## Get max column size for each column:
colwidths= [0] * maxcols 
for i in range(0, maxcols):
    for line in table:
        cell= line[i]
        if len(cell) > colwidths[i]:
            colwidths[i]= len(cell)
for line in table:
    for i in range(0, len(line)):
        colOffset= colwidths[i]
        cell= line[i]
        nspace= colOffset - len(cell)
        line[i]= cell + ' '*nspace
    print(spacer.join(line))
sys.exit()
    