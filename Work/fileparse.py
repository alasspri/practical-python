# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str,
              select=None,
              types=None,
              has_headers=True,
              delimiter=',',
              silence_errors=False) -> list:
    """
    Parse a CSV file into a list of records

    Args:
        silence_errors (): Don't raise parsing errors
        has_headers (): Does the file have headers
        delimiter (string): Optional argument to specificy different csv delimiter
        types (list): Optional list of datatypes to convert
        select (list): Names of the column headers to include
        filename (str): Name of the file

    Returns: A list of records
    """
    if not has_headers and select:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indicies = [headers.index(colname) for colname in select]
                headers = select
            else:
                indicies = []
        else:
            indicies = []

        records = []
        for i, row in enumerate(rows, start=1):
            try:
                if not row:  # skip rows with no data
                    continue
                if indicies:
                    row = [row[index] for index in indicies]
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {e}")
                continue

    return records
