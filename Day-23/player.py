#Player

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.left(90)
        
    def cross_road(self):
        self.forward(MOVE_DISTANCE)
        
    def goto_start(self):
        self.goto(STARTING_POSITION)
        
    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False