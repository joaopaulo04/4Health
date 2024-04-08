from flet import *
from features.Database import DataMethods

def main(page: Page):
    DataMethods.initialize()
    page.add(Text("Hello World!"))
    page.title = '4Health'
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False
    page.update()

if __name__ == '__main__':
    app(target=main)
