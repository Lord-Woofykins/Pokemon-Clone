import pygame

from inputManager import inputManager
from Constants import FPS, HEIGHT, WIDTH
from titlescreen import TitleScreen


class gameRunner:
    def __init__(self) -> None:
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = TitleScreen()

        self.inputManager = inputManager()

    def run(self) -> None:
        pygame.init()
        while self.running:
            # Game Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == self.inputManager.binds["quit"]:
                        self.running = False
                    else:
                        self.scene.handleEvent(event)
                
                else:
                    self.scene.handleEvent(event)

            self.scene.update()
            self.scene.display()
            pygame.display.flip()
            self.clock.tick(FPS)

    def displayGame(self) -> None:
        pass
