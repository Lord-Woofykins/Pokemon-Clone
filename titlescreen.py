import pygame

from inputManager import inputManager
from abstractClasses import scene
from Constants import ANTIALIASING, HEIGHT, WIDTH, fonts, palette


class TitleScreen(scene):
    def __init__(self):
        """A class to display the titlescreen, using variable colours to indicate selection."""
        pygame.font.init()

        # Keybinds Manager Reference
        self.inputManager = inputManager()

        # Font Settings
        self.antialiasing = ANTIALIASING

        # Fonts
        self.titleFont = pygame.font.Font(fonts["titleHeader"], 96)
        self.bodyFont = pygame.font.Font(fonts["titleBody"], 48)

        # Text Renders of Fonts
        self.titleText = self.titleFont.render("test", self.antialiasing, palette["titleText"])
        self.playText = self.bodyFont.render("Play", self.antialiasing, palette["titleText"])
        self.restartText = self.bodyFont.render("Restart", self.antialiasing, palette["titleText"])
        self.newGameText = self.bodyFont.render("New Game", self.antialiasing, palette["titleText"])
        self.keyBindOptionText = self.bodyFont.render("Change Keybinds", self.antialiasing, palette["titleText"])
        self.quitText = self.bodyFont.render("Quit Game", self.antialiasing, palette["titleText"])

        self.textRectCoords = {
            "titleText": (WIDTH // 2, HEIGHT // 5),
            "playText": (WIDTH // 2, HEIGHT // 3),
            "newGameText": (WIDTH // 2, HEIGHT // 1.8),
            "keybindOptionText": (WIDTH // 2, int(HEIGHT // 1.3)),
            "quitText": (WIDTH // 2, int(HEIGHT // 1.1))
        }

        self.textRecords = {
            "titleText": self.titleText,
            "playText": self.playText,
            "newGameText": self.newGameText,
            "keybindOptionText": self.keyBindOptionText,
            "quitText": self.quitText,
        }
        
        self.screen = pygame.display.get_surface()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def display(self): 
        """Displays the text elements on the sceen."""
        self.screen.fill(palette["titleScreen"])

        for element in self.textRecords:
            x, y = self.textRectCoords[element]
            surface = self.textRecords[element]
            self.screen.blit(surface, (x, y))

    def update(self):
        '''Animations?'''
        # TODO: Add animations
        
        pass

    def handleEvent(self, event):
        # TODO: Add titlescreen event handling
        if event.type == self.inputManager.binds["up"]:
            pass