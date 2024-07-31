from flet import *
from features.User import User
from features.Exam import Exam
from datetime import *


def editexams(page):

    def send_calendar(e):
        page.go("/calendar")

    def get_user_data():
        id_user = page.client_storage.get("logged_user_id")
        data = User.show_users()
        for user in data:
            if user[0] == id_user:
                return user

    def get_exam_id():
        exame_id = page.client_storage.get("exame_id")
        data = Exam.show_exames(user[0])
        for exam in data:
            if exam[0] == exame_id:
                return exam

    def edit_exam(e):
        mes = str(month)
        if len(mes) == 1:
            mes = "0%s" % mes
        if len(time_textfield.value) == 4:
            time_textfield.value = "0%s" % time_textfield.value
            if time_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[
                1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[2] == ":" and \
                    time_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                    time_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):

                try:
                    datetime.strptime(date_textfield.value, "%d/%m/%Y")
                    Exam.edit_exame(exam[0], name_textfield.value, notes_textfield.value, exam[5],
                                           time_textfield.value)
                    page.navigation_bar = ""
                    print(Exam.show_exames(user[0]))
                    page.go("/calendar")
                except ValueError:
                    page.dialog = AlertDialog(
                        content=Row([Text("Data de nascimento inválida (formato correto: DD/MM/YYYY'", size=18)],
                                    alignment=MainAxisAlignment.CENTER),
                        actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
                    page.dialog.open = True
            else:
                page.dialog = AlertDialog(
                    content=Row([Text("Horário no formato: 'HH:MM'", size=18)], alignment=MainAxisAlignment.CENTER),
                    actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
                page.dialog.open = True
        elif len(time_textfield.value) == 5:
            if time_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[
                1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[2] == ":" and \
                    time_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                    time_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):

                try:
                    datetime.strptime(date_textfield.value, "%d/%m/%Y")
                    Exam.edit_exame(exam[0], name_textfield.value, notes_textfield.value, date_textfield.value,
                                           time_textfield.value)
                    page.navigation_bar = ""
                    print(Exam.show_exames(user[0]))
                    page.go("/calendar")
                except ValueError:
                    page.dialog = AlertDialog(
                        content=Row([Text("Data de nascimento inválida\nFormato correto: DD/MM/YYYY", size=15)],
                                    alignment=MainAxisAlignment.CENTER),
                        actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
                    page.dialog.open = True
            else:
                page.dialog = AlertDialog(
                    content=Row([Text("Horário no formato: 'HH:MM'", size=18)], alignment=MainAxisAlignment.CENTER),
                    actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
                page.dialog.open = True
        else:
            page.dialog = AlertDialog(
                content=Row([Text("Horário no formato: 'HH:MM'", size=18)], alignment=MainAxisAlignment.CENTER),
                actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
            page.dialog.open = True
        page.update()

    def delete_exam(e):
        Exam.remove_exame(exam[0])
        page.navigation_bar = ""
        page.go("/calendar")

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    month = page.client_storage.get("number_month")
    day = page.client_storage.get("dia")
    year = page.client_storage.get("ano")

    user = get_user_data()
    exam = get_exam_id()

    name_text = Text("Nome :", width=300, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    name_row = Row([name_text], alignment=MainAxisAlignment.CENTER)

    if exam is not None:
        name_textfield = TextField(label="Exame de ...", value=exam[2], width=300, bgcolor=colors.WHITE, disabled=False)
        notes_textfield = TextField(label="Ex: Jejum de 12h", width=300, bgcolor=colors.WHITE, value=exam[3],
                                    disabled=False)
        date_textfield = TextField(label="17/10/2001", width=120, bgcolor=colors.WHITE, value=exam[5], disabled=False)
        time_textfield = TextField(label="Ex: 12:30", width=100, bgcolor=colors.WHITE, value=exam[4], disabled=False)

    else:
        name_textfield = TextField(label="Exame de ...", value="", width=300, bgcolor=colors.WHITE, disabled=False)
        notes_textfield = TextField(label="Ex: Jejum de 12h", width=300, bgcolor=colors.WHITE, value="",
                                    disabled=False)
        date_textfield = TextField(label="17/10/2001", width=120, bgcolor=colors.WHITE, value="20/12/2004", disabled=False)
        time_textfield = TextField(label="Ex: 12:30", width=100, bgcolor=colors.WHITE, value="8:00", disabled=False)

    name_textfield_row = Row([name_textfield], alignment=MainAxisAlignment.CENTER)

    notes_text = Text("Anotações :", width=300, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    notes_row = Row([notes_text], alignment=MainAxisAlignment.CENTER)

    notes_textfield_row = Row([notes_textfield], alignment=MainAxisAlignment.CENTER)

    date_text = Text("Data :", width=70, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    date_row = Row([date_text], alignment=MainAxisAlignment.CENTER)

    date_textfield_row = Row([date_textfield], alignment=MainAxisAlignment.CENTER)

    column_date = Column(controls=[date_row, date_textfield_row])

    time_text = Text("Horário :", width=70, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    time_row = Row([time_text], alignment=MainAxisAlignment.CENTER)

    time_textfield_row = Row([time_textfield], alignment=MainAxisAlignment.CENTER)

    column_time = Column(controls=[time_row, time_textfield_row])

    date_time_row = Row([column_time, column_date], alignment=MainAxisAlignment.CENTER)

    save_button = ElevatedButton(content=Text("Editar", size=15, color=colors.WHITE), on_click=edit_exam,
                                 style=ButtonStyle(padding={MaterialState.DEFAULT: 18}, bgcolor=colors.BLACK),
                                 width=200)
    save_button_row = Row([save_button], alignment=MainAxisAlignment.CENTER)

    delete_button = ElevatedButton(content=Text("Excluir", size=15, color=colors.WHITE), on_click=delete_exam, style=ButtonStyle(padding={MaterialState.DEFAULT: 18}, bgcolor=colors.RED_700),
                                   width=200)
    delete_button_row = Row([delete_button], alignment=MainAxisAlignment.CENTER)

    content = Stack([Column(controls=[Text("", height=45),
                                      Row(controls=[Text(width=40), IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                                                               icon_color=colors.BLACK,
                                                                               icon_size=35, on_click=send_calendar),
                                                    Text(width=50),
                                                    Text("Exames",
                                                         size=20,
                                                         weight=FontWeight.W_700)]),
                                      Text(height=26),
                                      name_row,
                                      name_textfield_row,
                                      Text(height=10),
                                      notes_row,
                                      notes_textfield_row,
                                      Text(height=10),
                                      date_time_row,
                                      Text(height=22),
                                      save_button_row,
                                      delete_button_row,
                                      ])])
    return content

