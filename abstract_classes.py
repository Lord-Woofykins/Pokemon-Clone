from abc import ABC, abstractmethod


class scene(ABC):
    """An abstract base class to define the standardised components of all scenes to interact with the game runner."""
    @abstractmethod
    def __init__(self, change_scene):
        self.scene_change_callback = change_scene

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def handleEvent(self, event):
        pass

class monster(ABC):
    @abstractmethod
    def __init__(self, name: str, damage: int, max_health: int):
        self._name = name
        self._damage = damage
        self._max_health = max_health
        self._health = self._max_health

    @property
    def max_health(self):
        return self._max_health

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self._max_health))

    @property
    def damage(self):
        return self._damage
    
    @property
    def name(self):
        return self._name    
    