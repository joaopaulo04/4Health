from flet import *
from features.NavBar import on_change
from features.Database import DataMethods


def editprofile(page):
    def get_user_data():
        id_user = page.client_storage.get("logged_user_id")
        data = DataMethods.show_users()
        for user in data:
            if user[0] == id_user:
                return user

    def edit_profile(e):
        DataMethods.edit_users(user[0], user[4], number_textfield.value, height_textfield.value, weight_textfield.value, blood_type_textfield.value)
        print(DataMethods.show_users())
        page.go('/')

    def delete_user(e):
        DataMethods.remove_users(user[0])
        page.navigation_bar = ""
        page.go('/login')

    user = get_user_data()

    name_textfield = TextField(label="Nome", value=user[1], disabled=True)
    name_row = Row([name_textfield], alignment=MainAxisAlignment.CENTER)

    email_textfield = TextField(label="Email", value=user[2], disabled=True)
    email_row = Row([email_textfield], alignment=MainAxisAlignment.CENTER)

    number_textfield = TextField(label="Número", value=user[7], keyboard_type=KeyboardType.NUMBER)
    number_row = Row([number_textfield], alignment=MainAxisAlignment.CENTER)

    blood_type_textfield = TextField(label="Tipo sanguíneo", value=user[8])
    blood_type_row = Row([blood_type_textfield], alignment=MainAxisAlignment.CENTER)

    height_textfield = TextField(label="Altura", value=user[9])
    height_row = Row([height_textfield], alignment=MainAxisAlignment.CENTER)

    weight_textfield = TextField(label="Peso", value=user[10])
    weight_row = Row([weight_textfield], alignment=MainAxisAlignment.CENTER)

    CPF_textfield = TextField(label="CPF", value=user[3], disabled=True)
    CPF_row = Row([CPF_textfield], alignment=MainAxisAlignment.CENTER)

    born_date_textfield = TextField(label="Data de nascimento", value=user[5], disabled=True)
    born_date_row = Row([born_date_textfield], alignment=MainAxisAlignment.CENTER)

    sex_textfield = TextField(label="Sexo", value=user[6], disabled=True)
    sex_row = Row([sex_textfield], alignment=MainAxisAlignment.CENTER)

    update_user_button = FilledButton(text="Atualizar dados", width=250, style=ButtonStyle(color=colors.WHITE, bgcolor=colors.BLUE_600), on_click=edit_profile)
    update_user_row = Row([update_user_button], alignment=MainAxisAlignment.CENTER)

    delete_user_button = FilledButton(text="Deletar conta", width=250, style=ButtonStyle(color=colors.WHITE, bgcolor=colors.RED), on_click=delete_user)
    delete_user_row = Row([delete_user_button], alignment=MainAxisAlignment.CENTER)

    content = Stack([Container(height=110,
                               bgcolor=colors.LIGHT_BLUE_ACCENT_200,
                               content=Column([Text("", height=30), Row(controls=[Text("Editar perfil",
                                                          size=20,
                                                          weight=FontWeight.W_700)], alignment=MainAxisAlignment.CENTER)],
                                              alignment=MainAxisAlignment.CENTER)),
                     Column([Text(height=120), Column([name_row,
                             email_row,
                             number_row,
                             blood_type_row,
                             height_row,
                             weight_row,
                             CPF_row,
                             born_date_row,
                             sex_row,
                             Text(height=5),
                             update_user_row,
                             Text(height=1),
                             delete_user_row], scroll=ScrollMode.ALWAYS, height=500)
                             ])])
    return content
