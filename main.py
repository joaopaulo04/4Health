from flet import *


def main(page: Page):
    page.add(Text("Hello World!"))
    pass


if __name__ == '__main__':
    app(target=main)
