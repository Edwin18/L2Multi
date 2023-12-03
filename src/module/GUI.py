"""
This module handles the graphical user interface (GUI) of the application. It is built on the `tkinter` library,
which is the standard Python interface to the Tk GUI toolkit. The GUI module is responsible for rendering the
interface, handling user interactions, and managing GUI events.

Dependencies:
- `tkinter`: Used for creating and managing GUI elements such as windows, buttons, and text fields.
"""

import tkinter as tk

from utils.resource_path import resource_path
from utils.singleton import SingletonBase


class CheckButton(tk.Checkbutton):
    """
    Subclass of tk.Checkbutton with an additional 'var' attribute for convenient state tracking.
    The 'var' attribute is an instance of tk.BooleanVar, which automatically updates when the state of the checkbox changes.
    """
    def __init__(self, master=None, checked=False, **kwargs):
        self.var = tk.BooleanVar(master, value=checked)
        super().__init__(master, variable=self.var, **kwargs)


class GUI(tk.Tk, SingletonBase):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("L2Multi")
        self.iconbitmap(resource_path("src/L2.ico"))

    def CheckButton(self, checked, **kwargs) -> CheckButton:
        checkbutton = CheckButton(self, checked=checked, **kwargs)
        return checkbutton
