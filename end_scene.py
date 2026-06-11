import pygame

from abstract_classes import scene
from data_managers import inputManager
from constants import palette, fonts, WIDTH, HEIGHT


class end(scene):
    def __init__(self, changescene, status: bool):
        self.status = status
        self.count = 0
        self.input_manager = inputManager()
        self.screen = pygame.display.get_surface()
        self.title_font = pygame.font.Font(fonts["title_body"], 96)
        self.small_title_font = pygame.font.Font(fonts["title_body"], 48)

    def update(self):
        return super().update()
    
    def display(self):
        self.screen.fill(palette["black"])
        if self.status:
            self.screen.blit(pygame.font.Font.render(self.title_font, "You WON!", False, palette["title_highlight"]), (WIDTH//4, HEIGHT//2), )
        else:
            if self.count < 5:
                self.screen.blit(pygame.font.Font.render(self.title_font, "You Failed", False, palette["title_highlight"]), (WIDTH//4, HEIGHT//2))
            else:
                self.screen.blit(pygame.font.Font.render(self.small_title_font, "Maybe the real treasure was the friends we made along the way.", False, palette["title_highlight"]), (WIDTH//8, HEIGHT//2))
    
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.input_manager.retrieve("enter"):
                self.count += 1