from datetime import datetime


def get_timedelta(time1: datetime, time2: datetime) -> str:
    """
    Calculate the time difference between two datetime objects, considering only their time part.

    Args:
    time1 (datetime): The first datetime object.
    time2 (datetime): The second datetime object.

    Returns:
    str: The time difference in HH:MM:SS format.
    """

    # Convert each datetime's time to seconds from the start of the day
    seconds1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    seconds2 = time2.hour * 3600 + time2.minute * 60 + time2.second

    # Calculate the difference in seconds between the two times
    time_difference_in_seconds = seconds2 - seconds1

    # Convert the time difference back to hours, minutes, and seconds
    hours = time_difference_in_seconds // 3600
    minutes = (time_difference_in_seconds % 3600) // 60
    seconds = time_difference_in_seconds % 60

    # Format the result to always show two digits for hours, minutes, and seconds
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


# Example usage
# time1 and time2 should be datetime.datetime objects
# Example: get_timedelta(datetime(2023, 1, 1, 10, 30), datetime(2023, 1, 1, 11, 45))
