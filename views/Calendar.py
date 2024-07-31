from flet import *
from features.Calendar import Calendar


def calendar(page):
    cal = Calendar(page)
    main_layer = Container(content=Column([Row([Text("Calendário", size=20, weight=FontWeight.W_700)], alignment=MainAxisAlignment.CENTER), Text(height=10), Row([cal.build()], alignment=MainAxisAlignment.CENTER), Row([cal.output], alignment=MainAxisAlignment.CENTER)]), padding=padding.only(top=50))
    content = Stack([main_layer])
    return content