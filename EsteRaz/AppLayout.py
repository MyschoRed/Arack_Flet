from flet import Row, Page, Container, colors


class AppLayout(Row):
    def __init__(self, app, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.detail_frame = Container(content=Row(),
                                      width=1200 / 3,
                                      height=800 - 170,
                                      bgcolor=colors.WHITE,
                                      border_radius=10)

        self.main_frame = Container(content=Row(),
                                    width=1200 / 1.556,
                                    height=800 - 170,
                                    bgcolor=colors.WHITE,
                                    border_radius=10)
        self.frame = Row(controls=[self.detail_frame, self.main_frame])
        self.controls = [self.frame]
