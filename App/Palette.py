from flet import ElevatedButton, colors, MaterialState, ButtonStyle, Row, ListView
from Database.Database import session, PaletteDb


class Palette(Row):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.button = ElevatedButton(
            text=f"{self.title}",
            on_click=self.on_click,
            height=20,
            # width=400,
            style=ButtonStyle(
                bgcolor={MaterialState.DEFAULT: colors.BLUE_ACCENT_400,
                         MaterialState.HOVERED: colors.BLUE_ACCENT_100},
                color=colors.BLACK
            )
        )

    def on_click(self, e):
        print(self.title)


class PaletteCluster:
    def __init__(self):

        self.p_a = session.query(PaletteDb).filter(PaletteDb.name.like("%A%")).all()
        self.p_b = session.query(PaletteDb).filter(PaletteDb.name.like("%B%")).all()

        self.palette_cluster = Row(
            [self.generate_paletts_column(self.p_a),
             self.generate_paletts_column(self.p_b)]
        )

    def generate_paletts_column(self, p_col):
        paletts_list = []
        cluster = ListView(expand=1, spacing=5.5, padding=10, auto_scroll=True)
        for p in p_col:
            paletts_list.append(p)
        paletts_list.reverse()
        for q in paletts_list:
            cluster.controls.append(Palette(f'{q.name}').button)
        return cluster
