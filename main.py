from flet import *
from features.Database import DataMethods
from features.FletRouter import *


def main(page: Page):
    DataMethods.initialize()
    DataMethods.add_users("Arthur", "arthur_de_faria@outlook.com", 52716328811, "arthur123", "24/08/2004", "M", 19995128382, "A+", "1.72", "80")
    DataMethods.add_exame(1, "Colonoscopia", "Clínica 4Health", "28/04/2026", "09:00")
    print(DataMethods.show_users())
    print(DataMethods.show_exames(1))
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


if __name__ == '__main__':
    app(target=main)
