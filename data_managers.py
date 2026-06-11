"""All Data Management Related Classes Are Contained Here. \n
Such as inputManager and saveManager."""

import json
import pygame

class dataManager:
    """A Parent Class of All Managers of Data"""
    _instances = {}

    data_path: str
    _data: dict

    def __new__(cls):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance

            instance.data_path = ""
            instance._data = {}
        return cls._instances[cls]

    def _load(self):
        try:
            with open(self.data_path, "r") as data_store:
                bindData = json.load(data_store)
                return bindData
        except json.JSONDecodeError:
                self._save()
                return self._data
    
    def _save(self):
        with open(self.data_path, "w") as data_store:
                json.dump(self._data, data_store)
    
    def retrieve(self, key):
         return self._data[key]
    
    def updateData(self, key, value):
            self._data.update({key: value})
            with open(self.data_path, "w") as bind_store:
                json.dump(self._data, bind_store)

class inputManager(dataManager):
    def __init__(self) -> None:
        if hasattr(self, "_initialised"):
               return
        self._initialised = True

        self.data_path = "saves/bind_store.json"
        self._data = {
            "up": pygame.K_w,
            "down": pygame.K_s,
            "left": pygame.K_a,
            "right": pygame.K_d,
            "quit": pygame.K_q,
            "enter": pygame.K_RETURN,
            "option_1": pygame.K_1,
            "option_2": pygame.K_2,
            "option_3": pygame.K_3
            }
        
        self._data.update(self._load())

class saveManager(dataManager):
     def __init__(self) -> None:
        if hasattr(self, "_initialised"):
               return
        self._initialised = True

        self.data_path = "saves/save_file.json"
        self._data = {}
        
        self._data.update(self._load())