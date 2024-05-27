from flet import *
from features.Database import DataMethods


def medicines(page):
    def send_newevent(e):
        page.go("/newevent")

    def get_user_data():
        id_user = page.client_storage.get("logged_user_id")
        data = DataMethods.show_users()
        for user in data:
            if user[0] == id_user:
                return user

    def add_medicine(e):
        if len(time_textfield.value) == 4:
            time_textfield.value = "0%s" % time_textfield.value
            if time_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[
                1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[2] == ":" and \
                    time_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                    time_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                if len(first_portion_textfield.value) == 4:
                    first_portion_textfield.value = "0%s" % first_portion_textfield.value
                    if first_portion_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and first_portion_textfield.value[1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and first_portion_textfield.value[2] == ":" and \
                            first_portion_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                            first_portion_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        DataMethods.add_remedio(user[0], name_textfield.value, notes_textfield.value, time_textfield.value,
                                                first_portion_textfield.value)
                        page.navigation_bar = ""
                        page.go("/calendar")
                elif len(first_portion_textfield.value) == 5:
                    if first_portion_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                            first_portion_textfield.value[
                                1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and first_portion_textfield.value[
                        2] == ":" and \
                            first_portion_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                            first_portion_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        DataMethods.add_remedio(user[0], name_textfield.value, notes_textfield.value,
                                                time_textfield.value,
                                                first_portion_textfield.value)
                        page.navigation_bar = ""
                        page.go("/calendar")
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
        elif len(time_textfield.value) == 5:
            if time_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[
                1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and time_textfield.value[2] == ":" and \
                    time_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                    time_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                if len(first_portion_textfield.value) == 4:
                    first_portion_textfield.value = "0%s" % first_portion_textfield.value
                    if first_portion_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and first_portion_textfield.value[1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and first_portion_textfield.value[2] == ":" and \
                            first_portion_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                            first_portion_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        DataMethods.add_remedio(user[0], name_textfield.value, notes_textfield.value, time_textfield.value,
                                                first_portion_textfield.value)
                        page.navigation_bar = ""
                        page.go("/calendar")
                elif len(first_portion_textfield.value) == 5:
                    if first_portion_textfield.value[0] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                            first_portion_textfield.value[
                                1] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and first_portion_textfield.value[
                        2] == ":" and \
                            first_portion_textfield.value[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") and \
                            first_portion_textfield.value[4] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        DataMethods.add_remedio(user[0], name_textfield.value, notes_textfield.value,
                                                time_textfield.value,
                                                first_portion_textfield.value)
                        page.navigation_bar = ""
                        page.go("/calendar")
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
        else:
            page.dialog = AlertDialog(
                content=Row([Text("Horário no formato: 'HH:MM'", size=18)], alignment=MainAxisAlignment.CENTER),
                actions=[Row([TextButton("OK", on_click=close_dialog)], alignment=MainAxisAlignment.CENTER)])
            page.dialog.open = True
        page.update()

    def close_dialog(e):
        page.dialog.open = False
        page.update()

    user = get_user_data()

    name_text = Text("Nome :", width=300, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    name_row = Row([name_text], alignment=MainAxisAlignment.CENTER)

    name_textfield = TextField(label="Remédio ...", width=300, bgcolor=colors.WHITE, filled=True)
    name_textfield_row = Row([name_textfield], alignment=MainAxisAlignment.CENTER)

    notes_text = Text("Anotações :", width=300, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    notes_row = Row([notes_text], alignment=MainAxisAlignment.CENTER)

    notes_textfield = TextField(label="Ex: Tomar remédio após o almoço", width=300, bgcolor=colors.WHITE, filled=True)
    notes_textfield_row = Row([notes_textfield], alignment=MainAxisAlignment.CENTER)

    first_portion = Text("Primeira dose :", width=120, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    first_portion_row = Row([first_portion], alignment=MainAxisAlignment.CENTER)

    first_portion_textfield = TextField(label="Ex: 12:00", width=120, bgcolor=colors.WHITE, filled=True)
    first_portion_textfield_row = Row([first_portion_textfield], alignment=MainAxisAlignment.CENTER)

    column_first_portion = Column(controls=[first_portion_row, first_portion_textfield_row])

    time_text = Text("Tomar remédio a cada :", width=165, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    time_row = Row([time_text], alignment=MainAxisAlignment.CENTER)

    time_textfield = TextField(label="Ex: 08:00", width=165, bgcolor=colors.WHITE, filled=True)
    time_textfield_row = Row([time_textfield], alignment=MainAxisAlignment.CENTER)

    column_time = Column(controls=[time_row, time_textfield_row])

    hour_time_row = Row([column_first_portion, column_time], alignment=MainAxisAlignment.CENTER)

    save_button = ElevatedButton(content=Text("Salvar", size=15, color=colors.WHITE),
                                 style=ButtonStyle(padding={MaterialState.DEFAULT: 18}, bgcolor=colors.BLACK),
                                 width=200, on_click=add_medicine)
    save_button_row = Row([save_button], alignment=MainAxisAlignment.CENTER)

    delete_button = ElevatedButton(content=Text("Excluir", size=15, color=colors.WHITE), on_click=send_newevent, style=ButtonStyle(padding={MaterialState.DEFAULT: 18}, bgcolor=colors.RED_700), width=200)
    delete_button_row = Row([delete_button], alignment=MainAxisAlignment.CENTER)

    content = Stack([Column(controls=[Text("", height=45),
                                      Row(controls=[Text(width=40), IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED,
                                                                               icon_color=colors.BLACK,
                                                                               on_click=send_newevent,
                                                                               icon_size=35),
                                                    Text(width=40),
                                                    Text("Remédios",
                                                         size=20,
                                                         weight=FontWeight.W_700)]),
                                      Text(height=26),
                                      name_row,
                                      name_textfield_row,
                                      Text(height=10),
                                      notes_row,
                                      notes_textfield_row,
                                      Text(height=10),
                                      hour_time_row,
                                      Text(height=22),
                                      save_button_row,
                                      delete_button_row
                                      ])])
    return content