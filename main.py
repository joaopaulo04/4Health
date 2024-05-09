from flet import *
from features.Database import DataMethods
from features.FletRouter import Router


def main(page: Page):
    # Main
    DataMethods.initialize()
    DataMethods.add_users("Arthur", "arthur_de_faria@outlook.com", 52716328811, "arthur123", "24/08/2004", "M", 19995128382, "A+", "1.72", "80")
    # DataMethods.add_consulta(1, "Consulta de rotina", "Doutor Ângelo", "14:30", "23/04/2024")
    # DataMethods.add_consulta(1, "Cardiologista", "Doutor Carlos", "15:15", "23/04/2024")
    # DataMethods.add_exame(1, "Exame de sangue", "Laboratório Biogen", "27/04/2024", "14:45")
    # DataMethods.add_exame(1, "Colonoscopia", "Clínica 4Health", "28/04/2024", "09:00")
    DataMethods.add_remedio(1, "Dipirona", "", "06:00", "08:00")
    DataMethods.add_remedio(1, "Buscopan", "", "12:00", "05:00")
    myrouter = Router(page)
    print(DataMethods.show_users())
    print(DataMethods.show_consultas(1))
    print(DataMethods.show_exames(1))
    print(DataMethods.show_remedios(1))
    page.padding = 0
    page.on_route_change = myrouter.route_change
    page.add(myrouter.body)
    page.title = 'ForHealth'
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 430
    page.window_height = 830
    page.window_resizable = False
    page.update()


if __name__ == '__main__':
    app(target=main)
