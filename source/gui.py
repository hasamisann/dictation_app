import pygame

class GUI:
    def __init__(self, settings, audio_engine):
        pygame.init()
        self.settings = settings
        self.audio_engine = audio_engine
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

        current_time = self.audio_engine.get_current_time()

        # Draw seek bar
        pygame.draw.rect(self.screen, (200, 200, 200), (self.bar_x, self.bar_y, self.bar_width, self.bar_height))
        played_width = (current_time / self.audio_engine.sound_length) * self.bar_width
        pygame.draw.rect(self.screen, (80, 80, 80), (self.bar_x, self.bar_y, played_width, self.bar_height))

        # Draw cue markers
        for t in self.audio_engine.cue_list:
            triangle_x = self.bar_x + (t / self.audio_engine.sound_length) * self.bar_width
            pygame.draw.polygon(self.screen, (100, 100, 100), [
                (triangle_x - 5, self.bar_y - 5),
                (triangle_x, self.bar_y),
                (triangle_x + 5, self.bar_y - 5)
            ])

        pygame.time.Clock().tick(30)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
