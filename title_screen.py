import pygame

from input_manager import inputManager
from abstract_classes import scene
from constants import ANTIALIASING, HEIGHT, WIDTH, fonts, palette


class titleScreen(scene):
    def __init__(self):
        """A class to display the titlescreen, using variable colours to indicate selection."""
        pygame.font.init()

        # Keybinds Manager Reference
        self.input_manager = inputManager()

        # Font Settings
        self.antialiasing = ANTIALIASING

        # Fonts
        self.title_font = pygame.font.Font(fonts["title_header"], 96)
        self.body_font = pygame.font.Font(fonts["title_body"], 48)

        # Text Renders of Fonts
        self.title_text = self.title_font.render("test", self.antialiasing, palette["title_text"])
        self.play_text = self.body_font.render("Play", self.antialiasing, palette["title_text"])
        self.restart_text = self.body_font.render("Restart", self.antialiasing, palette["title_text"])
        self.new_game_text = self.body_font.render("New Game", self.antialiasing, palette["title_text"])
        self.keybind_option_text = self.body_font.render("Change Keybinds", self.antialiasing, palette["title_text"])
        self.quit_text = self.body_font.render("Quit Game", self.antialiasing, palette["title_text"])

        self.text_rect_coords = {
            "title_text": (WIDTH // 2, HEIGHT // 5),
            "play_text": (WIDTH // 2, HEIGHT // 3),
            "new_game_text": (WIDTH // 2, HEIGHT // 1.8),
            "keybind_option_text": (WIDTH // 2, int(HEIGHT // 1.3)),
            "quit_text": (WIDTH // 2, int(HEIGHT // 1.1))
        }

        self.text_records = {
            "title_text": self.title_text,
            "play_text": self.play_text,
            "new_game_text": self.new_game_text,
            "keybind_option_text": self.keybind_option_text,
            "quit_text": self.quit_text,
        }
        
        self.screen = pygame.display.get_surface()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.selected_option = None


    def display(self): 
        """Displays the text elements on the sceen."""
        self.screen.fill(palette["title_screen"])

        for element in self.text_records:
            x, y = self.text_rect_coords[element]
            surface = self.text_records[element]
            self.screen.blit(surface, (x, y))

    def update(self):
        '''Animations?'''
        # TODO: Add animations
        
        pass

    def handleEvent(self, event):
        # TODO: Add titlescreen event handling
        if event.type == self.input_manager.binds["up"]:
            pass