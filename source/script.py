import re
import difflib
import pygame

class Script:
    def __init__(self, script_file_path):
        self.words = []
        with open(script_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                self.words.extend(line.strip().split())
        self.inputs = []
        self.result = []
        self.words_index = 0

    def input(self, str):
        self.inputs = str.split()
  
    def check_words(self):
        self.result = []
        d = difflib.Differ()
        def nm(words):
            return [re.sub(r'[^\w\s]', '', word.lower()) for word in words]
        self.inputs = nm(self.inputs)
        diffs = d.compare(nm(self.words[self.words_index:]), nm(self.inputs))

        correct = True
        index = 0 
        for diff in diffs:
            if index == len(self.inputs):
                break
            status = diff[0]  # diff status（' ', '-', '+'）
            word = [diff[2:], ' ']
            index += 1

            if status == '-':
                index -= 1
                correct = False
                word = ['*', '-']
            elif status == '+':
                correct = False
                word = [word[0], '+']

            self.result.append(word)
        if correct:
            self.words_index += len(self.inputs)
            if self.words_index > len(self.words) - 1:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            
        