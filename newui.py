import flet as ft

def create_home_page(page: ft.Page):
    page.title = "Music App"
    page.padding = 0
    page.bgcolor = "#800080"
    
    white = "#FFFFFF"
    purple = "#800080"

    def handle_hover(e):
        container = e.control
        is_hovered = e.data == "true"
        container.bgcolor = purple if is_hovered else white
        row_content = container.content
        row_content.controls[0].icon_color = white if is_hovered else purple
        row_content.controls[1].color = white if is_hovered else purple
        container.update()

    def handle_click(e):
        print(f"Clicked on {e.control.data}")
        page.update()

    swave_title = ft.Container(
        content=ft.Text("SWAVE", size=30, weight="bold", color=purple),
        margin=ft.margin.only(bottom=-20, top=0),
        alignment=ft.alignment.top_left,
    )

    menu_items = [
        ("HOME", ft.icons.HOME),
        ("SEARCH", ft.icons.SEARCH),
        ("LIBRARY", ft.icons.LIBRARY_MUSIC),
        ("MUSIC", ft.icons.MUSIC_NOTE),
        ("SETTINGS", ft.icons.SETTINGS)
    ]

    sidebar_items = [
        ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(icon=icon, icon_color="#800080", icon_size=24),
                    ft.Text(item, color="#800080", size=16, weight="bold")
                ],
                spacing=10,
            ),
            bgcolor=white,
            padding=10,
            margin=5,
            border_radius=10,
            width=400,
            on_hover=handle_hover,
            on_click=handle_click,
            data=item,
        ) for item, icon in menu_items
    ]

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column([swave_title] + sidebar_items, spacing=50),
                    bgcolor="#D8BFD8",
                    padding=20,
                    width=400,
                    height=page.window_height,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Image(
                                src="C:\\Users\YEMEL LECRAM\Downloads\head-removebg-preview (1).png",
                                width=page.window_width - 400,
                                height=page.window_height,
                                fit=ft.ImageFit.COVER,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    width=page.window_width - 400,
                    height=page.window_height,
                    alignment=ft.alignment.top_center,
                )
            ],
            spacing=0,
        )
    )

def main(page: ft.Page):
    page.title = "Music App Login"
    page.window_width = 400
    page.window_height = 900
    page.bgcolor = "#2b1b3b"
    page.padding = 20

    horizontal_offset = 450  
    vertical_offset = 50    

    def handle_signup(e):
        signup_container.visible = False
        signin_container.visible = True
        page.update()

    def handle_signin(e):
        page.clean()
        create_home_page(page)
        page.update()

    signup_container = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,  
            controls=[
                ft.Text("Create account or login if you have one", size=16, weight="bold", color="black"),
                ft.TextField(label="Create username", width=300, bgcolor="#FFFFFF", border_color="#8a6b9c"),
                ft.TextField(label="Create password", password=True, bgcolor="#FFFFFF", width=300, border_color="#8a6b9c"),
                ft.TextField(label="Confirm password", password=True, width=300, bgcolor="#FFFFFF", border_color="#FFFFFF"),
                ft.ElevatedButton(text="Sign Up", width=300, bgcolor="#8a6b9c", color="white", on_click=handle_signup),
                ft.Container(height=-100),
                ft.Image(
                    src="C:\\Users\YEMEL LECRAM\Downloads\man_music-removebg-preview (1).png",
                    width=150,
                    height=300,
                    fit=ft.ImageFit.CONTAIN,
                )
            ]
        ),
        bgcolor="#D8BFD8",
        padding=20,
        border_radius=10,
        width=400,
        height=500,
        visible=True,
        margin=ft.margin.only(top=vertical_offset, left=horizontal_offset)
    )

    signin_container = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,  
            controls=[
                ft.Text("Welcome to SWAVE", size=20, weight="bold", color="black"),
                ft.TextField(label="Enter username", width=300, bgcolor="#FFFFFF", border_color="#8a6b9c"),
                ft.TextField(label="Enter password", password=True, bgcolor="#FFFFFF", width=300, border_color="#8a6b9c"),
                ft.ElevatedButton(text="Sign In", width=300, bgcolor="#8a6b9c", color="white", on_click=handle_signin),
                ft.Container(height=-100),
                ft.Image(
                    src="C:\\Users\YEMEL LECRAM\Downloads\man_music-removebg-preview (1).png",
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,
                )
            ]
        ),
        bgcolor="#D8BFD8",
        padding=20,
        border_radius=10,
        width=400,
        height=500,
        visible=False,
        margin=ft.margin.only(top=vertical_offset, left=horizontal_offset)
    )

    page.add(signup_container, signin_container)
    page.update()

ft.app(target=main)
