import pygame
from engine import Engine

class EventHandler:
    def __init__(self, engine, gui):
        self.engine = engine
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

            elif event.type == Engine.AUDIO_END_EVENT:
                print("audio_end")
                if self.loop_mode:
                    self.engine.index = len(self.engine.cue_list) - 1
                    self.engine.skip_to_index(self.engine.index)
                else:
                    self.engine.start_time = 0
                    self.engine.index = 0

            elif event.type == Engine.LOOP_POINT_EVENT:
                print("loop_point")
                current_time = self.engine.get_current_time()
                self.engine.index = self.engine.find_index(self.engine.cue_list, current_time)
                if self.loop_mode:
                    self.engine.skip_to_index(self.engine.index - 1)

            elif event.type == pygame.KEYDOWN:
                current_time = self.engine.get_current_time()
                index = self.engine.find_index(self.engine.cue_list, current_time)

                if event.key == pygame.K_UP:
                    self.engine.skip_to_index(index)
                elif event.key == pygame.K_RIGHT:
                    self.engine.skip_to_index(index + 1)
                elif event.key == pygame.K_LEFT:
                    self.engine.skip_to_index(index - 1)
                elif event.key == pygame.K_SPACE:
                    self.paused = self.engine.toggle_audio_pause(self.paused)

                elif event.key == pygame.K_l: # loop
                    self.loop_mode = not self.loop_mode

                elif event.key == pygame.K_i: # insert cue
                    self.engine.insert_cue(current_time)

                elif event.key == pygame.K_d: # delete cue
                    self.engine.delete_cue(index)
                    self.engine.index = self.engine.find_index(self.engine.cue_list, current_time)

        return True
