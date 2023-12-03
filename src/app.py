from datetime import datetime
from tkinter import Event, Label, font

import pytz
from win10toast import ToastNotifier

from const import DEFAULT_EVENT_SCHEDULED_TIME, DEFAULT_EVENT_TIME_ZONE, DEFAULT_EVENTS
from Events import Events
from module.GUI import GUI, CheckButton
from utils.resource_path import resource_path
from utils.time import get_timedelta

toaster = ToastNotifier()

app = GUI()

#############
# Render UI #
#############

labels = {}

boldFont = font.Font(size=12, weight="bold")

label = Label(app, text="Список ивентов", font=boldFont)
label.grid(row=0, column=1, ipadx=5, ipady=5)
label = Label(app, text="Ближайшие ивенты", font=boldFont)
label.grid(row=0, column=2, ipadx=5, ipady=5)


def check_button_callback(event_name: str, instance: CheckButton):
    if instance.var.get():
        Events().add_event(event_name)
    else:
        Events().remove_event(event_name)
        label: Label = labels[event_name]
        label.config(text="")


def check_button_on_enter(event: Event):
    widget: CheckButton = event.widget
    widget.config(background="lightblue")


def check_button_on_leave(event: Event):
    widget: CheckButton = event.widget
    widget.config(background="SystemButtonFace")


# Render checkbuttons
for index, event_name in enumerate(DEFAULT_EVENTS):
    checkbutton = app.CheckButton(text=DEFAULT_EVENTS[event_name]["name"], checked=True, cursor="hand2")
    checkbutton.grid(row=index + 1, column=1, sticky="w")
    checkbutton.config(command=lambda cb=checkbutton, en=event_name: check_button_callback(en, cb))
    checkbutton.bind("<Enter>", check_button_on_enter)
    checkbutton.bind("<Leave>", check_button_on_leave)

# Render labels
for index, event_name in enumerate(DEFAULT_EVENTS):
    label = Label(app, text="")
    label.grid(row=index + 1, column=2)
    labels[event_name] = label

############
# Schedule #
############


def process_scheduled_events():
    now = datetime.now(pytz.timezone(DEFAULT_EVENT_TIME_ZONE))
    for event in Events().list:
        if (now.time().replace(second=0, microsecond=0) == event.time.time().replace(second=0, microsecond=0) and
                now.strftime("%A") in event.days):
            toaster.show_toast(
                title=event.name,
                msg="Пойди получи халявные ивентки, если конечно твоя команда победит, МУ-ХА-ХА!",
                icon_path=resource_path("src/L2.ico"),
                duration=60,
                threaded=True,
            )
    app.after(DEFAULT_EVENT_SCHEDULED_TIME, process_scheduled_events)


def process_next_events():
    now = datetime.now(pytz.timezone(DEFAULT_EVENT_TIME_ZONE))
    for default_event in [*DEFAULT_EVENTS]:
        label: Label = labels[default_event]
        if default_event in Events().active_list:
            events = Events().get_event(default_event)
            for event in events:
                if (now.time().replace(second=0, microsecond=0) < event.time.time().replace(second=0, microsecond=0) and
                        now.strftime("%A") in event.days):
                    label.config(text=get_timedelta(now, event.time))
                    break
                else:
                    label.config(text="До завтра:)")
        else:
            label.config(text="")
    app.after(1000, process_next_events)


app.after(DEFAULT_EVENT_SCHEDULED_TIME, process_scheduled_events)
app.after(1000, process_next_events)

# TODO: запилить таску которая будет генерить новые объекты дат каждый час например и все. Или придумать другой способ решения проблемы с временем до ивента который наступит уже АЖ завтра
##############
# App Events #
##############
# app.protocol('WM_DELETE_WINDOW', hide_window)

app.mainloop()
