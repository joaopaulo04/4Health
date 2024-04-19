from flet import *
from views.Home import home
from views.Login import login
from views.SignIn import signin
from views.ForgetPassword import forgetpassword
from views.UpdatePassword import updatepassword
from views.Calendar import calendar
from views.EditProfile import editprofile
from views.NewEvent import newevent


class Router:
    def __init__(self, page):
        self.page = page
        self.routes = {
            "/login": login(page)
        }
        self.body = Container(content=self.routes['/login'])

    def route_change(self, route):
        if route.route in ('/login', '/signin', '/forgetpassword', '/updatepassword'):
            self.routes = {
                "/login": login(self.page),
                "/signin": signin(self.page),
                "/forgetpassword": forgetpassword(self.page),
                "/updatepassword": updatepassword(self.page),
            }
        else:
            self.routes = {
                "/": home(self.page),
                "/calendar": calendar(self.page),
                "/editprofile": editprofile(self.page),
                "/newevent": newevent(self.page)
            }
        self.body.content = self.routes[route.route]
        self.body.update()