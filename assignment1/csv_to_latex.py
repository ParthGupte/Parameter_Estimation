import csv
import os

filename = "model_table_Q3"
f = open(os.path.dirname(__file__)+"/"+filename+".csv",'r')
csvreader = csv.reader(f)
header = next(csvreader)
nocols = len(header)

table_type = '|c'*nocols+'|'
cmd = "\\begin{tabular}{"+table_type+"} \n \\hline \n"


def rowtoline(row, roundoff = False):
    n = 0
    line = ''
    for col in row:
        if n == 0:
            line += col
            n += 1
        else:
            if roundoff == True:
                col_float = float(col)
                col_rounded = round(col_float,2)
                col = str(col_rounded)  
            line += ' & ' + col
    line += '\\\\ \n'
    return line

head_line = rowtoline(header)
cmd += head_line + '\\hline \n'

for row in csvreader:

    line = rowtoline(row,roundoff = False)
    cmd += line + '\\hline \n' 

cmd += "\\end{tabular}"



print(cmd)
