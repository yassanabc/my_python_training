import tkinter as tk
import time

class Model():
    def __init__(self):
        self.width  = 500
        self.height = 400

        self.button_text = "Sample"
        self.label_text = "Time"

    def get_time(self):
        self.label_text = time()