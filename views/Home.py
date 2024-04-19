from flet import *
from features.NavBar import on_change


def home(page):
    def send_edit(e):
        page.go("/editprofile")

    page.navigation_bar = NavigationBar([NavigationDestination(icon=icons.HOUSE, label="Início"),
                                         NavigationDestination(icon=icons.CALENDAR_MONTH, label="Calendário")],
                                        on_change=on_change)
    page.update()
    content = Row([IconButton(icon=icons.EDIT, icon_color=colors.BLACK, on_click=send_edit, icon_size=35)])
    return content