import time
import random
import threading
from PIL import ImageTk, Image

class Philosopher():
    __running = True
    deadlock = False
    __wsem = threading.Semaphore(1)

    def __init__(self, number, label, image):
        #super().__init__(self)
        self.number = number
        self.label = label
        self.image = image
        self.position_labels()
        self.setLabel("Philosopher {}".format(self.number))

    def run(self, forks, room):
        self.__running = True
        while self.keepRunning():

            self.think()
            self.waitForks()
            room.acquire()
            
            forks[self.number].acquire()
            forks[(self.number + 1) % 5].acquire()
            
            self.eat()

            forks[(self.number + 1) % 5].release()
            forks[self.number].release()
            room.release()

        self.setImage("./img/philosopher.png")
        self.setLabel("Philosopher {}".format(self.number))

    def position_labels(self):
        self.label.grid(row=self.number, column=self.number)
        self.image.grid(row=self.number + 1, column=self.number)


    def setLabel(self, text):
        self.label["text"] = text

    def setImage(self, img):
        image = ImageTk.PhotoImage(Image.open(img).resize((80, 80)))
        self.image["image"] = image
        self.Tkphoto = image 

    def iniciar_deadlock(self, forks, room_grande):
        self.stop()
        forks[self.number].acquire()
        self.forceDeadlock(forks, room_grande)


    def forceDeadlock(self, forks, room):
        self.__running = True
        self.deadlock = True
        while self.keepRunning():

            self.think()
            self.waitForks()
            room.acquire()
            print(self.number, " adquiere room")
            
            forks[self.number].acquire(False)
            print(self.number, " adquiere propio")
            forks[(self.number + 1) % 5].acquire()
            print(self.number, " adquiere siguiente")
            
            self.eat()

            forks[(self.number + 1) % 5].release()
            print(self.number, " suelta siguiente")
            forks[self.number].release()
            print(self.number, " suelta propio")
            room.release()
            print(self.number, " suelta room")

        self.setImage("./img/philosopher.png")
        self.setLabel("Philosopher {}".format(self.number))

    
    def think(self):
        self.setLabel("Thinking...")
        self.setImage("./img/philosopher.png")
        if self.keepRunning():
            time.sleep(random.randint(0,2))
            

    def eat(self):
        self.setLabel("Eating...")
        self.setImage("./img/stevemeat.png")
        if self.keepRunning():
            time.sleep(random.randint(0,6))

    def waitForks(self):
        self.setLabel("Waiting...")
        self.setImage("./img/sleep.png")

    def stop(self):
        self.__wsem.acquire()
        self.__running = False
        self.__wsem.release()

    def keepRunning(self):
        self.__wsem.acquire()
        temp = self.__running 
        self.__wsem.release()
        return temp


