import calendar
from datetime import datetime, timedelta
from typing import List

import pytz

from const import DEFAULT_EVENT_TIME_ZONE

pytz_timezone = pytz.timezone(DEFAULT_EVENT_TIME_ZONE)


def get_timedelta(now: datetime, event: datetime) -> str:
    """
    Calculate the total time difference between two datetime objects and return it in `HH:MM:SS` format.
    If the difference is more than 24 hours, hours will be extended accordingly.

    Args:
    now (datetime): The current datetime object.
    event (datetime): The event datetime object.

    Returns:
    str: The total time difference in `HH:MM:SS` format.
    """

    # Calculate the total difference in seconds

    print("compare =", event - now)

    total_seconds = int((event - now).total_seconds())

    # Calculate hours, minutes, and seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Format the result to show hours, minutes, and seconds
    # If hours exceed 24, they will be shown as is (e.g., 48 for 2 days)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def create_datetime(time_str: str, days_of_week: List[str]) -> datetime:
    """
    Update the given datetime object to the next closest day specified in the days_of_week list, keeping the time unchanged.

    Args:
    current_datetime (datetime): The current datetime object.
    days_of_week (List[str]): A list of days of the week to consider for the update.

    Returns:
    datetime: The updated datetime object set to the next occurrence of one of the specified days.
    """
    # Get the current datetime in the specified timezone
    now = datetime.now(pytz_timezone)

    # Преобразование строки времени в объект time
    event_time = datetime.strptime(time_str, "%H:%M").time()

    # Создание объекта datetime для текущего времени и времени события
    current_datetime = datetime.combine(now.date(), event_time)
    current_datetime = pytz_timezone.localize(current_datetime)

    # Convert days of the week to their corresponding indexes
    day_indexes = [list(calendar.day_name).index(day) for day in days_of_week]

    # Calculate the number of days until the next occurrence
    days_ahead = min([(day - current_datetime.weekday()) % 7 for day in day_indexes])
    # If the current time has passed and today is a potential event day, find the next day
    if days_ahead == 0 and current_datetime.time() < now.time():
        days_ahead = min([(day - current_datetime.weekday() - 1) % 7 for day in day_indexes if day != current_datetime.weekday()]) + 1

    # Calculate the new datetime for the next occurrence
    new_datetime = current_datetime + timedelta(days=days_ahead)

    return new_datetime
