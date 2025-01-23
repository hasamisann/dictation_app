from components import SeekBar, Button, Toggle
import pygame
import pygame_textinput

class GUI:
    def __init__(self, settings, engine, script):
        pygame.init()
        self.settings = settings
        self.engine = engine
        self.script = script
        self.screen = pygame.display.set_mode((settings.default_screen_width, settings.default_screen_height), pygame.RESIZABLE)
        self.seekbar = SeekBar(self.engine)
        self.buttons = {
            "skip": Button(50, ">>", (50, 50, 50), 40, 40),
            "pause": Button(0, "P", (50, 50, 50,), 40, 40),
            "back": Button(-100, "<<", (50, 50, 50,), 40, 40),
            "replay": Button(-50, "|<", (50, 50, 50), 40, 40),
            "insert": Button(-200, "I", (50, 50, 50), 40, 40),
            "delete": Button(-250, "D", (50, 50, 50), 40, 40),
            "save": Button(250, "S", (50, 50, 50), 40, 40)
        }
        self.toggles = {
            "loop": Toggle(150, "L", (50, 50, 50), 66, 40)
        }
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.running = True

    def textinput_initialize(self):
        self.textinput = pygame_textinput.TextInputVisualizer(font_object = pygame.font.Font(None, 35))

    def output_result(self):
        font = pygame.font.Font(None, 35)
        y = 100
        max_width = self.screen.get_width() - 20
        max_height = self.screen.get_height()

        space_width, _ = font.size(" ")
        x = 20
        line = []

        for res in self.script.result:
            line.append(res)
            line_width, line_height = font.size(" ".join([word[0] for word in line]))
            if line_width > max_width:
                x = 20
                for word in line[:-1]:
                    word_width, _ = font.size(word[0] + " ")
                    color = (0, 0, 0)
                    if word[1] == '-':
                        color = (0, 200, 200)
                    elif word[1] == '+':
                        color = (255, 50, 50)
                    self.screen.blit(font.render(word[0] + ' ', True, color), (x, y))
                    x += word_width
                line = [line[-1]]
                y += line_height + 10

        if line:
            x = 20
            line_width, line_height = font.size(" ".join([word[0] for word in line]))
            for word in line:
                word_width, _ = font.size(word[0] + " ")
                color = (0, 0, 0)
                if word[1] == '-':
                    color = (0, 200, 200)
                elif word[1] == '+':
                    color = (255, 50, 50)
                self.screen.blit(font.render(word[0] + ' ', True, color), (x, y))
                x += word_width
                    

    def update_display(self):
        self.screen.fill((255, 255, 255))

        self.seekbar.draw(self.screen, self.screen.get_width(), self.screen.get_height())

        for button in self.buttons.values():
            button.draw(self.screen, self.screen.get_width(), self.screen.get_height())

        for toggle in self.toggles.values():
            toggle.draw(self.screen, self.screen.get_width(), self.screen.get_height())

        self.screen.blit(self.textinput.surface, (20, 20))

        self.output_result()

        pygame.display.flip()

    def quit(self):
        pygame.quit()
