'''
Created on Jul 10, 2016

@author: Sameer Adhikari
'''

import turtle


class FractalKoch(object):
    def __init__(self):
        self.window = turtle.Screen()
        self.drawer = turtle.Turtle()
    
    def first_figure(self):
        self.drawer.forward(90)
        self.drawer.left(90)
        self.drawer.forward(90)
    
    def draw_fractals(self, order, distance):
        if order == 0:
            self.drawer.forward(distance)
        else:
            for angle in [60, -120, 60, 0]:
                self.draw_fractals(order - 1, distance / 3)
                self.drawer.left(angle)
            
    def wait_for_user(self):
        turtle.mainloop()
            
if __name__ == '__main__':
    fk = FractalKoch()
    fk.draw_fractals(1, 360)
    fk.wait_for_user()