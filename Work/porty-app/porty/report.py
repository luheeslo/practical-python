#!/home/lhel/.pyenv/shims/python
# report.py
#
# Exercise 2.4

from .fileparse import parse_csv
from .portfolio import Portfolio
from .stock import Stock

from . import tableformat


def read_portfolio(filename: str, **opts) -> Portfolio:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as f:
        return Portfolio.from_csv(f)


def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name, price data
    '''

    with open(filename) as f:
        return dict(parse_csv(f, types=[str, float], has_headers=False))


def make_report(portfolio: list, prices: dict) -> list:
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for s in portfolio:
        change = prices[s.name] - s.price
        report.append((s.name,
                       s.shares,
                       prices[s.name],
                       change))
    return report


def calculate_total_cost(portfolio: list) -> float:
    '''
    Calculate the total cost of the portfolio
    '''

    return sum(s.shares*s.price for s in portfolio)


def calculate_portfolio_value(portfolio: list, prices: dict) -> float:
    '''
    Compute the current value of the portfolio
    '''

    return sum(s.shares*prices[s.name] for s in portfolio)


def print_report(report: list, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    '''headers_format = '{:>10s} {:>10s} {:>10s} {:>10s}'
    headers = ('Name', 'Shares', 'Price', 'Change')
    border_bottom = '{:->10s} {:->10s} {:->10s} {:->10s}'.format('', '', '', '')

    print()
    print(headers_format.format(*headers))
    print(border_bottom)
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d}"
              f" {'$' + f'{price:>0.2f}':>10s} {change:>10.2f}")
    print()
    print('Total cost', total_cost)
    print('Current value', portfolio_value)
    print('Gain', portfolio_value - total_cost)'''

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename: str, prices_filename: str, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


# Main function
def main(argv):
    # Parse command line args, environment, etc
    if len(argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile formatter')
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]

    portfolio_report(portfile, pricefile, fmt)


if __name__ == "__main__":
    import logging
    import sys

    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.WARNING,
    )
    main(sys.argv)
