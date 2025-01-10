import flet as ft
from flet import Page, Container, Row, Column, Text, IconButton, Image, Stack

def main(page: Page):
    # ... (keep existing imports and initial setup)

    # Update the home container width to match new sidebar
    home = Container(
        bgcolor=Yellow,
        width=160,  # Reduced width
        content=Row(
            [
                IconButton(icon=ft.icons.HOME, icon_color=Black, icon_size=20, on_click=show_home_page),
                Text("Home", size=15, color=Black, bgcolor=Yellow),
            ]
        )
    )

    # Update the SideBar container
    SideBar = Container(
        bgcolor=White,
        width=180,  # Reduced width
        padding=15,  # Reduced padding
        content=Column(
            [
                Text("   SWAVE", size=30, color=Black, weight="bold"),
                Text("Discover", size=19, color=Black),
                home,
                *sidebar_rows
            ],
            spacing=15,  # Reduced spacing
            alignment="start",
            expand=True
        ),
        expand=True
    )

    # Update the search_content container with background image
    search_content = Container(
        expand=True,
        visible=False,
        content=Stack([
            Image(
                src=r"C:\\Users\YEMEL LECRAM\Desktop\filmess\search_background.jpg",  # Add your background image here
                fit="cover",
                width=3000,
                height=600,
            ),
            Column(
                controls=[
                    Container(
                        content=search_bar,
                        padding=ft.padding.only(left=50, top=50)
                    ),
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

    # Keep the rest of the code the same
