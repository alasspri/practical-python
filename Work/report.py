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
        for row in rows:
            holding = {'name': row[0],
                       'shares': int(row[1]),
                       'price': float(row[2])}
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


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Find current value and purchase value
current_value = 0
purchase_value = 0

for stock in portfolio:
    purchase_value += stock['shares'] * stock['price']
    current_value += stock['shares'] * prices[stock['name']]

print(f"Current Value: {current_value:.2f}")
print(f"Purchase Value: {purchase_value:.2f}")
print(f"Gain/loss: {current_value - purchase_value:.2f}")