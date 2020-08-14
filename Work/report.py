# report.py
#
# Exercise 2.4
import fileparse


def read_portfolio(filename: str) -> list:
    """
    Reads a portfolio from a file

    Returns:
        list: dicts of the stocks
    """
    with open(filename) as lines:
        return fileparse.parse_csv(lines,
                                   select=['name', 'shares', 'price'],
                                   types=[str, int, float])


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
        rows.append((stock['name'],
                     stock['shares'],
                     prices[stock['name']],
                     prices[stock['name']] - stock['price']
                     ))

    return rows


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')

    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        format_price = f"${price:.2f}"
        print(f"{name:>10s} {shares:>10d} {format_price:>10s} {change:10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    myportfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(myportfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfile pricefile')
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
