from flet import *
from features.Database import DataMethods

def editprofile(page):
    def get_user_data(e):
        id_user = page.client_storage.get("logged_user_id")
    content = Stack([Container(height=110,
                               bgcolor=colors.LIGHT_BLUE_ACCENT_200,
                               content=Column([Text("", height=30), Row(controls=[Text("Editar perfil",
                                                          size=20,
                                                          weight=FontWeight.W_700)], alignment=MainAxisAlignment.CENTER)],
                                              alignment=MainAxisAlignment.CENTER))])
    return content
