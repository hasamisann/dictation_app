from components import SeekBar, Button, Toggle
import pygame

class GUI:
    def __init__(self, settings, engine, script):
        pygame.init()
        self.settings = settings
        self.engine = engine
        #self.script = script
        self.screen = pygame.display.set_mode((settings.default_screen_width, settings.default_screen_height), pygame.RESIZABLE)
        self.seekbar = SeekBar(self.engine)
        self.buttons = {
            "skip": Button(50, ">>", (50, 50, 50), 40, 40),
            "pause": Button(0, "P", (50, 50, 50,), 40, 40),
            "back": Button(-100, "<<", (50, 50, 50,), 40, 40),
            "replay": Button(-50, "|<", (50, 50, 50), 40, 40)
        }
        self.toggles = {
            "loop": Toggle(150, "L", (50, 50, 50), 66, 40)
        }
        self.running = True

    def update_display(self):
        self.screen.fill((255, 255, 255))

        self.seekbar.draw(self.screen, self.screen.get_width(), self.screen.get_height())

        for button in self.buttons.values():
            button.draw(self.screen, self.screen.get_width(), self.screen.get_height())

        for toggle in self.toggles.values():
            toggle.draw(self.screen, self.screen.get_width(), self.screen.get_height())

        pygame.display.flip()

    def quit(self):
        pygame.quit()
