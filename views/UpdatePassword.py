from flet import *
from features.User import User
from views.ForgetPassword import *


def updatepassword(page):
    def forget_password(e):
        page.go("/forgetpassword")

    def verify_password(e):
        valid = True
        error_messages = []
        if len(password_textfield.value) < 8:
            valid = False
            error_messages.append("Sua senha deve ter no mínimo 8 caracteres")
        if not any(char.isalpha() for char in password_textfield.value) or not any(char.isdigit() for char in password_textfield.value):
            valid = False
            error_messages.append("Sua senha deve conter letras e números")
        if not valid:
            page.dialog = AlertDialog(
                content=Column(height=60, controls=[
                    *map(Text, error_messages)
                ]),
                actions=[
                    Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)
                ],
            )
            page.dialog.open = True
            page.update()
        if valid:
            email = page.client_storage.get("email")
            print("1 ", email)
            if password_textfield.value == password_confirmation_textfield.value:
                User.edit_password(email, password_textfield.value)
                page.dialog = AlertDialog(
                    content=Row([Text("Senha atualizada com sucesso!", size=18)], alignment=MainAxisAlignment.CENTER),
                    actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
                page.dialog.open = True
                page.update()
                send_login(e)

            else:
                page.dialog = AlertDialog(
                    content=Row([Text("Senhas diferentes", size=18)], alignment=MainAxisAlignment.CENTER),
                    actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
                page.dialog.open = True
                page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def send_login(e):
        page.go("/login")

    password_text = Text("Digite sua nova senha: ", width=300, bgcolor=colors.WHITE)
    password_text_row = Row([password_text], alignment=MainAxisAlignment.CENTER)

    password_textfield = TextField(label="Senha", width=300, filled=True, bgcolor=colors.WHITE, password=True, can_reveal_password=True)
    password_row = Row([password_textfield], alignment=MainAxisAlignment.CENTER)

    password_confirmation_text = Text("Digite novamente sua nova senha: ", width=300, bgcolor=colors.WHITE)
    password_confirmation_text_row = Row([password_confirmation_text], alignment=MainAxisAlignment.CENTER)

    password_confirmation_textfield = TextField(label="Confirmação", width=300, filled=True, bgcolor=colors.WHITE, password=True, can_reveal_password=True)
    password_confirmation_textfield_row = Row([password_confirmation_textfield], alignment=MainAxisAlignment.CENTER)

    confirmation_button = ElevatedButton(content=Text("Confirmar", size=15),
                                         style=ButtonStyle(padding={MaterialState.DEFAULT: 18}),
                                         width=250, bgcolor=colors.BLUE, color=colors.BLACK, on_click=verify_password)
    confirmation_button_row = Row([confirmation_button], alignment=MainAxisAlignment.CENTER)

    content = Stack([Column([Text("", height=25), Row([IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                                                  on_click=forget_password,
                                                                  icon_color=colors.BLACK, icon_size=35),
                                                       Text("                                   ")],
                                                      alignment=MainAxisAlignment.SPACE_AROUND)]),
                     Column(controls=[Text("", height=60),
                                      Row(controls=[Text("Atualizar senha?",
                                                         size=20,
                                                         weight=FontWeight.W_700)],
                                          alignment=MainAxisAlignment.CENTER),
                                      password_text_row,
                                      password_row,
                                      password_confirmation_text_row,
                                      password_confirmation_textfield_row,
                                      confirmation_button_row
                                      ],
                            alignment=MainAxisAlignment.CENTER)])
    return content