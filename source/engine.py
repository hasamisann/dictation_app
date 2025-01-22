import pygame
from mutagen.mp3 import MP3

class AudioEngine:
    MUSIC_END_EVENT = pygame.USEREVENT + 1

    def __init__(self, audio_file_path):
        pygame.mixer.init()
        self.audio_file_path = audio_file_path
        self.sound_length = MP3(audio_file_path).info.length
        self.time_list = [i for i in range(0, int(self.sound_length) + 20, 20)]
        self.index = 0
        self.start_time = 0
        pygame.mixer.music.load(audio_file_path)
        pygame.mixer.music.set_endevent(self.MUSIC_END_EVENT)

    def play(self):
        pygame.mixer.music.play(start=self.start_time)

    def skip_to_index(self, index):
        index = max(0, index)
        index = min(index, len(self.time_list) - 1)
        self.start_time = self.time_list[index]
        pygame.mixer.music.play(start=self.start_time)

    def get_current_time(self):
        if pygame.mixer.music.get_busy():
            return pygame.mixer.music.get_pos() / 1000 + self.start_time
        return 0

    @staticmethod
    def find_index(lst, target):
        best_index = -1
        best_value = -float('inf')
        for index, value in enumerate(lst):
            if value <= target and value > best_value:
                best_value = value
                best_index = index
        return best_index

    def quit(self):
        pygame.mixer.quit()
