import pygame
from source.engine import AudioEngine
from source.gui import GUI

class EventHandler:
    def __init__(self, audio_engine, gui):
        self.audio_engine = audio_engine
        self.gui = gui

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.VIDEORESIZE:
                self.gui.screen_width, self.gui.screen_height = event.size
                self.gui.bar_width, self.gui.bar_height, self.gui.bar_x, self.gui.bar_y = self.gui.update_display_param()

            elif event.type == AudioEngine.MUSIC_END_EVENT:
                self.audio_engine.start_time = 0
                self.audio_engine.index = 0

            elif event.type == pygame.KEYDOWN:
                current_time = self.audio_engine.get_current_time()
                index = self.audio_engine.find_index(self.audio_engine.time_list, current_time)
                if event.key == pygame.K_SPACE:
                    self.audio_engine.skip_to_index(index)
                elif event.key == pygame.K_RIGHT:
                    self.audio_engine.skip_to_index(index + 1)
                elif event.key == pygame.K_LEFT:
                    self.audio_engine.skip_to_index(index - 1)

        return True
