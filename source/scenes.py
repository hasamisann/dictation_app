class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        self.current_scene = self.scenes.get(name)

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def render(self):
        if self.current_scene:
            self.current_scene.render()
