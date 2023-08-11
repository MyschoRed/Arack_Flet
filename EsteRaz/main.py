import flet
from flet import Page, colors, AppBar, TextButton, ButtonStyle, Container, Row

from AppLayout import AppLayout
from DataTable import Table
from Palette import PaletteCluster


class ArackApp:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.appbar = AppBar(
            bgcolor=colors.BLUE_300,
            actions=[
                Row(
                    [Container(
                        content=TextButton(text='Arack', on_click=None, style=ButtonStyle(color=colors.BLACK))),
                        Container(
                            content=TextButton(text='Sklad', on_click=None, style=ButtonStyle(color=colors.BLACK))),
                        Container(
                            content=TextButton(text='Tabule', on_click=None, style=ButtonStyle(color=colors.BLACK)))])
            ]
        )
        self.page.appbar = self.appbar
        self.page.update()

    def build(self):
        palettes_a = PaletteCluster("A").generate_cluster()
        palettes_b = PaletteCluster("B").generate_cluster()
        stack = Row([palettes_a, palettes_b])

        my_table_cols = ['Tabula', 'Ks', 'Poznamka']
        table_data = [["jeden", "10", "nic"],
                      ["dva", "20", "nieco"],
                      ["tri", "30", "hocico"]]
        palette_detail_table = Table(my_table_cols, table_data)
        app_layout = AppLayout(self, self.page)
        app_layout.main_frame.content = stack
        app_layout.detail_frame.content = palette_detail_table.table

        return app_layout


if __name__ == "__main__":
    def main(page: Page):
        page.title = "Arack"

        page.bgcolor = colors.BLUE
        app = ArackApp(page).build()
        page.add(app)
        page.update()


    flet.app(target=main)
