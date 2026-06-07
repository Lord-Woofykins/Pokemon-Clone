import json

import pygame

class inputManager:
    _instance = None

    bind_store: str
    binds: dict

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        cls._instance.bind_store = "save_data/bind_store.json"
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
            with open(self.bind_store, "r") as bind_store:
                bindData = json.load(bind_store)
                return bindData
        except json.JSONDecodeError:
            with open(self.bind_store, "w") as bind_store:
                json.dump(self.binds, bind_store)
                return self.binds
        
    def temp(self, action, key):
        self.binds.update({action: key})
        with open(self.bind_store, "w") as save_file:
            json.dump(self.binds, save_file)
    

        
testmanager = inputManager()
print(testmanager.binds)
testmanager.temp("sus", 6767676767)
print(testmanager.binds)
