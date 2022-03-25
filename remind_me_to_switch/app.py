import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("RemindMe by LuminousNodes")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="clock.png"))

        self.root.mainloop()


App()        