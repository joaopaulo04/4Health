import calendar

from dateutil import relativedelta
from flet import *
from calendar import *
from datetime import *

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

        self.output = Text("Teste")

    def selected_date(self, e):
        data = e.control.data
        self.selected_day = data[0] + data[1]
        self.output.value = e.control.data
        self.build()
        self.page.update()

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

        self.calendar_container.content = calendar_column
        return self.calendar_container


