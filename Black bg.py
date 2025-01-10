import flet as ft

def main(page: ft.Page):
    page.title = "S-Wave Music App"
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = "auto"

    # Define the image paths with verified correct paths
    image_paths = {
        "Home": "C:\\Users\YEMEL LECRAM\Desktop\images/home.png",
        "Search": "C:\\Users\YEMEL LECRAM\Desktop\images/search.png",
        "Library": "C:\\Users\YEMEL LECRAM\Desktop\images/library.png",
        "My Songs": "C:\\Users\YEMEL LECRAM\Desktop\images/mysongs.png",
        "Settings": "C:\\Users\YEMEL LECRAM\Desktop\images/settings.png",
    }

    sidebar_items = [
        {"name": "Home", "icon_path": image_paths["Home"]},
        {"name": "Search", "icon_path": image_paths["Search"], "active": False},
        {"name": "Library", "icon_path": image_paths["Library"]},
        {"name": "My Songs", "icon_path": image_paths["My Songs"]},
        {"name": "Settings", "icon_path": image_paths["Settings"]},
    ]

    sidebar = ft.Container(
        width=250,
        bgcolor=ft.colors.WHITE,
        height=page.height,  # Ensure the sidebar stretches to the bottom
        content=ft.Column(
            controls=[
                ft.Text("Discover", size=18, weight="bold", color=ft.colors.BLACK),
                *[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(src=item["icon_path"], width=20, height=20),
                                ft.Text(
                                    item["name"],
                                    size=14,
                                    color=ft.colors.YELLOW if item.get("active") else ft.colors.BLACK,
                                    weight="bold" if item.get("active") else "normal",
                                ),
                            ],
                        ),
                        bgcolor=ft.colors.YELLOW if item.get("active") else ft.colors.TRANSPARENT,
                        padding=ft.Padding(10, 10, 10, 10),
                        border_radius=ft.border_radius.all(10),
                    )
                    for item in sidebar_items
                ],
            ],
            spacing=10,
            scroll="auto",
        ),
    )

    search_bar = ft.TextField(
        hint_text="Search music from playlist...",
        width=800,
        bgcolor=ft.colors.WHITE,
        border_color=ft.colors.YELLOW,
        border_radius=ft.border_radius.all(20),
        text_size=16,
    )

    main_content = ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                search_bar,
                ft.Row(
                    controls=[
                        ft.Text(
                            "Title",
                            size=24,
                            weight="bold",
                            color=ft.colors.YELLOW,
                        ),
                        ft.Text(
                            "Artist",
                            size=24,
                            weight="bold",
                            color=ft.colors.YELLOW,
                        ),
                    ],
                    alignment="spaceEvenly",
                ),
            ],
            spacing=20,
            alignment="start",
        ),
    )

    page.add(
        ft.Row(
            controls=[sidebar, main_content],
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.START  # Ensure alignment at the top
        )
    )

ft.app(target=main)
