import flet as ft


def app_bar(page):
    navbar_actions = [
        ft.Row([ft.Container(content=ft.TextButton(text='Arack', style=ft.ButtonStyle(color=ft.colors.BLACK))),
                ft.Container(content=ft.TextButton(text='Sklad', style=ft.ButtonStyle(color=ft.colors.BLACK))),
                ft.Container(content=ft.TextButton(text='Tabule', style=ft.ButtonStyle(color=ft.colors.BLACK)))])
    ]
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.BLUE_300,
        actions=navbar_actions
    )
    return page

def show_info():
    info_bar = ft.Container(content=None, bgcolor=ft.colors.WHITE, border_radius=10, height=40, width=page.window_width)
    return info_bar
def palette_generator(row: str):
    palettes = ft.ListView(expand=1, spacing=5.5, padding=10, auto_scroll=True)
    for p in range(24):
        palette_name = f"{row}{p + 1}"
        palettes.controls.append(ft.ElevatedButton(
            text=f"{palette_name}",
            on_click=show_info(),
            height=20,
            width=400,
            style=ft.ButtonStyle(bgcolor={ft.MaterialState.DEFAULT: ft.colors.BLUE_ACCENT_400,
                                          ft.MaterialState.HOVERED: ft.colors.BLUE_ACCENT_100},
                                 color=ft.colors.BLACK)))

    rack_column = palettes
    return rack_column


def main(page: ft.Page):
    page.title = "Arack"
    page.bgcolor = ft.colors.BLUE
    page.auto_scroll = True
    page.window_width = 1200
    page.window_height = 800

    app_bar(page)
    info_bar = ft.Container(content=None, bgcolor=ft.colors.WHITE, border_radius=10, height=40, width=page.window_width)
    form_frame = ft.Container(content=ft.Row([]),
                              width=page.window_width / 3,
                              height=page.window_height - 170,
                              bgcolor=ft.colors.WHITE,
                              border_radius=10)
    main_frame = ft.Container(content=ft.Row([palette_generator("A"), palette_generator("B")]),
                              width=page.window_width / 1.6,
                              height=page.window_height - 170,
                              bgcolor=ft.colors.WHITE,
                              border_radius=10)

    base_layout = ft.Row([form_frame, main_frame])

    page.add(
        info_bar,
        base_layout

    )


ft.app(target=main)
