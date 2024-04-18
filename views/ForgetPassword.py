from flet import *
from features.Database import DataMethods
import uuid
import smtplib
from email.mime.text import MIMEText

generated_token = None


def forgetpassword(page):

    def send_login(e):
        page.go("/login")

    def generate_token():
        global generated_token
        generated_token = uuid.uuid4().hex
        return generated_token

    def send_token_email(e):
        global email
        email = login_textfield.value
        page.client_storage.set("email", email)
        generated_token = generate_token()
        message = MIMEText(f"Seu token de acesso: {generated_token}")
        message['Subject'] = 'Token de autenticação 4Health'
        message['From'] = 'email_4Health' #opção less secureemail_4Health
        message['To'] = email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login('email_4Health',
                             'senha_4Health') #Tem que ativar a opção Less Secure do google para funcionar, no email que esta enviando.
                server.sendmail(message['From'], message['To'], message.as_string())
                print("Email enviado com sucesse!")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    def verify_token(e):
        entered_token = code_textfield.value
        if entered_token == generated_token:
            page.go("/updatepassword")
        else:
            print("Código incorreto.")
            page.dialog = AlertDialog(
                content=Row([Text("Código incorreto!", size=18)], alignment=MainAxisAlignment.CENTER),
                actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
            page.dialog.open = True
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    email_text = Text("Digite seu email para recuperação: ", width=300, bgcolor=colors.WHITE)
    email_row = Row([email_text], alignment=MainAxisAlignment.CENTER)

    login_textfield = TextField(label="Email", width=300, filled=True, bgcolor=colors.WHITE)
    login_row = Row([login_textfield],alignment=MainAxisAlignment.CENTER)

    send_code_button = ElevatedButton(content=Text("Enviar código para o Email", size=15), on_click=send_token_email, style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), width=250, bgcolor=colors.BLUE, color=colors.BLACK)
    send_code_row = Row([send_code_button], alignment=MainAxisAlignment.CENTER)

    code_text = Text("Digite o código: ", width=300, bgcolor=colors.WHITE)
    code_text_row = Row([code_text], alignment=MainAxisAlignment.CENTER)

    code_textfield = TextField(label="Código", width=300, filled=True, bgcolor=colors.WHITE)
    code_textfield_row = Row([code_textfield], alignment=MainAxisAlignment.CENTER)

    confirmation_button = ElevatedButton(content=Text("Confirmar", size=15), style=ButtonStyle(padding={MaterialState.DEFAULT: 18}), on_click=verify_token, width=250, bgcolor=colors.BLUE, color=colors.BLACK)
    confirmation_button_row = Row([confirmation_button], alignment=MainAxisAlignment.CENTER)

    content = Stack([Column([Text("", height=25), Row([IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                                                  on_click=send_login,
                                                                  icon_color=colors.BLACK, icon_size=35),
                                                       Text("                             ")], alignment=MainAxisAlignment.SPACE_AROUND)]),
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
