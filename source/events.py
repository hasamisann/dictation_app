import pygame
from engine import Engine

class EventHandler:
    def __init__(self, engine, gui, script):
        self.engine = engine
        self.script = script
        self.loop_mode = False
        self.paused = True
        self.gui = gui

    def handle_events(self):
        events = pygame.event.get()

        self.gui.textinput.update(events)

        for event in events:
            current_time = self.engine.get_current_time()
            index = self.engine.find_index(self.engine.cue_list, current_time)

            if event.type == pygame.QUIT:
                return False

            elif event.type == Engine.AUDIO_END_EVENT:
                if self.loop_mode:
                    self.engine.index = len(self.engine.cue_list) - 1
                    self.engine.skip_to_index(self.engine.index)
                else:
                    self.engine.start_time = 0
                    self.engine.index = 0
                    self.engine.play()

            elif event.type == Engine.LOOP_POINT_EVENT:
                current_time = self.engine.get_current_time()
                self.engine.index = self.engine.find_index(self.engine.cue_list, current_time)
                if self.loop_mode:
                    self.engine.skip_to_index(self.engine.index - 1)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.script.input(self.gui.textinput.value)
                    self.script.check_words()
                    self.gui.output_result()
                    self.gui.textinput_initialize()
                    self.script.inputs = []

            elif self.gui.buttons['back'].clicked(event):
                self.engine.skip_to_index(index - 1)

            elif self.gui.buttons['pause'].clicked(event):
                self.paused = self.engine.toggle_audio_pause(self.paused)
            
            elif self.gui.buttons['replay'].clicked(event):
                    self.engine.skip_to_index(index)

            elif self.gui.buttons['skip'].clicked(event):
                self.engine.skip_to_index(index + 1)

            elif self.gui.buttons['insert'].clicked(event):
                self.engine.insert_cue(current_time)

            elif self.gui.buttons['delete'].clicked(event):
                self.engine.delete_cue(index)
                self.engine.index = self.engine.find_index(self.engine.cue_list, current_time)
            
            elif self.gui.buttons['save'].clicked(event):
                self.engine.save_cue()
                

            elif self.gui.toggles['loop'].clicked(event):
                self.loop_mode = not self.loop_mode

        return True
