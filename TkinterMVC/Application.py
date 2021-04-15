import tkinter as tk

from Model import Model
from View import View
from Controller import Controller

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.model = Model()

        master.geometry(str(self.model.width)+"x"+str(self.model.height))
        master.title("Window Name")

        self.view = View(master)
        self.controller = Controller(master,self.model,self.view)