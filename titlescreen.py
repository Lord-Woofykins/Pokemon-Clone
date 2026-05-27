import pygame
from abstractClasses import scene
from Constants import fonts, palette, ANTIALIASING, WIDTH, HEIGHT

class TitleScreen(scene):
    def __init__(self):
        pygame.font.init()

        # Font Settings
        self.antialiasing = ANTIALIASING

        self.titleFont = pygame.font.Font(fonts["titleHeader"], 96)
        self.titleText = self.titleFont.render("test", self.antialiasing, palette["titleText"])
        self.bodyFont = pygame.font.Font(fonts["titleBody"], 48)
        self.bodyText = self.bodyFont.render("mwahhahahahahahah", self.antialiasing, palette["titleText"])

        self.textRectCoords = {
            "titleText": (WIDTH // 2, HEIGHT // 5),
            "startText": (WIDTH // 2, HEIGHT // 3),
            "newGameText": (WIDTH // 2, HEIGHT // 1.8),
            "continueText": (WIDTH // 2, int(HEIGHT // 1.5)),
            "keybindOptionText": (WIDTH // 2, int(HEIGHT // 1.3)),
            "selectArrow": (WIDTH // 2 - 200, int(HEIGHT // 1.8))
        }

        # TODO: Add remaining fonts and text
        
        
        self.screen = pygame.display.get_surface()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def display(self): 
        self.screen.fill(palette["titleScreen"])
        
        
        

        self.screen.blit(self.titleText, (20, 20))



    def update(self):
        '''Animations?'''
        # TODO Add animations
        pass

    def downKey(self):
        pass