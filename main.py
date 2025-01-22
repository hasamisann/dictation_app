from settings import Settings
from source.engine import AudioEngine
from source.gui import GUI

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

def main():
    settings = Settings(screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT,file_path="/mnt/c/Users/nalum/Music/TOXIC_VISIONS/Seventhrun_Zootoxin.mp3")
    audio_engine = AudioEngine(settings.file_path)
    gui = GUI(settings, audio_engine)

    running = True
    while running:
        running = gui.handle_events()
        gui.update_display()

    audio_engine.quit()
    gui.quit()

if __name__ == "__main__":
    main()
