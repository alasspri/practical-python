# pcost.py
#
from report import read_portfolio


def portfolio_cost(filename):
    value = 0

    portfolio = read_portfolio(filename)

    return portfolio.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)