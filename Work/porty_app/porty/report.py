# report.py
#
# Exercise 2.4
from . import fileparse
from . import tableformat
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    """
    Reads a portfolio from a file

    Returns:
        portfolio: dicts of the stocks
    """
    with open(filename) as lines:
        port = Portfolio.from_csv(lines, **opts)

        return port


def read_prices(filename):
    """
    Reads stock prices from a file
    """
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,
                                        has_headers=False,
                                        types=[str, float]))


def make_report(stocks, prices):
    rows = []

    for stock in stocks:
        rows.append((stock.name,
                     stock.shares,
                     prices[stock.name],
                     prices[stock.name] - stock.price
                     ))

    return rows


def print_report(reportdata, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    myportfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(myportfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfile pricefile fmt')
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    import logging
    logging.basicConfig(
        filename='../../app.log',
        filemode='w',
        level=logging.DEBUG
    )
    main(sys.argv)
