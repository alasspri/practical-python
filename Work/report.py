# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint


def read_portfolio(filename):
    """
    Reads a portfolio from a file
    """
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            holding = {'name': record['name'],
                       'shares': int(record['shares']),
                       'price': float(record['price'])}
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    """
    Reads stock prices from a file
    """
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices


def make_report(stocks, prices):
    rows = []

    for stock in stocks:
        rows.append((stock['name'],
                     stock['shares'],
                     prices[stock['name']],
                     prices[stock['name']] - stock['price']
                     ))

    return rows


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')

print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
print(('-' * 10 + ' ') * len(headers))

for name, shares, price, change in report:
    format_price = f"${price:.2f}"
    print(f"{name:>10s} {shares:>10d} {format_price:>10s} {change:10.2f}")

