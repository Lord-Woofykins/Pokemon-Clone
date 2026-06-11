
from abstract_classes import scene
from data_managers import saveManager

class battle(scene):
    def __init__(self, change_scene):
        # External references
        self.change_scene_callback = change_scene

        self.save_manager = saveManager()

        print("Battle Class Instantiated")
    
    def update(self):
        return super().update()
    
    def display(self):
        return super().display()
    
    def handleEvent(self, event):
        return super().handleEvent(event)