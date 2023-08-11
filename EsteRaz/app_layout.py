# from flet import Row, Page, Control, Column, Text, MainAxisAlignment, CrossAxisAlignment


# class AppLayout(Row):
#     def __init__(self, app, page: Page, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.app = app
#         self.page = page
#         self._active_view: Control = Column(controls=[Text('Active View')], alignment=MainAxisAlignment.CENTER,
#                                             horizontal_alignment=CrossAxisAlignment.CENTER)
#
#     @property
#     def active_view(self):
#         return self._active_view
#
#     @active_view.setter
#     def active_view(self, view):
#         self._active_view = view
#         self.update()
