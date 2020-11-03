import threading as th
import tkinter as tk
import philosophers as ph
import philGui as gui
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Dining Philosophers")

def run_philosophers(appgui):
    img = ImageTk.PhotoImage(Image.open("./img/beef.png").resize((80, 80)))
    for i in range(0,5):
        p = ph.Philosopher(i, tk.Label(appgui, fg="white", bg="black"), tk.Label(appgui, image=img))
        thread = th.Thread(target=p.run, args=(forks, room))
        thread.start()

if __name__ == "__main__":
    appgui = gui.AppGUI(root)
    
    forks = [th.Semaphore(1) for i in range(5)]
    room = th.Semaphore(4)

    appgui.pack()

    run_philosophers(appgui.Canvas)
    appgui.mainloop()


