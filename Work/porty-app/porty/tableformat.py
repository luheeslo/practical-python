class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table heading.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        ths = ''.join(f'<th>{header}</th>' for header in headers)
        print(f'<tr>{ths}</tr>')

    def row(self, rowdata):
        tds = ''.join(f'<td>{value}</td>' for value in rowdata)
        print(f'<tr>{tds}</tr>')


def create_formatter(fmt):
    formatter_classes = {'txt': TextTableFormatter,
                         'csv': CSVTableFormatter,
                         'html': HTMLTableFormatter}
    formatter_class = formatter_classes.get(fmt)
    if formatter_class is None:
        raise FormatError(f'Unknown table format {fmt}')
    return formatter_classes[fmt]()


def print_table(portfolio, fields, formatter):
    formatter.headings(fields)
    for p in portfolio:
        rowdata = [str(getattr(p, field)) for field in fields]
        formatter.row(rowdata)


class FormatError(Exception):
    pass
