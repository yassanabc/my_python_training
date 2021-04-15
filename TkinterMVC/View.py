import tkinter as tk

class View():
    def __init__(self,master):
        self.master = master

        self.create_widget

    def create_widget(self):
        button = tk.Button(
            width = 8,
            height = 1
        )

        label = tk.Label(
            width = 8,
            height = 1
        )