import pygame
from mutagen.mp3 import MP3
import bisect

class Engine:
    AUDIO_END_EVENT = pygame.USEREVENT + 1
    LOOP_POINT_EVENT = pygame.USEREVENT + 2

    def __init__(self, audio_file_path):
        pygame.mixer.init()
        self.audio_file_path = audio_file_path
        self.sound_length = MP3(audio_file_path).info.length
        self.cue_list = [float(i) + 0.2 for i in range(0, int(self.sound_length), 10)]
        self.cue_list.append(self.sound_length - 0.1)
        self.index = 0
        self.start_time = 0
        pygame.mixer.music.load(audio_file_path)
        pygame.mixer.music.set_endevent(self.AUDIO_END_EVENT)

    def play(self):
        pygame.mixer.music.play(start=self.start_time)

    def skip_to_index(self, index):
        index = max(0, index)
        index = min(index, len(self.cue_list) - 1)
        self.index = index
        self.start_time = self.cue_list[self.index]
        pygame.mixer.music.play(start=self.start_time)

    def get_current_time(self):
        return pygame.mixer.music.get_pos() / 1000 + self.start_time
    
    def monitor_loop_point(self):
        loop_point = self.cue_list[min(self.index + 1, len(self.cue_list) - 1)]
        if self.get_current_time() > loop_point:
            pygame.event.post(pygame.event.Event(self.LOOP_POINT_EVENT))
    
    def toggle_audio_pause(self, paused):
        if paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        return not paused
    
    def init_cue(self, lst):
        self.cue_list = lst
    
    def insert_cue(self, value):
        bisect.insort(self.cue_list, value)

    def delete_cue(self, index):
        if index < len(self.cue_list) - 1:
            self.cue_list.pop(index)

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
