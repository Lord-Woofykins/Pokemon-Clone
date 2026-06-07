import pygame

from input_manager import inputManager
from abstract_classes import scene
from constants import ANTIALIASING, HEIGHT, WIDTH, fonts, palette


class titleScreen(scene):
    def __init__(self, change_scene):
        """A class to display the titlescreen, using variable colours to indicate selection."""
        pygame.font.init()

        # External References
        self.input_manager = inputManager()
        self.scene_change_callback = change_scene

        # Font Settings
        self.antialiasing = ANTIALIASING
        self.title_font_size = 96
        self.body_font_size = 60

        self.text_names = {
            "title_text": "The Amazing Pokémon Clone",
            "play_text": "Play / Resume",
            "new_game_text": "New Game",
            "keybind_option_text": "Change Keybinds",
            "quit_text": "Quit",
        }

        # Fonts
        self.title_font = pygame.font.Font(fonts["title_header"], self.title_font_size)
        self.body_font = pygame.font.Font(fonts["title_body"], self.body_font_size)

        # Text Renders of Fonts
        self.title_text = self.title_font.render(self.text_names["title_text"], self.antialiasing, palette["title_text"])
        self.play_text = self.body_font.render(self.text_names["play_text"], self.antialiasing, palette["title_text"])
        self.new_game_text = self.body_font.render(self.text_names["new_game_text"], self.antialiasing, palette["title_text"])
        self.keybind_option_text = self.body_font.render(self.text_names["keybind_option_text"], self.antialiasing, palette["title_text"])
        self.quit_text = self.body_font.render(self.text_names["quit_text"], self.antialiasing, palette["title_text"])

        self.menu_start = 3
        self.line_height = self.body_font_size * 1.5

        self.text_rect_coords = {
            "title_text": (WIDTH // 8, HEIGHT // 5),
            "play_text": (WIDTH // 8, (HEIGHT // self.menu_start) + self.line_height),
            "new_game_text": (WIDTH // 8, (HEIGHT // self.menu_start) + self.line_height * 2),
            "keybind_option_text": (WIDTH // 8, (HEIGHT // self.menu_start) + self.line_height * 3),
            "quit_text": (WIDTH // 8, (HEIGHT // self.menu_start) + self.line_height * 5)
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

        self.selected_option = 1


    def display(self): 
        """Displays the text elements on the sceen."""
        self.screen.fill(palette["title_screen"])

        for element in self.text_records:
            x, y = self.text_rect_coords[element]
            if list(self.text_records.keys()).index(element) == self.selected_option:
                surface = self.body_font.render(self.text_names[element], self.antialiasing, palette["title_highlight"])
            else:
                surface = self.text_records[element]
            self.screen.blit(surface, (x, y))


    def update(self):
        '''Animations?'''
        # TODO: Add animations
        
        pass

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.input_manager.binds["up"]:
                if self.selected_option > 1:
                    self.selected_option -= 1
            elif event.key == self.input_manager.binds["down"]:
                if self.selected_option < (len(self.text_records) - 1):
                    self.selected_option += 1
            elif event.key == self.input_manager.binds["enter"]:
                match self.selected_option:
                    case 1:
                        self._play()
                    case 2:
                        self._newGame()
                    case 3:
                        self._changeKeybinds()
                    case 4:
                        self._quit()

    def _play(self):
        self.scene_change_callback("world")

    def _newGame(self):
        # TODO: Overwrite Save
        self.scene_change_callback("world")
        print("Not Yet Implemented")

    def _changeKeybinds(self):
        # TODO: Implement Change Keybinds
        print("Not Yet Implemented")

    def _quit(self):
        # TODO: Add save function
        quit()