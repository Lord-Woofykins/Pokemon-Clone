import pygame
import random
import math

from abstract_classes import scene
from data_managers import saveManager, inputManager
from monsters import sparkie, hydragon, ember
from constants import WIDTH, HEIGHT, palette, images


class battle(scene):
    def __init__(self, change_scene):
        # External references
        self.change_scene_callback = change_scene
        self.screen = pygame.display.get_surface()

        self.save_manager = saveManager()
        self.input_manager = inputManager()

        # Box Constants
        self.corner_rounding = 10

        # Rect objects for options, health bar and monsters
        self.option_rect = pygame.rect.Rect(WIDTH//2 + 50, HEIGHT//2 + 150, WIDTH//3, HEIGHT//4)

        # Health rects
        self.player_health_rect = pygame.Rect(50, HEIGHT - 100, 100, 25)

        self.opponent_health_rect = pygame.Rect(20, 20, 320, 60)

        # Monster rects
        self.player_monster_rect = pygame.Rect(150, HEIGHT//2 + 150, 75, 75)

        self.opponent_monster_rect = pygame.Rect(WIDTH//2 + 100, 50, 75, 75)

        # Move menu (bottom)
        self.menu_rect = pygame.Rect(20, 470, WIDTH - 40, 120)

        # Battle Setup
        self.monsters = [sparkie, hydragon, ember]
        self._player_monster, self._opponent_monster = self._pickMonsters()

        # Instantiating chosen classes
        self._player_monster = self._player_monster()
        self._opponent_monster = self._opponent_monster()

        # Fonts
        self.font = pygame.font.SysFont("Arial", 16)
        self.instructions = [
            "Press 1 to attack."
            "Press 2 to heal."
            "Press 3 to flee."
        ]

    def update(self):
        if self._player_monster.health <= 0:
            self.change_scene_callback("end", False)
        elif self._opponent_monster.health <= 0:
            self.change_scene_callback("end", True)

    def display(self):
        self.screen.fill(palette["white"])
        self._drawMonsters()
        self._drawOptions()
        self._drawHealthBars()

    def _drawOptions(self):
        pygame.draw.rect(
            self.screen,
            palette["title_highlight"],
            self.option_rect,
            border_radius=self.corner_rounding,
        )
        pygame.draw.rect(
            self.screen,
            palette["black"],
            self.option_rect,
            width=2,
            border_radius=self.corner_rounding
        )

        y = self.option_rect.y + 6
        for line in self.instructions:
            surf = self.font.render(line, True, palette["black"])
            self.screen.blit(surf, (self.option_rect.x + 10, y))
            y += 18

    def _drawHealthBars(self):
        try:
            player_colour = palette[f"health_bar_{math.floor((self._player_monster.health / self._player_monster.max_health) * 30)}"]
            opponent_colour = palette[f"health_bar_{math.floor((self._opponent_monster.health / self._opponent_monster.max_health) * 30)}"]

            # Draw Player Health Bar
            pygame.draw.rect(
                self.screen,
                player_colour,
                self.player_health_rect,
                border_radius=self.corner_rounding,
            )
            pygame.draw.rect(
                self.screen,
                palette["black"],
                self.player_health_rect,
                width=2,
                border_radius=self.corner_rounding
            )

            # Draw Opponent Health Bar
            pygame.draw.rect(
                self.screen,
                opponent_colour,
                self.opponent_health_rect,
                border_radius=self.corner_rounding,
            )
            pygame.draw.rect(
                self.screen,
                palette["black"],
                self.opponent_health_rect,
                width=2,
                border_radius=self.corner_rounding
            )

        except KeyError:
            self.update()

    def _drawMonsters(self):
        player_monster_image = pygame.transform.scale(pygame.image.load(images[self._player_monster.name]).convert_alpha(), (225, 225))
        opponent_monster_image = pygame.transform.scale(pygame.image.load(images[self._opponent_monster.name]).convert_alpha(), (225, 225))

        self.screen.blit(player_monster_image, self.player_monster_rect)
        self.screen.blit(opponent_monster_image, self.opponent_monster_rect)

    def _pickMonsters(self):
        player_monster = random.choices(self.monsters, [0.33, 0.33, 0.34])[0]
        possible_opp_monsters = random.choices(self.monsters, [0.33, 0.33, 0.34], k=2)
        opponent_monster = possible_opp_monsters[0] if possible_opp_monsters[0] != player_monster else possible_opp_monsters[1]
        return player_monster, opponent_monster
    
    def _attack(self):
        self._opponent_monster.health -= self._player_monster.damage
        self._player_monster.health -= ((0.5 + random.random()) * self._opponent_monster.damage)

    def _heal(self):
        self._player_monster.health += 40
        self._player_monster.health -= ((0.5 + random.random()) * self._opponent_monster.damage)


    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.input_manager.retrieve("option_1"):
                self._attack()
            elif event.key == self.input_manager.retrieve("option_2"):
                self._heal()
            elif event.key == self.input_manager.retrieve("option_3"):
                self.change_scene_callback("world")
