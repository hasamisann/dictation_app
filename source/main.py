from settings import Settings
from engine import AudioEngine
from gui import GUI
from events import EventHandler

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
PATH_FILE_NAME = "file_path.txt"
FPS = 30

def main():
    settings = Settings(default_screen_width = DEFAULT_SCREEN_WIDTH, default_screen_height = DEFAULT_SCREEN_HEIGHT, path_file_name = PATH_FILE_NAME)
    audio_engine = AudioEngine(settings.audio_file_path)
    gui = GUI(settings, audio_engine)
    event_handler = EventHandler(audio_engine, gui)

    running = True
    while running:
        running = event_handler.handle_events()
        gui.update_display()

    audio_engine.quit()
    gui.quit()

if __name__ == "__main__":
    main()
