'''
Created on Jul 10, 2016

@author: Sameer Adhikari
'''

import turtle


class FractalKoch(object):
    def __init__(self):
        self.window = turtle.Screen()
        self.drawer = turtle.Turtle()
        self.drawer.penup()
        self.drawer.goto(-200, 100) # very customized to my machine
        self.drawer.pendown()    
        
    def draw_koch_curve(self, order, distance):
        if order == 0:
            self.drawer.forward(distance)
        else:
            for angle in [60, -120, 60, 0]:
                self.draw_koch_curve(order - 1, distance / 3)
                self.drawer.left(angle)
    
    def draw_koch_snowflake(self, order, distance):
        for _ in range(3):
            self.draw_koch_curve(order, distance)
            self.drawer.right(120)
        
                
    def wait_for_user(self):
        turtle.mainloop()
            
if __name__ == '__main__':
    fk = FractalKoch()
    fk.draw_koch_snowflake(3, 360)
    fk.wait_for_user()