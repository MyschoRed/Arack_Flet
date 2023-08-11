import flet as ft

from settings import BLACK


def main(page: ft.Page):
    page.title = "Arack"
    page.bgcolor = ft.colors.BLUE
    page.auto_scroll = True
    page.window_width = 1200
    page.window_height = 800

    table = ft.DataTable(
        width=1200 / 3,
        heading_row_color=ft.colors.BLACK12,
        columns=[
            ft.DataColumn(label=ft.Text("Tabula", color=BLACK)),
            ft.DataColumn(label=ft.Text("Pocet", color=BLACK)),
            ft.DataColumn(label=ft.Text("Poznamka", color=BLACK))
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("prva", color=BLACK)),
                ft.DataCell(ft.Text("43", color=BLACK)),
                ft.DataCell(ft.Text("poznamka", color=BLACK))]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("prva", color=BLACK)),
                ft.DataCell(ft.Text("43", color=BLACK)),
                ft.DataCell(ft.Text("poznamka", color=BLACK))]),
        ])

    def table_on():
        print("table turn on")
        table.visible = True

    navbar_actions = [
        ft.Row(
            [ft.Container(
                content=ft.TextButton(text='Arack', on_click=table_on, style=ft.ButtonStyle(color=BLACK))),
                ft.Container(content=ft.TextButton(text='Sklad', on_click=None, style=ft.ButtonStyle(color=BLACK))),
                ft.Container(
                    content=ft.TextButton(text='Tabule', on_click=None, style=ft.ButtonStyle(color=BLACK)))])
    ]
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.BLUE_300,
        actions=navbar_actions
    )

    def palette_button(palette_name):
        btn = ft.ElevatedButton(
            text=f"{palette_name}",
            on_click=None,
            height=20,
            width=400,
            style=ft.ButtonStyle(
                bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_ACCENT_400,
                         ft.MaterialState.HOVERED: ft.colors.BLUE_ACCENT_100},
                color=ft.colors.BLACK
            )
        )
        return btn

    def palette_generator(row: str):
        palettes = ft.ListView(expand=1, spacing=5.5, padding=10, auto_scroll=True)
        for p in range(24, 0, -1):
            palette_name = f"{row}{p}"
            palettes.controls.append(palette_button(palette_name))

        rack_column = palettes
        return rack_column

    detail_frame = ft.Container(content=ft.Row([table]),
                                width=1200 / 3,
                                height=800 - 170,
                                bgcolor=ft.colors.WHITE,
                                border_radius=10, alignment=ft.alignment.top_center)

    main_frame = ft.Container(content=ft.Row([palette_generator("A"), palette_generator("B")]),
                              width=1200 / 1.556,
                              height=800 - 170,
                              bgcolor=ft.colors.WHITE,
                              border_radius=10)
    # layout
    info_bar = ft.Container(content=None, bgcolor=ft.colors.WHITE, border_radius=10, height=40, width=page.window_width)
    base_layout = ft.Row([detail_frame, main_frame])
    table.visible = False
    page.add(
        info_bar, base_layout
    )


ft.app(target=main)
