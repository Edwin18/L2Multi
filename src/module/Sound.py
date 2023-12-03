"""
This module manages sound playback functionalities of the application. It relies on the `pygame` library,
specifically pygame's mixer module, to load, play, and control audio files. It provides an interface
for playing sound effects and music within the application.

Dependencies:
- `pygame`: Used for loading, playing, and controlling audio files.
"""

from utils.singleton import SingletonBase


class Sound(SingletonBase):
    def __init__(self):
        pass


# pip install pygame

# TODO: реализовать саунд класс и 2 метода плей стоп, внутри плея будем првоерять состояние что бы по новой не запускать
# использовать будем pygame

# pygame

# import pygame

# # Инициализация pygame
# pygame.mixer.init()

# def play_alarm_sound():
#     # Загрузка и воспроизведение звукового файла
#     pygame.mixer.music.load('path_to_sound.mp3')
#     pygame.mixer.music.play()

# def stop_alarm_sound():
#     # Остановка воспроизведения
#     pygame.mixer.music.stop()

# # Использование в обработчике событий
# def process_scheduled_events():
#     now = datetime.now(pytz.timezone(DEFAULT_EVENT_TIME_ZONE))
#     for event in Events().list:
#         if (now.time().replace(second=0, microsecond=0) == event.time.time().replace(second=0, microsecond=0) and
#                 now.strftime("%A") in event.days):
#             play_alarm_sound()
#     app.after(1000, process_scheduled_events)
