import flet
from flet import Page, colors, AppBar, TextButton, ButtonStyle, Container, Row, WEB_BROWSER

from App.AppLayout import AppLayout
from App.DataTable import Table
from App.Palette import PaletteCluster


class ArackApp:
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.palette_cluster = Row()
        self.palette_detail_table = Table
        self.appbar = AppBar(
            bgcolor=colors.BLUE_300,
            actions=[
                Row(
                    [Container(
                        content=TextButton(text='Arack', on_click=self.show_arack,
                                           style=ButtonStyle(color=colors.BLACK))),
                        Container(
                            content=TextButton(text='Sklad', on_click=None, style=ButtonStyle(color=colors.BLACK))),
                        Container(
                            content=TextButton(text='Tabule', on_click=None, style=ButtonStyle(color=colors.BLACK)))])
            ]
        )
        self.page.appbar = self.appbar
        self.page.update()

    def show_arack(self, e):
        self.palette_cluster.visible = True
        print(self.palette_cluster.visible)
        self.page.update()

    def build(self):

        self.palette_cluster = PaletteCluster().palette_cluster
        self.palette_cluster.visible = False

        my_table_cols = ['Tabula', 'Ks', 'Poznamka']
        table_data = [["jeden", "10", "nic"],
                      ["dva", "20", "nieco"],
                      ["tri", "30", "hocico"]]
        palette_detail_table = Table(my_table_cols, table_data).table
        palette_detail_table.visible = False

        # render content in layout
        app_layout = AppLayout(self, self.page)
        app_layout.main_frame.content = self.palette_cluster
        app_layout.detail_frame.content = palette_detail_table
        app_layout.alignment = flet.MainAxisAlignment.CENTER

        return app_layout


if __name__ == "__main__":
    def main(page: Page):
        page.title = "Arack"
        page.window_width = 1200
        page.window_height = 800
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.bgcolor = colors.BLUE
        app = ArackApp(page).build()
        page.add(app)
        page.update()


    flet.app(target=main)
    # flet.app(target=main, view=WEB_BROWSER)
