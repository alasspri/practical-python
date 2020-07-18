# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    value = 0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    next(rows)

    for row in rows:
        try:
            nshares = int(row[1])
            shareprice = float(row[2])
            value += nshares * shareprice
        except ValueError:
            print('Bad data, skipping line')

    f.close()

    return value


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost {cost}")
