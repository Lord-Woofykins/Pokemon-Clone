import json

import pygame

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

        with open("saveFile.json", "w") as saveFile:
            saveData = json.load(saveFile)
            self.binds = saveData["binds"]

    def run(self) -> None:
        pygame.init()
        while self.running:
            # Game Input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.scene.handleEvent(event)

            self.scene.update()
            self.scene.display()
            pygame.display.flip()
            self.clock.tick(FPS)

    def displayGame(self) -> None:
        pass
