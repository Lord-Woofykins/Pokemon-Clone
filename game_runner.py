import pygame

from data_managers import inputManager
from constants import FPS, HEIGHT, WIDTH
from title_screen import titleScreen
from game_world import gameWorld


class gameRunner:
    def __init__(self) -> None:
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("The Amazing Pokémon Clone")
        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = titleScreen(self.changeScene)

        self.input_manager = inputManager()

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
                    elif event.key == self.input_manager.retrieve("quit"):
                        self.running = False
                    else:
                        self.scene.handleEvent(event)
                
                else:
                    self.scene.handleEvent(event)
            self.scene.update()
            self.scene.display()
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def changeScene(self, option):
        match option:
            case "title_screen":
                self.scene = titleScreen(self.changeScene)
            case "world":
                self.scene = gameWorld(self.changeScene)