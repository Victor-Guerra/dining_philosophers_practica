import threading as th
import tkinter as tk
import philosophers as ph
import philGui as gui
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Dining Philosophers")
root.geometry('410x450')

def run_philosophers():
    for p in philosophers:
        thread = th.Thread(target=p.run, args=(forks, room))
        thread.start()

def stop_philosophers():
    for p in philosophers:
        thread = th.Thread(target=p.stop())
        thread.start()

def force_deadlock():
    room_grande = th.Semaphore(5);
    for p in philosophers:
        print(p, " pre deadlock")
        #p.iniciar_deadlock(forks, room_grande)
        thread = th.Thread(target=p.iniciar_deadlock, args=(forks,room_grande))
        thread.start()

def create_philosophers(appgui):
    img = ImageTk.PhotoImage(Image.open("./img/philosopher.png").resize((80, 80)))
    philosophers = []

    for i in range(0,5):
        p = ph.Philosopher(i, tk.Label(appgui, fg="white", bg="black"), tk.Label(appgui, image=img))
        p.Tkphoto = img
        philosophers.append(p)
        
    return philosophers

if __name__ == "__main__":
    appgui = gui.AppGUI(root)
    appgui.Start["command"] = run_philosophers
    appgui.Stop["command"] = stop_philosophers
    appgui.ForceDeadlock["command"] = force_deadlock

    philosophers = create_philosophers(appgui.Canvas)

    
    forks = [th.Semaphore(1) for i in range(5)]
    room = th.Semaphore(4)

    appgui.pack()
    appgui.mainloop()
