from abstract_classes import scene

class player():
    def __init__(self):
        pass

class gameWorld(scene):
    def __init__(self, change_scene):
        super().__init__(change_scene)
        print("HEE HEE")
        self.scene_change_callback("titleScreen")

        self.current_map = "town"
        

    
    def update(self):
        pass

    def display(self):
        pass

    def handleEvent(self, event):
        pass