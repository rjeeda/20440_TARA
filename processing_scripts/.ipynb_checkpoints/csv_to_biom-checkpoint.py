import csv
from biom.table import Table, DenseTable
from biom.util import biom_open

# read CSV file

csv_file = "data/otu_csv_table.csv"

with open(csv_file) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    data = [row for row in reader]

# create BIOM table
rows = [row[0] for row in data]
cols = header[1:]
matrix = [[float(val) for val in row[1:]] for row in data]
table = DenseTable(matrix, rows, cols)

# write BIOM table to file
with biom_open('output.biom', 'w') as f:
    table.to_hdf5(f, 'example')
