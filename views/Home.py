from flet import *
from features.NavBar import on_change


def home(page):
    page.navigation_bar = NavigationBar([NavigationDestination(icon=icons.HOUSE, label="Início"),
                                         NavigationDestination(icon=icons.CALENDAR_MONTH, label="Calendário")],
                                        on_change=on_change)
    page.update()
    content = Text("Home")
    return content