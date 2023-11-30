from tkinter import Tk, Canvas, ARC, W 
from human import human

class Hero(human):

    def __init__(self, canvas, name, x,y,gen) :
        super(). __init__(canvas, name, x,y,gen)
        self.health = 100
        
    def _drawName (self):
        self.canvas.create_tesxt(self.x+25,self.t-250, text=self._name, anchor=W, font="Arial", fill="salom")
        
        
