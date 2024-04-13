from flet import *
from features.Database import DataMethods


def forgetpassword(page):

    def send_login(e):
        page.go("/login")

    email_text = Text("Digite seu email para recuperação: ", width=300, bgcolor=colors.WHITE)
    email_row = Row([email_text], alignment=MainAxisAlignment.CENTER)

    login_textfield = TextField(label="Email", width=300, filled=True, bgcolor=colors.WHITE)
    login_row = Row([login_textfield],alignment=MainAxisAlignment.CENTER)

    send_code = ElevatedButton(content=Text("Enviar código para o Email", size=15), style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), width=250, bgcolor=colors.BLUE, color=colors.BLACK)
    send_code_row = Row([send_code], alignment=MainAxisAlignment.CENTER)

    code_text = Text("Digite o código: ", width=300, bgcolor=colors.WHITE)
    code_text_row = Row([code_text], alignment=MainAxisAlignment.CENTER)

    code_textfield = TextField(label="Código", width=300, filled=True, bgcolor=colors.WHITE)
    code_textfield_row = Row([code_textfield], alignment=MainAxisAlignment.CENTER)

    confirmation_button = ElevatedButton(content=Text("Confirmar", size=15), style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), width=250, bgcolor=colors.BLUE, color=colors.BLACK)
    confirmation_button_row = Row([confirmation_button], alignment=MainAxisAlignment.CENTER)

    content = Stack([Column([Text("", height=25), Row([IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                     on_click=send_login,
                                     icon_color=colors.BLACK, icon_size=35), Text("                                   ")], alignment=MainAxisAlignment.SPACE_AROUND)]),
                     Column(controls=[Text("", height=60),
                                      Row(controls=[Text("Esqueceu a senha ?",
                                                         size=20,
                                                         weight=FontWeight.W_700)],
                                          alignment=MainAxisAlignment.CENTER),
                                      email_row,
                                      login_row,
                                      send_code_row,
                                      code_text_row,
                                      code_textfield_row,
                                      confirmation_button_row
                                      ],
                            alignment=MainAxisAlignment.CENTER)])
    return content
