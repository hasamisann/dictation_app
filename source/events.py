import pygame
from source.audio_engine import AudioEngine

class EventHandler:
    def __init__(self, audio_engine, gui):
        self.audio_engine = audio_engine
        self.gui = gui
        self.loop_mode = False
        self.paused = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.VIDEORESIZE:
                self.gui.screen_width, self.gui.screen_height = event.size
                self.gui.bar_width, self.gui.bar_height, self.gui.bar_x, self.gui.bar_y = self.gui.update_display_param()

            elif event.type == AudioEngine.AUDIO_END_EVENT:
                print("audio_end")
                if self.loop_mode:
                    self.audio_engine.index = len(self.audio_engine.cue_list) - 1
                    self.audio_engine.skip_to_index(self.audio_engine.index)
                else:
                    self.audio_engine.start_time = 0
                    self.audio_engine.index = 0

            elif event.type == AudioEngine.LOOP_POINT_EVENT:
                print("loop_point")
                current_time = self.audio_engine.get_current_time()
                self.audio_engine.index = self.audio_engine.find_index(self.audio_engine.cue_list, current_time)
                if self.loop_mode:
                    self.audio_engine.skip_to_index(self.audio_engine.index - 1)

            elif event.type == pygame.KEYDOWN:
                current_time = self.audio_engine.get_current_time()
                index = self.audio_engine.find_index(self.audio_engine.cue_list, current_time)

                if event.key == pygame.K_UP:
                    print("up")
                    self.audio_engine.skip_to_index(index)
                elif event.key == pygame.K_RIGHT:
                    print("right")
                    self.audio_engine.skip_to_index(index + 1)
                elif event.key == pygame.K_LEFT:
                    print("reft")
                    self.audio_engine.skip_to_index(index - 1)
                elif event.key == pygame.K_SPACE:
                    print("space")
                    self.paused = self.audio_engine.toggle_audio_pause(self.paused)
                elif event.key == pygame.K_l:
                    self.loop_mode = not self.loop_mode
                    print("loop", self.loop_mode)

        return True
