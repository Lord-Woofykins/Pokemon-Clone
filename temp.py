import pygame
import json

binds = {
    "binds": {
        "up": pygame.K_w,
        "down": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
        "quit": pygame.K_q,
        "curveball": pygame.K_b
    }
}

with open("Save Data/bindStore.json", "w") as saveFile:
    json.dump(binds, saveFile, indent=4)

print(pygame.K_1)