from tkinter import Tk, Canvas, ARC, SE, W


class Human():

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        
    def display(self):
        self.__drawHead()
        self.__drawBody()
        self.__drawLeggs()
        self.__drawHands()
        
    def __drawLeggs(self):
            self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width=2)
            
    def __drawHead(self):
            self.canvas.create_oval(self.x+25, self.y-150, self.x+75, self.y-200, width=2)
            self.canvas.create_arc(self.x+40, self.y-155, self.x+60, self.y-175, start=0, extent=-180, style=ARC, outline="red", width=3)
            self.canvas.create_oval(self.x+30, self.y-200, self.x+50, self.y-215, width=0, fill="green")
            self.canvas.create_oval(self.x+70, self.y-200, self.x+50, self.y-215, width=0, fill="orange")
            
    def __drawBody(self):
            self.canvas.create_line(self.x+50, self.y-50, self.x+50, self.y-150, width=2)

    def __drawHands(self):
            self.canvas.create_line(self.x, self.y-100, self.x+50, self.y-150, self.x+100, self.y-100, width=2)
