from flet import *
from features.Database import DataMethods



def login(page):

    def send_forget_password(e):
        page.go("/forgetpassword")

    def send_home(e):
        if DataMethods.verify_login(login_textfield.value, password_textfield.value):
            page.go("/")
        else:
            login_textfield.value = ""
            password_textfield.value = ""
            page.dialog = AlertDialog(content=Row([Text("Usuário ou senha incorretos!", size=18)], alignment=MainAxisAlignment.CENTER), actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
            page.dialog.open = True
        page.update()

    def send_signin(e):
        page.go("/signin")

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    login_textfield = TextField(label="Email", width=300, filled=True, bgcolor=colors.WHITE)
    login_row = Row([login_textfield], alignment=MainAxisAlignment.CENTER)

    password_textfield = TextField(label="Senha", width=300, filled=True, bgcolor=colors.WHITE, password=True, can_reveal_password=True)
    password_row = Row([password_textfield], alignment=MainAxisAlignment.CENTER)

    forget_password = TextButton("Esqueceu a senha ?", on_click=send_forget_password)
    forget_row = Row([forget_password], alignment=MainAxisAlignment.CENTER)

    login_button = ElevatedButton(content=Text("Login", size=15), on_click=send_home, style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), width=140)
    login_button_row = Row([login_button], alignment=MainAxisAlignment.CENTER)

    signin_button = ElevatedButton(content=Text("Cadastrar-se", size=15), on_click=send_signin, style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), width=140)
    signin_button_row = Row([signin_button], alignment=MainAxisAlignment.CENTER)

    or_row = Row([Text("ou", color=colors.BLUE_800, weight=FontWeight.W_600)], alignment=MainAxisAlignment.CENTER)

    content = Stack([Image(src=f"../assets/LoginBackgroundView.png",
                           fit=ImageFit.FILL,
                           width=450, height=900),
                     Column(controls=[Text("", height=195),
                                      Row(controls=[Text("Login",
                                                         size=20,
                                                         weight=FontWeight.W_700)],
                                          alignment=MainAxisAlignment.CENTER),
                                      login_row,
                                      password_row,
                                      forget_row,
                                      login_button_row,
                                      or_row,
                                      signin_button_row],
                            alignment=MainAxisAlignment.CENTER)])
    return content
