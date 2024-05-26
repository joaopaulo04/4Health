from flet import *
from features.Database import DataMethods
from features.Calendar import *

def newevent(page):
    def events(e):
        if e.control.value == "exames":
            page.go("/exams")
        elif e.control.value == "remedios":
            page.go("/medicines")
        else:
            page.go("/medicalappointment")
        page.update()
    month = page.client_storage.get("month")
    select_day = page.client_storage.get("dia_1")
    page.client_storage.set("dia", select_day)
    year = page.client_storage.get("year")
    page.client_storage.set("ano", year)
    instruction_text = Text("Selecione a opção desejada: ", width=265)
    instruction_row = Row([instruction_text], alignment=MainAxisAlignment.CENTER)
    options = RadioGroup(content=Row(controls=[
        Radio(value="exames", label="Exames", fill_color={
            MaterialState.HOVERED: colors.RED,
            MaterialState.DEFAULT: colors.RED}),
        Radio(value="consulta", label="Consultas", fill_color={
            MaterialState.HOVERED: colors.BLUE,
            MaterialState.DEFAULT: colors.BLUE}),
        Radio(value="remedios", label="Remédios", fill_color={
            MaterialState.HOVERED: colors.GREEN,
            MaterialState.DEFAULT: colors.GREEN})], alignment=MainAxisAlignment.CENTER), on_change=events)
    content = Stack([Column(controls=[Text("", height=45),
                                      Row(controls=[Text("Calendário",
                                                         size=20,
                                                         weight=FontWeight.W_700)],
                                          alignment=MainAxisAlignment.CENTER),
                                      Row(controls=[Text(f'{select_day}° de {month} de {year}', size=25, weight=FontWeight.BOLD)],
                                          alignment=MainAxisAlignment.CENTER),
                                      instruction_row,
                                      options
                                      ])])
    return content
