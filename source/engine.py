import pygame
from mutagen.mp3 import MP3
import bisect
import whisper
import re
import json
import os
from pathlib import Path

class Engine:
    AUDIO_END_EVENT = pygame.USEREVENT + 1
    LOOP_POINT_EVENT = pygame.USEREVENT + 2

    def __init__(self, audio_file_path, script_file_path):
        pygame.mixer.init()
        self.audio_file_path = audio_file_path
        self.script_file_path = script_file_path
        self.sound_length = MP3(audio_file_path).info.length
        self.cue_list = [float(i) + 0.2 for i in range(0, int(self.sound_length), 5)]
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
    
    def save_cue(self):
        dir = 'data'
        os.makedirs(dir, exist_ok=True)
        file_name = Path(self.script_file_path).stem + '.json'
        file_path = Path(dir) / file_name              
        with open(file_path, 'w') as f:
            json.dump(self.cue_list, f)
    
    def load_cue(self):
        file_name = Path(self.script_file_path).stem + '.json'
        file_path = Path('data') / file_name 
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.cue_list = json.load(f)
            return True
        else:
            return False
    
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

    def set_cue_by_sentences_with_whisper(self, model_weight): 
        def normalize_text(text):
            text = text.lower()
            text = re.sub(r'[^\w\s]', '', text)  # 句読点を削除
            return text
        
        def match_sentence(str1, str2):
            print(str1)
            print(str2)
            words1 = str1.split()
            words2 = str2.split()
            for word1, word2 in zip(words1, words2):
                if word1 != word2:
                    return False
            return True

        # スクリプトを読み込み
        with open(self.script_file_path, 'r', encoding='utf-8') as f:
            sentences = [line.strip() for line in f if line.strip()]

        # スクリプト文を正規化
        normalized_sentences = [normalize_text(sentence) for sentence in sentences]

        # Whisperモデルの読み込み
        model = whisper.load_model(model_weight)

        # 音声ファイルの認識
        result = model.transcribe(self.audio_file_path)

        # 各スクリプト文に対して最適なタイムスタンプを取得
        timestamps = []
        index = 0
        for normalized_sentence in normalized_sentences:
            for i in range(index, len(result['segments'])):
                segment = result['segments'][i]
                start_time = segment['start']
                segment_text = normalize_text(segment['text'])

                if match_sentence(normalized_sentence, segment_text):
                    timestamps.append(start_time)
                    index = i + 1
                    break

        print(timestamps)

        self.cue_list = timestamps

    def quit(self):
        pygame.mixer.quit()
