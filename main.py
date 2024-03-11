from flet import *


def main(page: Page):
    page.add(Text("Hello World!"))
    page.add(Text("Size 10", size=10))
    page.title = '4Health'
    page.theme_mode = ThemeMode.LIGHT
    page.window_width = 30
    page.window_height = 100
    page.update()


if __name__ == '__main__':
    app(target=main)
