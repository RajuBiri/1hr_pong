import pygame 

class Bar:
    def __init__(self,surface,pos):
        self.surface = surface

        self.pos = pos

    def draw(self):
        pygame.draw.rect(self.surface,((255,255,255)),pygame.Rect(self.pos.x,self.pos.y,175,25))

    def move(self,dir):
        self.pos.x += dir
