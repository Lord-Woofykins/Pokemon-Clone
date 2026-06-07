from abc import ABC, abstractmethod


class scene(ABC):
    """An abstract base class to define the standardised components of all scenes to interact with the game runner."""

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def handleEvent(self, event):
        pass
