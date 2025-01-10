import flet as ft
from flet import Page, Container, Row, Column, Text, IconButton, Image, Stack

def main(page: Page):
    page.scroll = "adaptive"
    page.title = "Music App"
    page.bgcolor = "#FFFFFF"

    Yellow = "#FFFF00"
    White = "#FFFFFF"
    Black = "#000000"

    # Image paths dictionary
    image_paths = {
        "Home": "C:/Users/YEMEL LECRAM/Desktop/images/home.png",
        "Search": "C:/Users/YEMEL LECRAM/Desktop/images/search.png",
        "Library": "C:/Users/YEMEL LECRAM/Desktop/images/library.png",
        "My Songs": "C:/Users/YEMEL LECRAM/Desktop/images/mysongs.png",
        "Settings": "C:/Users/YEMEL LECRAM/Desktop/images/settings.png"
    }

    def show_home_page(e):
        home_content.visible = True
        search_content.visible = False
        page.update()

    def show_search_page(e):
        home_content.visible = False
        search_content.visible = True
        page.update()

    # Sidebar components
    home = Container(
        bgcolor=Yellow,
        width=350,
        content=Row(
            [
                IconButton(icon=ft.icons.HOME, icon_color=Black, icon_size=20, on_click=show_home_page),
                Text("Home", size=15, color=Black, bgcolor=Yellow),
            ]
        )
    )

    sidebar_items = [
        (ft.icons.SEARCH, "Search", show_search_page),
        (ft.icons.LIBRARY_ADD, "Library", None),
        (ft.icons.MUSIC_NOTE, "My songs", None),
        (ft.icons.FAVORITE_ROUNDED, "Favorites", None),
        (ft.icons.SETTINGS, "Settings", None),
    ]

    sidebar_rows = [
        Row(
            [
                IconButton(icon=icon, icon_color=Black, icon_size=20, on_click=on_click),
                Text(text, size=15, color=Black),
            ],
            spacing=10,
        )
        for icon, text, on_click in sidebar_items
    ]

    SideBar = Container(
        bgcolor=White,
        width=10,
        padding=50,
        content=Column(
            [
                Text("   SWAVE", size=30, color=Black, weight="bold"),
                Text("Discover", size=19, color=Black),
                home,
                *sidebar_rows
            ],
            spacing=20,
            alignment="start",
            expand=True
        ),
        expand=True
    )

    # Home Content
    home_content = Container(
        bgcolor=White,
        width=1000,
        padding=0,
        expand=True,
        visible=True,
        content=Stack(
            [
                Image(
                    src=r"F:\\images\\girl.jpg",
                    fit="contain",
                    width=3000,
                    height=600,
                ),
                Container(
                    content=Text(
                        "Satisfy your soul, not your ego",
                        size=30,
                        color=White,
                        weight="bold",
                    ),
                    margin=ft.margin.only(right=300, bottom=2.5),
                    alignment=ft.alignment.bottom_left,
                ),
            ]
        )
    )

    # Search Content
    search_bar = ft.TextField(
        hint_text="Search music from playlist...",
        width=600,
        bgcolor=White,
        border_color=Black,
        border_radius=ft.border_radius.all(3),
        text_size=16,
    )

    title_with_line = Column(
        controls=[
            Text("Title", size=24, weight="bold", color=Yellow),
            Container(width=350, height=6, bgcolor=Yellow, margin=ft.margin.only(top=5)),
        ],
    )

    search_content = Container(
        expand=True,
        visible=False,
        content=Stack([
            # Background image
            Image(
                src=r"C:\\Users\YEMEL LECRAM\Desktop\filmess",
                fit="cover",
                width=3000,
                height=600,
            ),
            # Search interface on top of the image
            Column(
                controls=[
                    Container(content=search_bar, padding=ft.padding.only(left=50, top=50)),
                    Row(
                        controls=[
                            title_with_line,
                            Text("Artist", size=24, weight="bold", color=Yellow),
                        ],
                        alignment="spaceEvenly",
                    ),
                ],
                spacing=20,
                alignment="start",
            ),
        ])
    )
    

    # Main layout
    content = Row([SideBar, home_content, search_content], spacing=0)
    page.add(content)

ft.app(target=main)
