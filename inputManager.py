import json

import pygame

class inputManager:
    _instance = None

    bindStore: str
    binds: dict

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        cls._instance.bindStore = "Save Data/bindStore.json"
        cls._instance.binds = {
            "up": pygame.K_w,
            "down": pygame.K_s,
            "left": pygame.K_a,
            "right": pygame.K_d,
            "quit": pygame.K_q,
        }

        cls._instance.binds.update(cls._instance._load())

        return cls._instance

    def _load(self):
        try:
            with open(self.bindStore, "r") as bindStore:
                bindData = json.load(bindStore)
                return bindData
        except json.JSONDecodeError:
            with open(self.bindStore, "w") as bindStore:
                json.dump(self.binds, bindStore)
                return self.binds
        
    def temp(self, action, key):
        self.binds.update({action: key})
        with open(self.bindStore, "w") as saveFile:
            json.dump(self.binds, saveFile)
    

        
testmanager = inputManager()
print(testmanager.binds)
testmanager.temp("sus", 6767676767)
print(testmanager.binds)
