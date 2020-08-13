# pcost.py
#
# Exercise 1.27
from report import read_portfolio

import sys


def portfolio_cost(filename):
    value = 0

    portfolio = read_portfolio(filename)

    for stock in portfolio:
        value += stock['shares'] * stock['price']

    return value


def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)