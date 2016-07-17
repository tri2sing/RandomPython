'''
Created on Jul 16, 2016

@author: Sameer Adhikari
'''

# TODO: Change colors of triangles at level 0 or 2.

import pygame
from point import Point

class FractalSierpinski(object):
    def __init__(self, surface_size=800):
        pygame.init()
        self.surface_size = surface_size
        self.surface = pygame.display.set_mode((self.surface_size, self.surface_size))
        self.clock = pygame.time.Clock()
        self.surface.fill((255, 255, 255))
        self.colors = [(128, 0, 0), (0, 128, 0), (0, 0, 128)]
        self.num_colors = len(self.colors)
        pygame.display.update()
    
    def _draw_triangle(self, levels, points, color_choice):
        """
            levels (int): number of levels to draw fractal.
            points ([tuple]): points to draw the triangle.
            color_choice (tuple): the (r, g, b) option to use for drawing the triangle
            
        """
        pygame.draw.polygon(self.surface, color_choice, [(p.x, p.y) for p in points], 1)
        
        if levels > 0:
            midpoints = [points[i].mid_point(points[(i + 1)%3]) for i in range(3)]
            for i in range(3):
                self._draw_triangle(levels-1, [points[i], midpoints[i], midpoints[(i + 2)%3]], color_choice)
        
    def draw_triangle(self, levels, points):
        while True:
            evt = pygame.event.poll()
            if evt.type == pygame.QUIT:
                self.surface.fill((255, 255, 255))
                pygame.display.update()
                break
            elif evt.type == pygame.MOUSEBUTTONUP:
                self.surface.fill((255, 255, 255))
                self._draw_triangle(levels, points, (0, 0, 0))
                pygame.display.update()
                self.clock.tick(60)

    def exit_program(self):
        pygame.quit()

if __name__ == '__main__':
    # Define the vertices of an equilateral triangle
    p1 = Point(0.0, 0.0)
    p2 = Point(200.0, 346.41)
    p3 = Point(400.0, 0.0)        
    fs = FractalSierpinski()
    points = [p1, p2, p3]    
    #fs.draw_triangle(0, points)
    #fs.draw_triangle(1, points)
    #fs.draw_triangle(2, points)
    #fs.draw_triangle(5, points)
    fs.draw_triangle(6, points)
    fs.exit_program()
    
    