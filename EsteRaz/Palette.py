from flet import ElevatedButton, colors, MaterialState, ButtonStyle, Row, ListView


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
        pass


class PaletteCluster:
    def __init__(self, column_title):
        self.column_title = column_title
        self.cluster = ListView(expand=1, spacing=5.5, padding=10, auto_scroll=True)

    def generate_cluster(self):
        for p in range(24, 0, -1):
            self.cluster.controls.append(Palette(f'{self.column_title}{p}').button)
        return self.cluster
