# pcost.py
#
# Exercise 1.27

value = 0

f = open('Data/portfolio.csv', 'rt')
next(f)

for row in f:
    rowdata = row.strip().split(',')
    value += int(rowdata[1]) * float(rowdata[2])

f.close()

print(f"Total cost {value}")
