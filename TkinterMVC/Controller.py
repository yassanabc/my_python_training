import tkinter as tk

from Model import Model
from View import View

class Controller():
    def __init__(self,master,model,view):
        self.master = master
        self.model = model
        self.view = view
    
        self.view.button.config(
            text=self.model.button_text,
            command=self.model.get_time
            )
        self.view.label.config(
            text=self.model.label_text
        )