from game import Game 
import pygame 

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.game = Game()
        self.clock = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def main(self):
        while True:
            self.events()
            self.screen.fill((0,0,0))

            self.game.update()

            self.clock.tick(60)
            pygame.display.flip()

if __name__ == '__main__':
    main = Main()
    main.main()
