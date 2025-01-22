import pygame
from game.scenes import SceneManager

class GameEngine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = SceneManager(self.screen)

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._render()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scene_manager.handle_event(event)

    def _update(self):
        self.scene_manager.update()

    def _render(self):
        self.scene_manager.render()
        pygame.display.flip()
        self.clock.tick(60)
