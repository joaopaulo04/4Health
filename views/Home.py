from flet import *
from features.NavBar import on_change
from features.Database import DataMethods
from features.Calendar import Calendar

def home(page):
    def send_edit(e):
        page.go("/editprofile")
    def get_user_data():
        id_user = page.client_storage.get("logged_user_id")
        data = DataMethods.show_users()
        for user in data:
            if user[0] == id_user:
                return user



    user = get_user_data()
    #ola, usuario
    ola = Text("   Olá,", size=25,bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    nome = Text(value=f'  {user[1]}', size=45, bgcolor=colors.WHITE, weight=FontWeight.BOLD)
    list_ola_nome = [ola, nome]
    column_list_ola_nome = Column(spacing=1,controls=list_ola_nome)

    #edit com ola, usuario
    edit_user = IconButton(icon=icons.EDIT, icon_color=colors.BLACK, on_click=send_edit, icon_size=35)
    list_ola_nome_edit = [column_list_ola_nome,edit_user]
    row_nome_edit = Row(spacing=200, controls=list_ola_nome_edit)

    #remedio com nome e horario
    medication_icon = Icon(name=icons.MEDICATION, color=colors.RED, size=30,)
    nome_medication = Text("Tomar Dramin", size=20)
    hora_medication = Text("11:30 AM", size=20)
    medication = [medication_icon, nome_medication, hora_medication]
    info_medication = Column(spacing=15, controls=medication)

    #stackando remedio com o fundo
    stack_medication = Stack(
        [
            Container(width=175, height=125, bgcolor="#D28E79", border_radius=5,opacity=0.5),
            info_medication
        ]
    )

    # calculo imc
    imc_calculo = user[10] / (user[9] * 2)
    imc_numero = round(imc_calculo,1)
    if imc_numero <= 18.5:
        imc = Text("Abaixo do peso", size=20,width=95, weight=FontWeight.BOLD)
    elif imc_numero >= 18.6 and imc_numero <= 24.9:
        imc = Text("Peso ideal", size=20,width=95, weight=FontWeight.BOLD)
    elif imc_numero >= 25 and imc_numero <= 29.9:
        imc = Text("Acima do peso", size=20,width=95, weight=FontWeight.BOLD)
    elif imc_numero >= 30 and imc_numero <= 34.9:
        imc = Text("Obesidade grau 1", size=20,width=105, weight=FontWeight.BOLD)
    elif imc_numero >= 35 and imc_numero <= 39.9:
        imc = Text("Obesidade grau 2", size=20,width=105, weight=FontWeight.BOLD)
    elif imc_numero >= 40:
        imc = Text("Obesidade grau 3", size=20,width=105, weight=FontWeight.BOLD)

    #imc com valor e faixa que se encontra
    imc_icon = Icon(name=icons.MONITOR_HEART_OUTLINED, size=30, color=colors.BLACK)
    nome_imc = Text("IMC", size=20)
    valor_imc = Text(value=imc_numero, size=20)
    esquerda_imc = [imc_icon, nome_imc, valor_imc]
    row_esquerda_imc = Column(spacing=10, controls=esquerda_imc)
    junto_imc = [row_esquerda_imc, imc]
    info_imc = Row(controls=junto_imc, spacing=20)

    # stackando imc com o fundo
    stack_imc = Stack(
        [
            Container(width=175, height=125, bgcolor="#63B147", border_radius=5,opacity=0.5),
            info_imc
        ]
    )
    espaco_remedio_imc = Text("",size=5)
    remedio_imc = [espaco_remedio_imc,stack_medication,espaco_remedio_imc, stack_imc]
    row_medication_imc = Row(spacing=15, controls=remedio_imc)

    #eventos proximos
    eventos_proximos = Text("Eventos proximos:", size=45, weight=FontWeight.BOLD)
    page.navigation_bar = NavigationBar([NavigationDestination(icon=icons.HOUSE, label="Início"),
                                         NavigationDestination(icon=icons.CALENDAR_MONTH, label="Calendário")],
                                        on_change=on_change)

    page.update()
    content = Column([Text("",height=25),row_nome_edit, row_medication_imc, eventos_proximos])
    return content