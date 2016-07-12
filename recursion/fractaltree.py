'''
Created on Jul 11, 2016

@author: Sameer Adhikari
'''

import pygame, math

class FractalTree(object):
    def __init__(self, surface_size=1024):
        pygame.init()
        self.surface_size = surface_size
        self.main_surface = pygame.display.set_mode((self.surface_size, self.surface_size))
        self.clock = pygame.time.Clock()
        self.main_surface.fill((255, 255, 0))
        pygame.display.update()
        
    def draw_tree(self, levels, size, ratio, start_coordinates, heading, heading_change, color=(0, 0, 0)):
        '''
            levels: number of levels to draw the tree.
            size: total size of the tree.
            ration: the proportion of the total size that is the trunk.
            start_coordinates: coordinates of where the trunk starts.
            heading: direction to draw the trunk.
            heading_change: change in the heading for the next level of the tree.
            
        '''
        trunk_size = ratio * size  # length of the trunk
        delta_x = trunk_size * math.cos(heading) 
        delta_y = trunk_size * math.sin(heading) 
        (start_x, start_y) = start_coordinates
        end_coordinates = (start_x + delta_x, start_y + delta_y)
        pygame.draw.line(self.main_surface, color, start_coordinates, end_coordinates)
        
        if levels > 0:
            self.draw_tree(levels - 1, size * (1 - ratio), ratio, end_coordinates, heading - heading_change, heading_change, color)
            self.draw_tree(levels - 1, size * (1 - ratio), ratio, end_coordinates, heading + heading_change, heading_change, color)

    def run_event_loop(self, levels, heading, heading_change):
        while True:
            evt = pygame.event.poll()
            if evt.type == pygame.QUIT:
                self.main_surface.fill((255, 255, 0))
                pygame.display.update()
                break
            elif evt.type == pygame.MOUSEBUTTONUP:
                self.main_surface.fill((255, 255, 0))
                self.draw_tree(levels, self.surface_size * 0.5, 0.29, (self.surface_size//2, self.surface_size//2), heading, heading_change)
                pygame.display.update()
                self.clock.tick(120)
                heading += 10
        
    def exit_program(self):
        pygame.quit()
        
        
if __name__ == '__main__':
    ft = FractalTree()
    ft.run_event_loop(7, 0, -math.pi/2)
    ft.run_event_loop(7, 0, -math.pi/3)
    ft.run_event_loop(7, 0, -math.pi/4)
    ft.run_event_loop(7, 0, -math.pi/6)
    ft.run_event_loop(7, 0, -math.pi/12)
    ft.run_event_loop(7, 0, 0)
    ft.exit_program()
    
    
    