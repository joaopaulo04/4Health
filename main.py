from flet import *
from features.Database import DataMethods
from features.User import User
from features.Appointment import Appointment
from features.Medicine import Medicine
from features.Exam import Exam
from features.FletRouter import *


def main(page: Page):
    DataMethods.initialize()
    print(User.show_users())
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


app(target=main)
