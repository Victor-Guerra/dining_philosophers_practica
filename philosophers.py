import time
import random
import threading
from PIL import ImageTk, Image

class Philosopher():
    __running = True
    __wsem = threading.Semaphore(1)

    def __init__(self, number, canvas, label, image):
        #super().__init__(self)
        self.number = number
        self.label = label
        self.canvas = canvas
        #self.image = image
        self.setImage(image)
        self.position_labels()

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

    def position_labels(self):
        self.label.grid(row=self.number, column=self.number)
        self.canvas.create_image(40 * self.number, 20 * self.number, image=self.image)
        #self.image.grid(row=self.number + 1, column=self.number)


    def setLabel(self, text):
        self.label["text"] = text

    def setImage(self, img):
        self.image = ImageTk.PhotoImage(Image.open(img).resize((80, 80)))
        self.canvas.create_image(80 * self.number, 80 * self.number, image=self.image)
        #self.Tkphoto = image 

    def forceDeadlock(self, forks):
        forks[self.number].acquire()
    
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
        self.setImage("./img/beef.png")

    def stop(self):
        self.__wsem.acquire()
        self.__running = False
        self.__wsem.release()

    def keepRunning(self):
        self.__wsem.acquire()
        temp = self.__running 
        self.__wsem.release()
        return temp


