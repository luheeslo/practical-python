# ticker.py


import csv

from .follow import follow
from .tableformat import create_formatter


def select_columns(rows, indices):
    """TODO: Docstring for select_columns.

    :row: TODO
    :indices: TODO
    :returns: TODO

    """
    return ([row[index] for index in indices]
            for row in rows)


def convert_types(rows, types):
    return ([func(val) for func, val in zip(types, row)]
            for row in rows)


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)


def parse_stock_data(lines, fields=None):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    if fields:
        rows = make_dicts(rows, fields)
    return rows


def ticker(portfile, logfile, fmt):
    import report
    fields = ['name', 'price', 'change']
    formatter = create_formatter(fmt)
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile), fields)
    rows = filter_symbols(rows, portfolio)

    formatter.headings([field.title() for field in fields])
    for r in rows:
        rowdata = [str(r[field]) for field in fields]
        formatter.row(rowdata)


if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
