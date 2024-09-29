from datetime import datetime
from typing import List

from const import DEFAULT_EVENTS
from utils.singleton import SingletonBase
from utils.time import create_datetime


class Event:
    def __init__(self, tech_name: str, name: str, time: datetime, days: List[str], win: int, los: int, msg: str):
        self.tech_name = tech_name
        self.name = name
        self.time = time
        self.days = days
        self.win = win
        self.los = los
        self.msg = msg

    def update_time(self):
        self.time = create_datetime(self.time.strftime("%H:%M"), self.days)


class Events(SingletonBase):
    def __init__(self):
        # TODO: Будем доставать сохраненные настройки чекбоксов и если они есть будем перезаписывать дефолтный массив если нет то берем дефолтный
        self.active_list: List[str] = [*DEFAULT_EVENTS]
        self.list: List[Event] = []

        for event_name in [*DEFAULT_EVENTS]:
            self.__set_dynamic_attribute(
                f"__{event_name}",
                [
                    Event(
                        DEFAULT_EVENTS[event_name]["tech_name"],
                        DEFAULT_EVENTS[event_name]["name"],
                        create_datetime(time, DEFAULT_EVENTS[event_name]["days"]),
                        DEFAULT_EVENTS[event_name]["days"],
                        DEFAULT_EVENTS[event_name]["win"],
                        DEFAULT_EVENTS[event_name]["los"],
                        DEFAULT_EVENTS[event_name]["msg"],
                    ) for time in DEFAULT_EVENTS[event_name]["times"]
                ],
            )

        self.__update_list()

    def __set_dynamic_attribute(self, name: str, value: List[Event]):
        setattr(self, name, value)

    def __update_list(self):
        self.list = []
        for event_name in self.active_list:
            event_list = getattr(self, f"__{event_name}", [])
            self.list.extend(event_list)

    def add_event(self, event_name):
        if event_name not in self.active_list:
            self.active_list.append(event_name)
            self.__update_list()

    def get_event(self, event_name) -> List[Event]:
        return getattr(self, f"__{event_name}", [])

    def remove_event(self, event_name):
        if event_name in self.active_list:
            self.active_list.remove(event_name)
            self.__update_list()
