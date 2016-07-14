'''
Created on Jul 10, 2016

@author: Sameer Adhikari
'''

import turtle


class FractalCesaro(object):
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title('Cesaro Fractal')
        self.drawer = turtle.Turtle()
        self.drawer.penup()
        self.drawer.goto(-200, 100) # very customized to my machine
        self.drawer.pendown()    
        
    def draw_cesaro_curve(self, order, distance, tear):
        if order == 0:
            self.drawer.forward(distance)
        else:
            for angle in [90 - (tear/2), 180 + tear, 90 - (tear/2), 0]:
                self.draw_cesaro_curve(order - 1, distance / 3, tear)
                self.drawer.right(angle)
    
    def draw_cesaro_square(self, order, distance, tear):
        for _ in range(4):
            self.draw_cesaro_curve(order, distance, tear)
            self.drawer.right(90)
        
                
    def wait_for_user(self):
        turtle.mainloop()
            
if __name__ == '__main__':
    fk = FractalCesaro()
    #fk.draw_cesaro_curve(3, 360, 10)
    fk.draw_cesaro_square(3, 540, 10)
    fk.wait_for_user()