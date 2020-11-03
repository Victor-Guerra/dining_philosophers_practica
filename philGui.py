import tkinter as tk
import os


def wea():
    pass

class AppGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        self.Canvas = tk.Canvas(self, height=700, width=800, bg="white")
        self.Start = tk.Button(self, text="Start", fg="black", bg="#CCCCCC", command=wea)
        self.Stop = tk.Button(self, text="Stop", fg="black", bg="#CCCCCC", command=wea)
        self.ForceDeadlock = tk.Button(self, text="Force Deadlock", fg="black", bg="#CCCCCC", command=wea)
        self.Quit = tk.Button(self, text="Quit", fg="#BB2233", bg="#CCCCCC", command=self.exit)

    def position_widgets(self):
        self.Canvas.grid(row=0, column=0, columnspan=9)
        self.Start.grid(row=1, column=1)
        self.Stop.grid(row=1, column=3)
        self.ForceDeadlock.grid(row=1, column=5)
        self.Quit.grid(row=1, column=7)
         
    def exit(self):
        self.quit()
        exit()
