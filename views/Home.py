from flet import *
from features.NavBar import on_change
from features.User import User
from features.Medicine import Medicine
from features.Appointment import Appointment
from features.Exam import Exam
from datetime import *
import operator
from features.Calendar import Calendar

def home(page):
    def send_edit(e):
        page.go("/editprofile")

    def get_user_data():
        id_user = page.client_storage.get("logged_user_id")
        data = User.show_users()
        for user in data:
            if user[0] == id_user:
                return user

    def send_editmedicines(e, medicines_id):
        page.client_storage.set("remedio_id", medicines_id)
        page.go("/editmedicines")

    def send_editmeda(e, meda_id):
        page.client_storage.set("consulta_id", meda_id)
        page.go("/editmeda")

    def send_editexams(self, e, exame_id):
        page.client_storage.set("exame_id", exame_id)
        page.go("/editexams")

    def sort_meds(dates):
        dates.sort(key=lambda x: x[5])
        return dates

    def sort_dates(dates):
        dates.sort(key=operator.itemgetter(5, 4), reverse=True)
        dates = sorted(dates, key=lambda x: to_datetime(x[5] + ' ' + x[4]))
        return dates

    def to_datetime(date_time_str):
        date_str, time_str = date_time_str.split(' ', 1)
        return tuple(map(int, date_str.split('/'))) + tuple(map(int, time_str.split(':')))

    def verify_output():
        id_user = page.client_storage.get("logged_user_id")
        consultas = Appointment.show_consultas(id_user)
        consultas = sort_dates(consultas)
        exames = Exam.show_exames(id_user)
        exames = sort_dates(exames)
        remedios = Medicine.show_remedios(id_user)
        remedios = sort_meds(remedios)

        if not consultas and not exames and not remedios:
            return Column([Text(height=10),
                           Row([Text("Nenhum evento agendado até o momento!", size=15, weight=FontWeight.BOLD)],
                               alignment=MainAxisAlignment.CENTER)])
        else:
            blocks = Column([], scroll=ScrollMode.ALWAYS, width=355)
            output = Container(width=370, height=375, padding=padding.all(15), content=blocks)

            for remedio in remedios:
                hora_remedio = datetime.strptime(remedio[5], "%H:%M").time()
                if hora_remedio < datetime.now().time():
                    plus_hour = int(remedio[4][0:2])
                    past_hour = int(remedio[5][0:2])
                    future_hour = past_hour + plus_hour
                    if future_hour >= 24:
                        future_hour = future_hour - 24
                    future_hour = str(future_hour).zfill(2)
                    plus_minutes = int(remedio[4][3:5])
                    past_minutes = int(remedio[5][3:5])
                    future_minutes = past_minutes + plus_minutes
                    if future_minutes >= 60:
                        future_minutes = future_minutes - 60
                    future_minutes = str(future_minutes).zfill(2)
                    teste = future_hour + ":" + future_minutes
                    Medicine.edit_remedio(remedio[0], remedio[2], remedio[3], remedio[4], teste)
                remedio_block = Container(border_radius=15,
                                           height=60,
                                           width=355,
                                           bgcolor=colors.GREEN,
                                           padding=padding.only(top=5, left=5, right=5),
                                           content=Stack([
                                               Container(
                                                   Text(
                                                       f"{remedio[5][0]}" + f"{remedio[5][1]}" + f"{remedio[5][2]}" + f"{remedio[5][3]}" + f"{remedio[5][4]}",
                                                       size=32,
                                                       weight=FontWeight.W_900,
                                                       color=colors.WHITE),
                                                   padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                   border_radius=10,
                                                   bgcolor=colors.GREEN_300,
                                                   width=92,
                                                   height=48
                                               ),
                                               Row([
                                                   Text("              "),
                                                   Text(f"{remedio[2]}",
                                                        size=20,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_600),
                                                   Text(),
                                                   Text()],
                                                   height=45,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN),
                                               Column([Text(height=15), Row([
                                                   Text("              "),
                                                   Text(f"{remedio[3]}",
                                                        size=15,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_400),
                                                   Text(),
                                                   Text()],
                                                   height=32,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                      height=48, ),
                                           ]), on_click=lambda e, id=remedio[0]: send_editmedicines(e, id))
                blocks.controls.append(remedio_block)
            for consulta in consultas:
                consulta_block = Container(border_radius=15,
                                           height=60,
                                           width=355,
                                           bgcolor=colors.BLUE,
                                           padding=padding.only(top=5, left=5, right=5),
                                           content=Stack([
                                               Container(
                                                   Text(
                                                       f"{consulta[5][0]}" + f"{consulta[5][1]}" + f"{consulta[5][2]}" + f"{consulta[5][3]}" + f"{consulta[5][4]}",
                                                       size=32,
                                                       weight=FontWeight.W_900,
                                                       color=colors.WHITE),
                                                   padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                   border_radius=10,
                                                   bgcolor=colors.BLUE_300,
                                                   width=92,
                                                   height=48
                                               ),
                                               Row([
                                                   Text("              "),
                                                   Text(f"{consulta[2]}",
                                                        size=18,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_600),
                                                   Text(),
                                                   Text()],
                                                   height=45,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN),
                                               Column([Text(height=15), Row([
                                                   Text("              "),
                                                   Text(f" - {consulta[3]}",
                                                        size=15,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_400),
                                                   Text(),
                                                   Text()],
                                                   height=32,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                      height=48, ),
                                               Row([Text("  "),
                                                    Text(f"{consulta[4]}",
                                                         size=11,
                                                         color=colors.WHITE,
                                                         weight=FontWeight.W_600),
                                                    Text("           ")
                                                    ], alignment=MainAxisAlignment.SPACE_BETWEEN),

                                           ]), on_click=lambda e, id=consulta[0]: send_editmeda(e, id))
                blocks.controls.append(consulta_block)
            for exame in exames:
                exame_block = Container(border_radius=15,
                                        height=60,
                                        width=355,
                                        bgcolor=colors.RED,
                                        padding=padding.only(top=5, left=5, right=5),
                                        content=Stack([
                                            Container(
                                                Text(
                                                    f"{exame[5][0]}" + f"{exame[5][1]}" + f"{exame[5][2]}" + f"{exame[5][3]}" + f"{exame[5][4]}",
                                                    size=32,
                                                    weight=FontWeight.W_900,
                                                    color=colors.WHITE),
                                                padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                border_radius=10,
                                                bgcolor=colors.RED_300,
                                                width=92,
                                                height=48
                                            ),
                                            Row([
                                                Text("              "),
                                                Text(f"{exame[2]}",
                                                     size=18,
                                                     color=colors.WHITE,
                                                     weight=FontWeight.W_600),
                                                Text(),
                                                Text()],
                                                height=44,
                                                alignment=MainAxisAlignment.SPACE_BETWEEN),
                                            Column([Text(height=15), Row([
                                                Text("              "),
                                                Text(f" - {exame[3]}",
                                                     size=15,
                                                     color=colors.WHITE,
                                                     weight=FontWeight.W_400),
                                                Text(),
                                                Text()],
                                                height=32,
                                                alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                   height=48, ),
                                            Row([Text(""),
                                                 Text(f"{exame[4]}",
                                                      size=11,
                                                      color=colors.WHITE,
                                                      weight=FontWeight.W_600),
                                                 Text("           ")
                                                 ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                                        ]), on_click=lambda e, id=exame[0]: send_editexams(e, id))
                blocks.controls.append(exame_block)
            return output



    user = get_user_data()
    #ola, usuario
    ola = Text("   Olá,", size=25,bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    nome = Text(value=f'  {user[1]}', size=30, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    list_ola_nome = [ola, nome]
    column_list_ola_nome = Column(spacing=1,controls=list_ola_nome)

    #edit com ola, usuario
    edit_user = IconButton(icon=icons.EDIT, icon_color=colors.BLACK, on_click=send_edit, icon_size=35)
    list_ola_nome_edit = [column_list_ola_nome,edit_user]
    row_nome_edit = Row(spacing=220, controls=list_ola_nome_edit)

    #remedio com nome e horario
    remedios = Medicine.show_remedios(user[0])
    remedios = sort_meds(remedios)
    medication_icon = Icon(name=icons.MEDICATION, color=colors.RED, size=30)
    nome_medication = Text(f'   Sem remédios', size=20)
    hora_medication = Text(f'          -- : --', size=20,weight=FontWeight.BOLD)

    if remedios != []:
        remedio = remedios[0]
        nome_medication = Text(f"   {remedio[2]}", size=20,width=170)
        hora_medication = Text(f"           {remedio[5]}", size=20,weight=FontWeight.BOLD)

    medication_icon_container = Container(content=Row([medication_icon]))
    medication_icon_container.padding = padding.only(left=15, top=5)

    medication = [medication_icon_container, nome_medication, hora_medication]
    info_medication = Column(spacing=15, controls=medication)

    #stackando remedio com o fundo
    fundo_vermelho = Container(width=160, height=125, bgcolor="#D28E79", border_radius=10,opacity=0.5)
    stack_medication = Stack(
        [
            fundo_vermelho,
            info_medication
        ]
    )

    # calculo imc
    imc_calculo = user[10] / (user[9] * 2)
    imc_numero = round(imc_calculo,1)
    if imc_numero <= 18.5:
        imc = Text("Abaixo do peso", size=20,width=95, weight=FontWeight.BOLD)
    elif imc_numero >= 18.6 and imc_numero <= 24.9:
        imc = Text("Peso ideal", size=20,width=100, weight=FontWeight.BOLD)
    elif imc_numero >= 25 and imc_numero <= 29.9:
        imc = Text("Acima do peso", size=20,width=95, weight=FontWeight.BOLD)
    elif imc_numero >= 30 and imc_numero <= 34.9:
        imc = Text("Obesidade 1º Grau", size=19,width=105, weight=FontWeight.BOLD)
    elif imc_numero >= 35 and imc_numero <= 39.9:
        imc = Text("Obesidade 2º Grau", size=19,width=105, weight=FontWeight.BOLD)
    elif imc_numero >= 40:
        imc = Text("Obesidade 3º Grau", size=19,width=105, weight=FontWeight.BOLD)

    imc_valor = Container(content=Row([imc]))
    imc_valor.padding = padding.only(top=35)

    #imc com valor e faixa que se encontra
    imc_icon = Icon(name=icons.MONITOR_HEART_OUTLINED, size=30, color=colors.BLACK)
    imc_icon_container = Container(content=Row([imc_icon]))
    imc_icon_container.padding = padding.only(top=5,left=15)
    nome_imc = Text("  IMC", size=20, weight=FontWeight.BOLD)
    valor_imc = Text(value=f'  {imc_numero}', size=20)
    esquerda_imc = [imc_icon_container, nome_imc, valor_imc]
    row_esquerda_imc = Column(spacing=10, controls=esquerda_imc)
    junto_imc = [row_esquerda_imc, imc_valor]
    info_imc = Row(controls=junto_imc, spacing=10)

    # stackando imc com o fundo
    fundo_verde = Container(width=160, height=125, bgcolor="#63B147", border_radius=10, opacity=0.5)
    stack_imc = Stack(
        [
            fundo_verde,
            info_imc
        ]
    )
    #espaco_remedio_imc = Text("",size=5)
    segundo_remedio_imc = Text("",width=26)
    primeiro_remedio_imc = Text("", width=19)

    remedio_imc = [primeiro_remedio_imc,stack_medication,segundo_remedio_imc ,stack_imc]
    row_medication_imc = Row(spacing=0, controls=remedio_imc)

    #eventos proximos
    eventos_proximos = Text("   Eventos proximos:", size=20, weight=FontWeight.BOLD)
    page.navigation_bar = NavigationBar([NavigationDestination(icon=icons.HOUSE, label="Início"),
                                         NavigationDestination(icon=icons.CALENDAR_MONTH, label="Calendário")],
                                        on_change=on_change)

    output = verify_output()
    centralizar_output = Row([output],alignment=MainAxisAlignment.CENTER)

    page.update()
    content = Column([Text("",height=25),row_nome_edit, row_medication_imc, eventos_proximos, centralizar_output])
    return content