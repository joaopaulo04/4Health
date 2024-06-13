from dateutil import relativedelta
from flet import *
from calendar import *
from datetime import *
from features.Database import DataMethods
import operator


BORDER_COLOR = colors.BLUE
ICON_COLOR = colors.GREY
TEXT_COLOR = colors.BLACK
CURRENT_DAY_COLOR = colors.BLUE_100
SELECTED_DAY_COLOR = colors.BLUE_50


class Calendar(Container):
    def __init__(self, page):
        super().__init__()

        self.page = page
        today = datetime.today()
        self.current_month = today.month
        self.current_day = today.day
        self.current_year = today.year

        self.selected_day = None

        self.calendar_container = Container(width=355,
                                            height=343,
                                            padding=padding.all(2),
                                            border=border.all(2, BORDER_COLOR),
                                            border_radius=border_radius.all(10),
                                            alignment=alignment.bottom_center)
        self.output = None

        self.output = self.verify_output()

    def send_editmedicines(self, e, medicines_id):
        self.page.client_storage.set("remedio_id", medicines_id)
        self.page.go("/editmedicines")

    def send_editmeda(self, e, meda_id):
        self.page.client_storage.set("consulta_id", meda_id)
        self.page.go("/editmeda")

    def send_editexams(self, e, exame_id):
        self.page.client_storage.set("exame_id", exame_id)
        self.page.go("/editexams")
    @staticmethod
    def to_datetime(date_time_str):
        date_str, time_str = date_time_str.split(' ', 1)
        return tuple(map(int, date_str.split('/'))) + tuple(map(int, time_str.split(':')))


    def sort_dates(self, dates):
        dates.sort(key=operator.itemgetter(5, 4), reverse=True)
        dates = sorted(dates, key=lambda x: self.to_datetime(x[5] + ' ' + x[4]))
        return dates

    @staticmethod
    def sort_meds(dates):
        dates.sort(key=lambda x: x[5])
        return dates

    def verify_output(self):
        id_user = self.page.client_storage.get("logged_user_id")
        consultas = DataMethods.show_consultas(id_user)
        consultas = self.sort_dates(consultas)
        exames = DataMethods.show_exames(id_user)
        exames = self.sort_dates(exames)
        remedios = DataMethods.show_remedios(id_user)
        remedios = self.sort_meds(remedios)
        # if self.selected_day is None:
        #     return Text("Teste")
        if not consultas and not exames and not remedios:
            return Column([Text(height=10),
                           Row([Text("Nenhum evento agendado até o momento!", size=15, weight=FontWeight.BOLD)],
                               alignment=MainAxisAlignment.CENTER)])
        else:
            blocks = Column([], scroll=ScrollMode.ALWAYS, width=355)
            output = Container(width=370, height=235, padding=padding.all(15), content=blocks)

            for remedio in remedios:
                hora_remedio = datetime.strptime(remedio[5], "%H:%M").time()
                if hora_remedio < datetime.now().time():
                    plus_hour = int(remedio[4][0:2])
                    past_hour = int(remedio[5][0:2])
                    future_hour = past_hour + plus_hour
                    if future_hour >= 24:
                        future_hour = future_hour - 24
                    future_hour = str(future_hour).zfill(2)
                    plus_minutes = int(remedio[4][3:5])
                    past_minutes = int(remedio[5][3:5])
                    future_minutes = past_minutes + plus_minutes
                    if future_minutes >= 60:
                        future_minutes = future_minutes - 60
                    future_minutes = str(future_minutes).zfill(2)
                    teste = future_hour + ":" + future_minutes
                    DataMethods.edit_remedio(remedio[0], remedio[2], remedio[3], remedio[4], teste)
                remedio_block = Container(border_radius=15,
                                           height=60,
                                           width=355,
                                           bgcolor=colors.GREEN,
                                           padding=padding.only(top=5, left=5, right=5),
                                           content=Stack([
                                               Container(
                                                   Text(
                                                       f"{remedio[5][0]}" + f"{remedio[5][1]}" + f"{remedio[5][2]}" + f"{remedio[5][3]}" + f"{remedio[5][4]}",
                                                       size=32,
                                                       weight=FontWeight.W_900,
                                                       color=colors.WHITE),
                                                   padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                   border_radius=10,
                                                   bgcolor=colors.GREEN_300,
                                                   width=92,
                                                   height=48
                                               ),
                                               Row([
                                                   Text("              "),
                                                   Text(f"{remedio[2]}",
                                                        size=20,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_600),
                                                   Text(),
                                                   Text()],
                                                   height=45,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN),
                                               Column([Text(height=15), Row([
                                                   Text("              "),
                                                   Text(f"{remedio[3]}",
                                                        size=15,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_400),
                                                   Text(),
                                                   Text()],
                                                   height=32,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                      height=48, ),
                                           ]), on_click=lambda e, id=remedio[0]: self.send_editmedicines(e, id))
                blocks.controls.append(remedio_block)
            for consulta in consultas:
                consulta_block = Container(border_radius=15,
                                           height=60,
                                           width=355,
                                           bgcolor=colors.BLUE,
                                           padding=padding.only(top=5, left=5, right=5),
                                           content=Stack([
                                               Container(
                                                   Text(
                                                       f"{consulta[5][0]}" + f"{consulta[5][1]}" + f"{consulta[5][2]}" + f"{consulta[5][3]}" + f"{consulta[5][4]}",
                                                       size=32,
                                                       weight=FontWeight.W_900,
                                                       color=colors.WHITE),
                                                   padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                   border_radius=10,
                                                   bgcolor=colors.BLUE_300,
                                                   width=92,
                                                   height=48
                                               ),
                                               Row([
                                                   Text("              "),
                                                   Text(f"{consulta[2]}",
                                                        size=18,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_600),
                                                   Text(),
                                                   Text()],
                                                   height=45,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN),
                                               Column([Text(height=15), Row([
                                                   Text("              "),
                                                   Text(f" - {consulta[3]}",
                                                        size=15,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_400),
                                                   Text(),
                                                   Text()],
                                                   height=32,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                      height=48, ),
                                               Row([Text("  "),
                                                    Text(f"{consulta[4]}",
                                                         size=11,
                                                         color=colors.WHITE,
                                                         weight=FontWeight.W_600),
                                                    Text("           ")
                                                    ], alignment=MainAxisAlignment.SPACE_BETWEEN),

                                           ]), on_click=lambda e, id=consulta[0]: self.send_editmeda(e, id))
                blocks.controls.append(consulta_block)
            for exame in exames:
                exame_block = Container(border_radius=15,
                                        height=60,
                                        width=355,
                                        bgcolor=colors.RED,
                                        padding=padding.only(top=5, left=5, right=5),
                                        content=Stack([
                                            Container(
                                                Text(
                                                    f"{exame[5][0]}" + f"{exame[5][1]}" + f"{exame[5][2]}" + f"{exame[5][3]}" + f"{exame[5][4]}",
                                                    size=32,
                                                    weight=FontWeight.W_900,
                                                    color=colors.WHITE),
                                                padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                border_radius=10,
                                                bgcolor=colors.RED_300,
                                                width=92,
                                                height=48
                                            ),
                                            Row([
                                                Text("              "),
                                                Text(f"{exame[2]}",
                                                     size=18,
                                                     color=colors.WHITE,
                                                     weight=FontWeight.W_600),
                                                Text(),
                                                Text()],
                                                height=44,
                                                alignment=MainAxisAlignment.SPACE_BETWEEN),
                                            Column([Text(height=15), Row([
                                                Text("              "),
                                                Text(f" - {exame[3]}",
                                                     size=15,
                                                     color=colors.WHITE,
                                                     weight=FontWeight.W_400),
                                                Text(),
                                                Text()],
                                                height=32,
                                                alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                   height=48, ),
                                            Row([Text(""),
                                                 Text(f"{exame[4]}",
                                                      size=11,
                                                      color=colors.WHITE,
                                                      weight=FontWeight.W_600),
                                                 Text("           ")
                                                 ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                                        ]), on_click=lambda e, id=exame[0]: self.send_editexams(e, id))
                blocks.controls.append(exame_block)
            return output

    def verify_day_output(self, data):
        id_user = self.page.client_storage.get("logged_user_id")
        consultas = DataMethods.show_consultas(id_user)
        consultas = self.sort_dates(consultas)
        exames = DataMethods.show_exames(id_user)
        exames = self.sort_dates(exames)
        remedios = DataMethods.show_remedios(id_user)
        remedios = self.sort_meds(remedios)


        blocks = Column([], scroll=ScrollMode.ALWAYS, width=355)
        output = Container(width=370, height=235, content=blocks)

        for consulta in consultas:
            if consulta[5] == data:
                consulta_block = Container(border_radius=15,
                                           height=60,
                                           width=355,
                                           bgcolor=colors.BLUE,
                                           padding=padding.only(top=5, left=5, right=5),
                                           content=Stack([
                                               Container(
                                                   Text(
                                                       f"{consulta[5][0]}" + f"{consulta[5][1]}" + f"{consulta[5][2]}" + f"{consulta[5][3]}" + f"{consulta[5][4]}",
                                                       size=25,
                                                       weight=FontWeight.W_900,
                                                       color=colors.WHITE),
                                                   padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                   border_radius=10,
                                                   bgcolor=colors.BLUE_300,
                                                   width=92,
                                                   height=48
                                               ),
                                               Row([
                                                   Text("              "),
                                                   Text(f"{consulta[2]}",
                                                        size=18,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_600),
                                                   Text(),
                                                   Text()],
                                                   height=45,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN),
                                               Column([Text(height=15), Row([
                                                   Text("              "),
                                                   Text(f" - {consulta[3]}",
                                                        size=15,
                                                        color=colors.WHITE,
                                                        weight=FontWeight.W_400),
                                                   Text(),
                                                   Text()],
                                                   height=32,
                                                   alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                      height=48, ),
                                               Row([Text("  "),
                                                    Text(f"{consulta[4]}",
                                                         size=11,
                                                         color=colors.WHITE,
                                                         weight=FontWeight.W_600),
                                                    Text("           ")
                                                    ], alignment=MainAxisAlignment.SPACE_BETWEEN),

                                           ]), on_click=lambda e, id=consulta[0]: self.send_editmeda(e, id))
                blocks.controls.append(consulta_block)
        for exame in exames:
            if exame[5] == data:
                exame_block = Container(border_radius=15,
                                        height=60,
                                        width=355,
                                        bgcolor=colors.GREEN,
                                        padding=padding.only(top=5, left=5, right=5),
                                        content=Stack([
                                            Container(
                                                Text(
                                                    f"{exame[5][0]}" + f"{exame[5][1]}" + f"{exame[5][2]}" + f"{exame[5][3]}" + f"{exame[5][4]}",
                                                    size=25,
                                                    weight=FontWeight.W_900,
                                                    color=colors.WHITE),
                                                padding=padding.only(top=8, left=8, right=8, bottom=8),
                                                border_radius=10,
                                                bgcolor=colors.GREEN_300,
                                                width=92,
                                                height=48
                                            ),
                                            Row([
                                                Text("              "),
                                                Text(f"{exame[2]}",
                                                     size=18,
                                                     color=colors.WHITE,
                                                     weight=FontWeight.W_600),
                                                Text(),
                                                Text()],
                                                height=44,
                                                alignment=MainAxisAlignment.SPACE_BETWEEN),
                                            Column([Text(height=15), Row([
                                                Text("              "),
                                                Text(f" - {exame[3]}",
                                                     size=15,
                                                     color=colors.WHITE,
                                                     weight=FontWeight.W_400),
                                                Text(),
                                                Text()],
                                                height=32,
                                                alignment=MainAxisAlignment.SPACE_BETWEEN), ],
                                                   height=48, ),
                                            Row([Text(""),
                                                 Text(f"{exame[4]}",
                                                      size=11,
                                                      color=colors.WHITE,
                                                      weight=FontWeight.W_600),
                                                 Text("           ")
                                                 ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                                        ]), on_click=lambda e, id=exame[0]: self.send_editexams(e, id))
                blocks.controls.append(exame_block)
        return output

    def selected_date(self, e):
        data = e.control.data
        self.selected_day = data[0] + data[1]
        self.output.content = self.verify_day_output(data)
        self.build()
        e.page.update()

    def get_next(self, e):
        current = date(self.current_year, self.current_month, self.current_day)
        add_month = relativedelta.relativedelta(months=1)
        next_month = current + add_month

        self.current_year = next_month.year
        self.current_month = next_month.month
        self.current_day = next_month.day
        self.build()
        self.page.update()

    def get_previous(self, e):
        current = date(self.current_year, self.current_month, self.current_day)
        add_month = relativedelta.relativedelta(months=1)
        next_month = current - add_month

        self.current_year = next_month.year
        self.current_month = next_month.month
        self.current_day = next_month.day
        self.build()
        self.page.update()

    def get_calendar(self):
        cal = HTMLCalendar()
        return cal.monthdayscalendar(self.current_year, self.current_month)

    @staticmethod
    def translate_month(to_translate_month):
        if to_translate_month == "January":
            return "Janeiro"
        elif to_translate_month == "February":
            return "Fevereiro"
        elif to_translate_month == "March":
            return "Março"
        elif to_translate_month == 'April':
            return "Abril"
        elif to_translate_month == 'May':
            return "Maio"
        elif to_translate_month == 'June':
            return "Junho"
        elif to_translate_month == "July":
            return "Julho"
        elif to_translate_month == "August":
            return "Agosto"
        elif to_translate_month == "September":
            return "Setembro"
        elif to_translate_month == "October":
            return "Outubro"
        elif to_translate_month == "November":
            return "Novembro"
        elif to_translate_month == "December":
            return "Dezembro"
        else:
            return "Error"

    def build(self):
        current_calendar = self.get_calendar()
        month = self.translate_month(month_name[self.current_month])

        str_date = '{0} de {1}'.format(month, self.current_year)

        date_display = Text(value=str_date,
                            text_align=TextAlign.CENTER,
                            size=20,
                            color=TEXT_COLOR)
        previous_button = IconButton(icon=icons.ARROW_CIRCLE_LEFT,
                                     alignment=alignment.center_left,
                                     icon_size=20,
                                     icon_color=ICON_COLOR,
                                     on_click=self.get_previous)
        next_button = IconButton(icon=icons.ARROW_CIRCLE_RIGHT,
                                 alignment=alignment.center_right,
                                 icon_size=20,
                                 icon_color=ICON_COLOR,
                                 on_click=self.get_next)
        div = Divider(height=1, thickness=2, color=BORDER_COLOR)

        first_row = Container(padding=padding.only(left=15, right=15))
        first_row.content = Row([previous_button, date_display, next_button], alignment=MainAxisAlignment.SPACE_BETWEEN, height=40, width=315)

        week_days_row = Row([Text("S", size=20, color=TEXT_COLOR), Text("T", size=20, color=TEXT_COLOR), Text("Q", size=20, color=TEXT_COLOR), Text("Q", size=20, color=TEXT_COLOR), Text("S", size=20, color=TEXT_COLOR), Text("S", size=20, color=TEXT_COLOR), Text("D", size=20, color=TEXT_COLOR)], alignment=MainAxisAlignment.SPACE_AROUND)

        calendar_column = Column([Row([first_row],
                                      alignment=MainAxisAlignment.SPACE_BETWEEN,
                                      vertical_alignment=CrossAxisAlignment.CENTER,
                                      height=40,
                                      expand=False),
                                  div,
                                  week_days_row,
                                  div],
                                 spacing=2,
                                 width=355,
                                 height=330,
                                 alignment=MainAxisAlignment.SPACE_BETWEEN,
                                 expand=False)

        for week in current_calendar:
            week_row = Row(alignment=MainAxisAlignment.CENTER)
            for day in week:
                if day > 0:
                    is_current_day_font = FontWeight.W_300
                    is_current_day_bg = colors.TRANSPARENT
                    display_day = str(day)
                    if len(display_day) == 1: display_day = "0%s" % display_day
                    if day == self.current_day and self.current_month == datetime.today().month:
                        is_current_day_font = FontWeight.BOLD
                        is_current_day_bg = CURRENT_DAY_COLOR
                    if self.selected_day == display_day:
                        is_current_day_font = FontWeight.BOLD
                        is_current_day_bg = SELECTED_DAY_COLOR

                    day_button = Container(
                        content=Text(display_day,
                                     weight=is_current_day_font,
                                     color=TEXT_COLOR),
                        on_click=self.selected_date, data=f"{display_day}/0%s/{self.current_year}" % self.current_month,
                        width=40,
                        height=40,
                        ink=True,
                        alignment=alignment.center,
                        border_radius=border_radius.all(10),
                        bgcolor=is_current_day_bg
                    )
                else:
                    day_button = Container(width=40, height=40, border_radius=border_radius.all(10))
                week_row.controls.append(day_button)
            calendar_column.controls.append(week_row)
        dia = self.selected_day
        self.page.client_storage.set("number_month", self.current_month)
        self.page.client_storage.set("year", self.current_year)
        self.page.client_storage.set("month", month)
        if self.selected_day is not None:
            self.page.client_storage.set("dia_1", dia)
        if self.selected_day is None:
            self.page.client_storage.set("dia_1", self.current_day)
        self.calendar_container.content = calendar_column
        return self.calendar_container


