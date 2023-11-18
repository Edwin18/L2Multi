import tkinter as tk

from utils.singleton import SingletonBase


class App(tk.Tk, SingletonBase):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("L2Multi")
        self.iconbitmap('L2.ico')
