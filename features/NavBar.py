from flet import *


def on_change(e):
    index = e.control.selected_index
    if index == 0:
        e.page.go("/")
    if index == 1:
        e.page.go("/calendar")
