from settings import Settings
from engine import Engine
from gui import GUI
from events import EventHandler
from script import Script
import pygame

DEFAULT_SCREEN_WIDTH = 1280
DEFAULT_SCREEN_HEIGHT = 720
PATH_FILE_NAME = "file_path.txt"
FPS = 30

def main():
    settings = Settings(default_screen_width = DEFAULT_SCREEN_WIDTH, default_screen_height = DEFAULT_SCREEN_HEIGHT, path_file_name = PATH_FILE_NAME)
    engine = Engine(settings.audio_file_path, settings.script_file_path)
    script = Script(settings.script_file_path)

    if not engine.load_cue():
        engine.set_cue_by_sentences_with_whisper(model_weight="medium")
        engine.save_cue()

    gui = GUI(settings, engine, script)
    event_handler = EventHandler(engine, gui, script)

    engine.play()
    engine.toggle_audio_pause(False)

    running = True
    while running:
        running = event_handler.handle_events()
        gui.update_display()
        engine.monitor_loop_point()
        pygame.time.Clock().tick(FPS)
    engine.quit()
    gui.quit()

if __name__ == "__main__":
    main()
