import flet
from flet import Page, colors, AppBar, TextButton, ButtonStyle, Container, Row, UserControl, View

# from app_layout import AppLayout


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
        # self.page.add(self.appbar)
        self.page.update()


    # def build(self):
    #     self.layout = AppLayout(self, self.page)
    #     return self.layout
    #
    # def initialize(self):
    #     self.page.views.clear()
    #     self.page.views.append(
    #         View(
    #             "/",
    #             [self.appbar, self.layout]
    #         )
    #     )
    #     self.page.update()
    #     self.page.go("/")


if __name__ == "__main__":
    def main(page: Page):
        page.title = "Arack"
        page.padding = 0
        page.bgcolor = colors.BLUE
        app = ArackApp(page)
        page.add(app)
        page.update()
        # app.initialize()


    flet.app(target=main)
