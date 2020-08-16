class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings
        """

        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data
        """

        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-"*10 + " ")*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f"<th>{header}</th>", end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for cell in rowdata:
            print(f"<th>{cell}</th>", end='')
        print('</tr>')


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown format {name}")


def print_table(rawdata, columns, formatter):
    formatter.headings(columns)
    for item in rawdata:
        row = []
        for colname in columns:
            row.append(str(getattr(item, colname)))
        formatter.row(row)
