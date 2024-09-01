from ball import Ball
from bar import Bar

import pygame 

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface((800,600))

        self.ball = Ball(self.surface)
        self.bar1 = Bar(self.surface,pygame.math.Vector2(310,550))
        self.bar2 = Bar(self.surface,pygame.math.Vector2(310,50))

        self.ctrl = True
        self.ball_dir = pygame.math.Vector2(3,3)

        self.sc = 0 

    def draw(self):
        self.screen.blit(self.surface,(0,0))
        self.surface.fill((0,0,0))
        self.ball.draw()
        self.bar1.draw()
        self.bar2.draw()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.ctrl:
                self.bar1.pos.x -= 8 
            else:
                self.bar2.pos.x -= 8 
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.ctrl:
                self.bar1.pos.x += 8
            else:
                self.bar2.pos.x += 8 

        self.ball.pos += self.ball_dir

    def collide(self):
        if self.ctrl:
            if self.bar1.pos.x < 0:
                self.bar1.pos.x = 0 
            elif self.bar1.pos.x > 770 - 150:
                self.bar1.pos.x = 770 - 150
        else:
            if self.bar2.pos.x < 0:
                self.bar2.pos.x = 0 
            elif self.bar2.pos.x > 770 - 150:
                self.bar2.pos.x = 770 - 150

        if abs(self.ball.pos.y - self.bar1.pos.y) < 40 and abs(self.ball.pos.x - self.bar1.pos.x) < 150:
            self.reflect_bar()
            self.sc += 1
            print("score" + str(self.sc))
            self.ctrl = not self.ctrl

        if abs(self.ball.pos.y - self.bar2.pos.y) < 40 and abs(self.ball.pos.x - self.bar2.pos.x) < 150:
            self.reflect_bar()
            self.sc += 1
            self.ctrl = not self.ctrl

        if self.ball.pos.x < 0 or self.ball.pos.x > 770:
            self.reflect_field()
        if self.ball.pos.y < 0 or self.ball.pos.y > 570:
            pygame.quit()
            print("\n\n\n\n\n\n\n                               Game over                             \n\n\n\n\n\n")
            exit()

    def reflect_bar(self):
        self.ball_dir = pygame.math.Vector2(self.ball_dir.x,-self.ball_dir.y)

    def reflect_field(self):
        self.ball_dir = pygame.math.Vector2(-self.ball_dir.x,self.ball_dir.y)

    def update(self):
        self.draw()
        self.collide()
        self.move()

