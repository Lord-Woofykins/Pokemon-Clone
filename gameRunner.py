import pygame
from titlescreen import TitleScreen

from Constants import HEIGHT, WIDTH, FPS

class gameRunner():
    def __init__(self) -> None:
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = TitleScreen()


    def run(self) -> None:
        pygame.init()
        while self.running:
            # Game Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.scene.update()
            self.scene.display()
            pygame.display.flip()
            self.clock.tick(FPS)


    def displayGame(self):
        pass