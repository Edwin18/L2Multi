"""
This module is responsible for integrating the application with the system tray. It uses the `pystray` library
to create a system tray icon and associated menu, allowing the application to run in the background and be
accessible with minimal interaction.

Dependencies:
- `pystray`: Utilized for creating and handling the system tray icon and menu operations.
"""

# pip install pystray

# TODO: при создании трея прокидывать экземпляр гуи/аппа так же сделать его с синглтоном и можно спокойно повторно вызывать будет, но сперва проиниализировать в начале приложения

# Работа с системным треем
# Для работы с системным треем в Windows вы можете использовать библиотеку, такую как pystray. Эта библиотека позволяет создать иконку в трее и управлять ею.

# Этот код создает простое окно Tkinter и добавляет иконку в системный трей. При нажатии на иконку в трее появляется меню с опциями "Выйти" и "Показать". Вы можете настроить это поведение по своему усмотрению.

# Пример использования pystray:

# import tkinter as tk

# import pystray
# from PIL import Image, ImageDraw
# from pystray import MenuItem as item

# def create_image(width, height, color1, color2):
#     # Создание простого изображения для иконки трея
#     image = Image.new("RGB", (width, height), color1)
#     dc = ImageDraw.Draw(image)
#     dc.rectangle([width // 2, 0, width, height // 2], fill=color2)
#     dc.rectangle([0, height // 2, width // 2, height], fill=color2)

#     return image

# def on_clicked(icon, item):
#     icon.stop()
#     root.destroy()

# def show_window(icon, item):
#     icon.stop()
#     root.after(0, root.deiconify)

# def hide_window():
#     root.withdraw()
#     image = create_image(64, 64, "black", "red")
#     menu = (item("Выйти", on_clicked), item("Показать", show_window))
#     icon = pystray.Icon("name", image, "title", menu)
#     icon.run()

# root = tk.Tk()
# root.geometry('200x100')

# root.protocol("WM_DELETE_WINDOW", hide_window)

# root.mainloop()

# from pystray import Icon as icon, Menu as menu, MenuItem as item
# from PIL import Image, ImageDraw

# def create_image():
#     # Функция для создания изображения для иконки трея
#     image = Image.new('RGB', (64, 64), color=(0, 0, 0))
#     dc = ImageDraw.Draw(image)
#     dc.rectangle(
#         (0, 0, 64, 64),
#         fill=(0, 0, 0))
#     dc.text((10, 10), 'Icon', fill=(255, 255, 255))

#     return image

# def show_message(icon, item):
#     icon.notify('Hello World!', 'Title')

# def exit_action(icon, item):
#     icon.stop()

# # Создание иконки трея с меню
# icon('test', create_image(), menu=menu(
#     item('Show message', show_message),
#     item('Exit', exit_action)
# )).run()
