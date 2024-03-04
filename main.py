from flet import *


def main(page: Page):
    page.add(Text("Hello World!"))
    page.title = '4Health'
    pass


if __name__ == '__main__':
    app(target=main)
