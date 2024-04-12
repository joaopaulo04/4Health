from flet import *
from features.Database import DataMethods
from features.FletRouter import Router


def main(page: Page):
    # Main
    DataMethods.initialize()
    myrouter = Router(page)
    page.padding = 0
    page.on_route_change = myrouter.route_change
    page.add(myrouter.body)
    page.title = '4Health'
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 430
    page.window_height = 830
    page.window_resizable = False
    page.update()


if __name__ == '__main__':
    app(target=main)