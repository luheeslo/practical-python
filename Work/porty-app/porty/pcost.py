# pcost.py
#
# Exercise 1.27

import csv
import sys

from .report import read_portfolio


def portfolio_cost(filename):
    '''Computes the total cost (shares*prices) of a portfolio file'''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    portfile = argv[1]
    print('Total cost:', portfolio_cost(portfile))


if __name__ == "__main__":
    import logging
    import sys

    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.WARNING,
    )
    main(sys.argv)
