from datetime import datetime
from typing import List

from const import DEFAULT_EVENTS
from utils.singleton import SingletonBase


class Event:
    def __init__(self, name: str, time: datetime, day: List[str]):
        self.name = name
        self.time = time
        self.days = day


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
                        DEFAULT_EVENTS[event_name]["name"],
                        datetime.strptime(time, "%H:%M"),
                        DEFAULT_EVENTS[event_name]["day"],
                    ) for time in DEFAULT_EVENTS[event_name]["time"]
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
