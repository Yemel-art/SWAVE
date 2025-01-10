import flet
from flet import *

def create_signup_container_left(logo_path, padding_left=110):
    return Container(
        Stack([
            Image(
                src=r"F:\your\image\path.jpg",
                width=580,
                height=740,
                fit=ImageFit.COVER,
            ),
            Container(
                Container(
                    Stack([
                        Container(
                            border_radius=100,
                            
                            width=360,
                            height=560,
                            bgcolor='#22ffffff',  
                        ),
                        Container(
                            Container(
                                Column([
                                    Container(
                                        Image(src=logo_path, width=50),
                                        padding=padding.only(150,20)
                                    ),
                                    Text(
                                        "Create Account",
                                        width=360,
                                        size=30,
                                        weight="bold",
                                        text_align="center",
                                    ),
                                    Text(
                                        "Sign up to join SWAVE",
                                        width=360,
                                        text_align="center",
                                        weight="#968"
                                    ),
                                    Container(
                                        TextField(
                                            width=280,
                                            height=30,
                                            hint_text="Create Username",
                                            border="underline",
                                            color="#303030",
                                            prefix_icon=icons.PERSON,                                
                                        ),
                                        padding=padding.only(40,20),
                                    ),
                                    Container(
                                        TextField(
                                            width=280,
                                            height=30,
                                            hint_text="Create Password",
                                            border="underline",
                                            color="#303030",
                                            prefix_icon=icons.LOCK,
                                            password=True,                                
                                        ),
                                        padding=padding.only(40,20),    
                                    ),
                                    Container(
                                        TextField(
                                            width=280,
                                            height=30,
                                            hint_text="Confirm Password",
                                            border="underline",
                                            color="#303030",
                                            prefix_icon=icons.LOCK,
                                            password=True,                                
                                        ),
                                        padding=padding.only(40,20),    
                                    ),
                                    Container(
                                        ElevatedButton(
                                            content=Text(
                                                "SIGN UP",
                                                color="white",
                                                weight="bold",
                                            ),
                                            width=240,
                                            bgcolor="black",
                                        ),
                                        padding=padding.only(45,10),
                                    ),
                                ]),
                            ),
                            border_radius=11,
                            width=360,
                            height=560,
                            bgcolor='#22ffffff',  
                        )
                    ]),
                    padding=padding_left,
                    width=360,
                    height=560,
                ),
                width=580,
                height=740,
            )
        ])
    )

def create_login_container_right(logo_path, padding_left=110):
    return Container(
        Stack([
            Image(
                src=r"C:\\Users\YEMEL LECRAM\Desktop\filmess\yemelbg.jpg",
                width=580,
                height=740,
                fit=ImageFit.COVER,
            ),
            Container(
                Container(
                    Stack([
                        Container(
                            border_radius=11,
                            rotate=Rotate(0.98-1.14),
                            width=360,
                            height=560,
                        ),
                        Container(
                            Container(
                                Column([
                                    Container(
                                        Image(src=logo_path, width=50),
                                        padding=padding.only(150,20)
                                    ),
                                    Container(
                                        content=Text(
                                            "Sign In",
                                            width=360,
                                            size=30,
                                            weight="bold",
                                            text_align="center",
                                        ),
                                        bgcolor="white",
                                        border_radius=11,
                                        padding=10,
                                    ),
                                    Container(
                                        content=Text(
                                            "Welcome back!",
                                            width=360,
                                            text_align="center",
                                            weight="#968"
                                        ),
                                        bgcolor="white",
                                        border_radius=11,
                                        padding=10,
                                    ),
                                    Container(
                                        TextField(
                                            width=280,
                                            height=30,
                                            hint_text="Username",
                                            border="underline",
                                            color="#303030",
                                            prefix_icon=icons.PERSON,                                
                                        ),
                                        bgcolor="white",
                                        border_radius=11,
                                        padding=padding.only(40,20),
                                    ),
                                    Container(
                                        TextField(
                                            width=280,
                                            height=30,
                                            hint_text="Password",
                                            border="underline",
                                            color="#303030",
                                            prefix_icon=icons.LOCK,
                                            password=True,                                
                                        ),
                                        bgcolor="white",
                                        border_radius=11,
                                        padding=padding.only(40,20),    
                                    ),
                                    Container(
                                        TextButton(
                                            "Forgot password?",
                                        ),
                                        bgcolor="transparent",
                                    
                                        border_radius=11,
                                        padding=padding.only(80),
                                    ),
                                    Container(
                                        ElevatedButton(
                                            content=Text(
                                                "SIGN IN",
                                                color="white",
                                                weight="bold",
                                            ),
                                            width=240,
                                            bgcolor="black",
                                        ),
                                        padding=padding.only(45,10),
                                    ),
                                ]),
                            ),
                            border_radius=11,
                            width=360,
                            height=560,
                        )
                    ]),
                    padding=padding_left,
                    width=360,
                    height=560,
                ),
                width=580,
                height=740,
            )
        ])
    )

def main(page: Page):
    page.title = "Sign Up / Sign In"
    page.window_max_width = 1000
    page.window_max_height = 700
    page.scroll = "adaptive"
    page.padding = 0
   
    dual_login = Row(
        controls=[
            create_signup_container_left(r"C:\Users\Adrien\Desktop\groupe 2 ca\my-flet-project\logo groupe.png"),
            create_login_container_right(r"C:\Users\Adrien\Desktop\groupe 2 ca\my-flet-project\logo groupe.png")
        ],
        spacing=0
    )
   
    page.add(dual_login)

if __name__ == "__main__":
    app(target=main)