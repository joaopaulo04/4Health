from flet import *


def go_newevent(e):
    e.page.floating_action_button = None
    e.page.go("/newevent")


def on_change(e):
    index = e.control.selected_index
    if index == 0:
        e.page.floating_action_button = None
        e.page.go("/")
    if index == 1:
        e.page.floating_action_button = FloatingActionButton(
            icon=icons.ADD, on_click=go_newevent, bgcolor=colors.RED_400
        )
        e.page.go("/calendar")
