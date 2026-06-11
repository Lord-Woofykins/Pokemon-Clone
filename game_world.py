import pygame
import json
import random

from abstract_classes import scene
from data_managers import inputManager, saveManager

from constants import palette, images

class player():
    def __init__(self, start_coords: tuple):
        self.sprite = pygame.image.load(images["player"]).convert_alpha()

        self.x, self.y = start_coords

    def display(self):
        pygame.display.get_surface().blit(self.sprite, (self.x*75, self.y*75))
    
    def move(self, x, y, boundaryMovementCallback, boundaryEventCallback):
        future_x = self.x + x
        future_y = self.y + y

        if boundaryMovementCallback(future_x, future_y):
            self.x = future_x
            self.y = future_y

            boundaryEventCallback(self.x, self.y)

class gameWorld(scene):
    def __init__(self, change_scene):
        super().__init__(change_scene)
        # TODO: Implement gameWorld

        # External References
        self.scene_change_callback("titleScreen")
        
        self.input_manager = inputManager()
        self.save_manager = saveManager()

        self.player = player((10, 8))

        # Variable Constants
        self.screen = pygame.display.get_surface()



        self.current_map = self.save_manager.retrieve("map")
        with open(f"assets/maps/{self.current_map}", "r") as map_data:
            self.map_data = json.load(map_data)


    def update(self):
        pass

    def display(self):
        self.screen.fill(palette["black"])

        dictEntry = self.map_data["layers"]["ground"]
        for y in range(len(dictEntry)):
            for x in range(len(dictEntry[0])):
                match dictEntry[y][x]:
                    case 0:
                        tile = pygame.image.load(images["dirt"])
                    case 1:
                        tile = pygame.image.load(images["grass"])
                    case 2:
                        tile = pygame.image.load(images["path"])
                    case 3:
                        tile = pygame.image.load(images["brick_wall"])
                    case 4:
                        tile = pygame.image.load(images["doorTop"])
                    case 5:
                        tile = pygame.image.load(images["doorBottom"])
                    case 6:
                        tile = pygame.image.load(images["roof"])
                    case 7:
                        tile = pygame.image.load(images["window"])
                    case _:
                        tile = pygame.image.load(images["default"])

                self.screen.blit(tile, (x*75, y*75))
        
        self.player.display()
        
        dictEntry = self.map_data["layers"]["decorations"]
        for y in range(len(dictEntry)):
            for x in range(len(dictEntry[0])):
                if dictEntry[y][x] != 0:
                    match dictEntry[y][x]:
                        case 1:
                            decoration = pygame.image.load(images["fence"]).convert_alpha()
                        case 2:
                            decoration = pygame.image.load(images["tall_grass"]).convert_alpha()
                        case _:
                            decoration = pygame.image.load(images["fence"]).convert_alpha()
                    
                    self.screen.blit(decoration, (x*75, y*75))
                
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.input_manager.retrieve("up"):
                self.player.move(0, -1, self.checkBoundaryMovement, self.checkBoundaryEvent)
            elif event.key == self.input_manager.retrieve("down"):
                self.player.move(0, 1, self.checkBoundaryMovement, self.checkBoundaryEvent)
            elif event.key == self.input_manager.retrieve("left"):
                self.player.move(-1, 0, self.checkBoundaryMovement, self.checkBoundaryEvent)
            elif event.key == self.input_manager.retrieve("right"):
                self.player.move(1, 0, self.checkBoundaryMovement, self.checkBoundaryEvent)

    def checkBoundaryMovement(self, x, y) -> bool:
        """Returns True if there is no boundary conflicing with the given position."""
        if self.map_data["layers"]["boundaries"][y][x] == 1:
            return False
        else:
            return True
    
    def checkBoundaryEvent(self, x, y):
        """"""
        if self.map_data["layers"]["boundaries"][y][x] == 2:
            if random.random() < 0.08:
                self.scene_change_callback("battle")