from settings import Settings
from engine import Engine
from gui import GUI
from events import EventHandler
import pygame

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
PATH_FILE_NAME = "file_path.txt"
FPS = 30

def main():
    settings = Settings(default_screen_width = DEFAULT_SCREEN_WIDTH, default_screen_height = DEFAULT_SCREEN_HEIGHT, path_file_name = PATH_FILE_NAME)
    engine = Engine(settings.audio_file_path)
    gui = GUI(settings, engine)
    event_handler = EventHandler(engine, gui)

    running = True
    while running:
        running = event_handler.handle_events()
        gui.update_display()
        engine.monitor_loop_point()
        pygame.time.Clock().tick(60)
    engine.quit()
    gui.quit()

if __name__ == "__main__":
    main()
