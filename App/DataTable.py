from flet import Row, colors, DataTable, DataRow, DataCell, DataColumn, Text


class Table(Row):
    def __init__(self, colums, detail_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heading_row_color = colors.BLACK12
        self.colums = colums
        self.detail_data = detail_data
        self.table = DataTable(
            width=1200 / 3,
            heading_row_color=self.heading_row_color,
            columns=self.columns(),
            rows=self.rows()
        )

    def columns(self):
        c = []
        for col in self.colums:
            c.append(DataColumn(label=Text(col)))
        return c

    def rows(self):
        rows = []
        for r in self.detail_data:
            cells = []
            for q in r:
                cells.append(DataCell(Text(q)))
            rows.append(DataRow(cells=cells))
        return rows
