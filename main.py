from flet import *
from features.Database import DataMethods
from features.FletRouter import *


def main(page: Page):
    DataMethods.initialize()
    # DataMethods.add_users('Arthur', 'a', 52716328811, 'a', '24/08/2004', 'M', 19995128382, 'A+', 1.72, 80.0)
    # DataMethods.add_exame(1, 'Exame de Urina', '', '31/05/2024', '09:30')
    # DataMethods.add_exame(1, 'Exame de Sangue', '', '01/06/2024', '10:30')
    print(DataMethods.show_users())
    print(DataMethods.show_exames(1))
    print(DataMethods.show_remedios(1))
    myrouter = Router(page)
    page.padding = 0
    page.on_route_change = myrouter.route_change
    page.add(myrouter.body)
    page.title = 'ForHealth'
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 430
    page.window_height = 830
    page.window_resizable = False
    page.update()


app(target=main)
