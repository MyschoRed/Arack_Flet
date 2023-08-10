import flet as ft


def app_bar(page):
    navbar_actions = [
        ft.Row([ft.Container(content=ft.TextButton(text='Arack')),
                ft.Container(content=ft.TextButton(text='Sklad')),
                ft.Container(content=ft.TextButton(text='Tabule'))])
    ]
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.BLUE_300,
        actions=navbar_actions
    )
    return page


def palette_generator(row: str):
    palettes = []
    for p in range(24):
        palette_name = f"{row}{p + 1}"
        palettes.append(ft.ElevatedButton(
            text=f"{palette_name}",
            height=20,
            width=400,
            style=ft.ButtonStyle(bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_ACCENT_400,
                                          ft.MaterialState.HOVERED: ft.colors.BLUE_ACCENT_100},
                                 color=ft.colors.BLACK)))
    palettes.reverse()

    rack_column = ft.Container(content=ft.Column(controls=palettes))
    return rack_column


def main(page: ft.Page):
    page.title = "Arack"

    app_bar(page)

    main_frame = ft.Row([palette_generator("A"), palette_generator("B")], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        main_frame
    )


ft.app(target=main)
