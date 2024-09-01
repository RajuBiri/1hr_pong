import pygame 

class Ball:
    def __init__(self,surface):
        self.surface = surface

        self.pos = pygame.math.Vector2(380,270)

    def draw(self):
        pygame.draw.rect(self.surface,((255,255,255)), pygame.Rect(self.pos.x,self.pos.y,30,30))

