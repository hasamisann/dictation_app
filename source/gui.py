import pygame

class GUI:
    def __init__(self, settings, engine):
        pygame.init()
        self.settings = settings
        self.engine = engine
        self.screen_width = settings.default_screen_width
        self.screen_height = settings.default_screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.running = True
        self.bar_width, self.bar_height, self.bar_x, self.bar_y = self.update_display_param()

    def update_display_param(self):
        bar_width = self.screen_width - 100
        bar_height = 10
        bar_x = self.screen_width / 2 - bar_width / 2
        bar_y = self.screen_height - 30
        return bar_width, bar_height, bar_x, bar_y

    def update_display(self):
        self.screen.fill((255, 255, 255))

        current_time = self.engine.get_current_time()

        # Draw seek bar
        pygame.draw.rect(self.screen, (200, 200, 200), (self.bar_x, self.bar_y, self.bar_width, self.bar_height))
        played_width = (current_time / self.engine.sound_length) * self.bar_width
        pygame.draw.rect(self.screen, (110, 110, 110), (self.bar_x, self.bar_y, played_width, self.bar_height))

        # Draw cue markers
        for i, cue in enumerate(self.engine.cue_list):
            cue = self.engine.cue_list[i]
            color = (90, 90, 90)
            if i == self.engine.index:
                color = (37, 176, 243)
            triangle_x = self.bar_x + (cue / self.engine.sound_length) * self.bar_width
            pygame.draw.polygon(self.screen, color, [
                (triangle_x - 5, self.bar_y - 6),
                (triangle_x, self.bar_y - 1),
                (triangle_x + 5, self.bar_y - 6)
            ])
        pygame.display.flip()

    def quit(self):
        pygame.quit()
