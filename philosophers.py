import time
import random
import threading

class Philosopher():
    __running = True
    __wsem = threading.Semaphore(1)
    def __init__(self, number, label, image):
        #super().__init__(self)
        self.number = number
        self.label = label
        self.image = image
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
        self.image.grid(row=self.number + 1, column=self.number)


    def setLabel(self, text):
        self.label["text"] = text
    
    def think(self):
        self.setLabel("Thinking...")
        if self.keepRunning():
            time.sleep(random.randint(0,2))
            

    def eat(self):
        self.setLabel("Eating...")
        if self.keepRunning():
            time.sleep(random.randint(0,6))

    def waitForks(self):
        self.setLabel("Waiting...")

    def stop(self):
        self.__wsem.acquire()
        self.__running = False
        self.__wsem.release()

    def keepRunning(self):
        self.__wsem.acquire()
        temp = self.__running 
        self.__wsem.release()
        return temp


