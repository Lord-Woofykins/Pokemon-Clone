from abc import ABC, abstractmethod

from Constants import WIDTH

class scene(ABC):
    @abstractmethod
    def update(self):
        pass
    def display(self):
        pass