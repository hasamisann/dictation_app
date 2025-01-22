import pygame
from source.engine import AudioEngine

class GUI:
    def __init__(self, settings, audio_engine):
        pygame.init()
        self.settings = settings
        self.audio_engine = audio_engine
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Audio Player")
        self.running = True
        self.bar_width, self.bar_height, self.bar_x, self.bar_y = self.update_display_param()

    def update_display_param(self):
        bar_width = self.settings.screen_width - 100
        bar_height = 10
        bar_x = self.settings.screen_width / 2 - bar_width / 2
        bar_y = self.settings.screen_height - 30
        return bar_width, bar_height, bar_x, bar_y

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE:
                self.settings.screen_width, self.settings.screen_height = event.size
                self.bar_width, self.bar_height, self.bar_x, self.bar_y = self.update_display_param()
            elif event.type == AudioEngine.MUSIC_END_EVENT:
                self.audio_engine.start_time = 0
                self.audio_engine.index = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.audio_engine.play()
                elif event.key == pygame.K_RIGHT:
                    self.audio_engine.skip_to_index(self.audio_engine.index + 1)
                elif event.key == pygame.K_LEFT:
                    self.audio_engine.skip_to_index(self.audio_engine.index - 1)

        return True

    def update_display(self):
        self.screen.fill((255, 255, 255))
        current_time = self.audio_engine.get_current_time()
        self.audio_engine.index = self.find_largest_under_limit(self.audio_engine.time_list, current_time)

        # Draw seek bar
        pygame.draw.rect(self.screen, (200, 200, 200), (self.bar_x, self.bar_y, self.bar_width, self.bar_height))
        played_width = (current_time / self.audio_engine.sound_length) * self.bar_width
        pygame.draw.rect(self.screen, (80, 80, 80), (self.bar_x, self.bar_y, played_width, self.bar_height))

        # Draw time markers
        for t in self.audio_engine.time_list:
            if t <= self.audio_engine.sound_length:
                triangle_x = self.bar_x + (t / self.audio_engine.sound_length) * self.bar_width
                pygame.draw.polygon(self.screen, (100, 100, 100), [
                    (triangle_x - 5, self.bar_y - 5),
                    (triangle_x, self.bar_y),
                    (triangle_x + 5, self.bar_y - 5)
                ])

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    @staticmethod
    def find_largest_under_limit(lst, target):
        best_index = -1
        best_value = -float('inf')
        for index, value in enumerate(lst):
            if value <= target and value > best_value:
                best_value = value
                best_index = index
        return best_index

    def quit(self):
        pygame.quit()
