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

    def input(self):
        user_input = input()
        self.inputs = user_input.split()
  
    def check_words(self):
        d = difflib.Differ()
        def nm(words):
            return [re.sub(r'[^\w\s]', '', word.lower()) for word in words]
        diffs = d.compare(nm(self.words[self.words_index:]), nm(self.inputs))
        
        correct = True
        for diff in diffs:
            status = diff[0]  # 差分のステータス（' ', '-', '+' のいずれか）
            word = [diff[2:], ' ']   # 実際の単語

            if status == '-':  # inputにだけ存在する単語
                correct = False
                word = [word, '-']
            elif status == '+':  # wordsにだけ存在する単語
                correct = False
                word = ["*", '+']

            self.result.append(word)
        if correct:
            self.words_index = len(self.inputs)
            if self.words_index > len(self.words) - 1:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            
        