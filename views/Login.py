from flet import *
from features.Database import DataMethods

def login(page):
    #content = Text('Login')
    content = ElevatedButton('Mudar para home', on_click= lambda _: page.go('/'))
    return content
