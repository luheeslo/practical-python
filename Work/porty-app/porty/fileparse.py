# fileparse.py
#
# Exercise 3.3

import csv
import logging

log = logging.getLogger(__name__)


def parse_csv(f,
              select=None,
              types=None, has_headers=True, delimiter=',', silence_errors=False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    if isinstance(f, str):
        raise ValueError("accept only file-like objects")

    rows = csv.reader(f, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []
    indices = []
    if select and headers:
        indices = [headers.index(s) for s in select]
        headers = select
    records = []
    for line, row in enumerate(rows, start=1):
        if not row:
            continue
        if types:
            try:
                row = [convert(value) for convert, value in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning(f"Row {line}: Couldn't convert {row}")
                    log.debug(f"Row {line}: {e}")
                continue

        if indices:
            row = [row[i] for i in indices]

        record = dict(zip(headers, row)) if headers else tuple(row)
        records.append(record)

    return records
