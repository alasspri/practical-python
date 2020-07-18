# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    value = 0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)

    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            nshares = int(record['shares'])
            shareprice = float(record['price'])
            value += nshares * shareprice
        except ValueError:
            print(f"Row {rowno}: Bad row: {row}")

    f.close()

    return value


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print(f"Total cost {cost}")
