import tkinter as tk
from PIL import ImageTk, Image
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
        self.put_bg()

    def create_widgets(self):
        self.Canvas = tk.Canvas(self, height=700, width=800, bg="white")
        self.Start = tk.Button(self, text="Start", fg="black", bg="#CCCCCC")
        self.Stop = tk.Button(self, text="Stop", fg="black", bg="#CCCCCC")
        self.ForceDeadlock = tk.Button(self, text="Force Deadlock", fg="black", bg="#CCCCCC")
        self.Quit = tk.Button(self, text="Quit", fg="#BB2233", bg="#CCCCCC", command=self.exit)

    def position_widgets(self):
        self.Canvas.grid(row=0, column=0, columnspan=9)
        self.Start.grid(row=1, column=1)
        self.Stop.grid(row=1, column=3)
        self.ForceDeadlock.grid(row=1, column=5)
        self.Quit.grid(row=1, column=7)

    def put_bg(self):
        self.bg_img = ImageTk.PhotoImage(Image.open("./img/fondo.png").resize((410,430)))
        self.Canvas.create_image(205, 213, image=self.bg_img)
        
         
    def exit(self):
        self.quit()
        exit()
