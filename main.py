import flet
from flet import Page, colors, AppBar, TextButton, ButtonStyle, Container, Row, WEB_BROWSER

from App.AppLayout import AppLayout
from App.DataTable import Table
from App.Palette import PaletteCluster
from Database.Database import session, PaletteDb


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
        p_a = session.query(PaletteDb).filter(PaletteDb.name.like("%A%")).all()
        p_b = session.query(PaletteDb).filter(PaletteDb.name.like("%B%")).all()

        palettes_a = PaletteCluster(p_a).generate_cluster()
        palettes_b = PaletteCluster(p_b).generate_cluster()
        stack = Row([palettes_a, palettes_b])

        my_table_cols = ['Tabula', 'Ks', 'Poznamka']
        table_data = [["jeden", "10", "nic"],
                      ["dva", "20", "nieco"],
                      ["tri", "30", "hocico"]]
        palette_detail_table = Table(my_table_cols, table_data)
        app_layout = AppLayout(self, self.page)
        app_layout.main_frame.content = stack
        app_layout.detail_frame.content = palette_detail_table.table
        app_layout.alignment = flet.MainAxisAlignment.CENTER

        return app_layout


if __name__ == "__main__":
    def main(page: Page):
        page.title = "Arack"
        page.window_width = 1300
        page.window_height = 900
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.bgcolor = colors.BLUE
        app = ArackApp(page).build()
        page.add(app)
        page.update()


    flet.app(target=main)
    # flet.app(target=main, view=WEB_BROWSER)
