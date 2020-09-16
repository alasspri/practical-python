#! python
import csv

from follow import follow
from report import read_portfolio
import tableformat


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 4]] for row in rows)
    rows = ([func(val) for func, val in zip([str, float, float], row)] for row in rows)
    rows = (dict(zip(['name', 'price', 'change'], row)) for row in rows)
    return rows


def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)
    stocknames = [stock.name for stock in portfolio]

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])

    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in stocknames)

    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile logfile fmt' % args[0])
    ticker(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
