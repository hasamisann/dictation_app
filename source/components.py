import pygame

class SeekBar:
    def __init__(self, engine):
        pygame.init()
        self.engine = engine
        y = 0

    def draw(self, screen, screen_width, screen_height):
        current_time = self.engine.get_current_time()

        width = screen_width - 100
        height = 10
        x = screen_width / 2 - width / 2
        y = screen_height - 30

        # Draw seek bar
        pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height))
        played_width = (current_time / self.engine.sound_length) * width
        pygame.draw.rect(screen, (110, 110, 110), (x, y, played_width, height))

        # Draw cue markers
        for i, cue in enumerate(self.engine.cue_list):
            color = (90, 90, 90)
            if i == self.engine.index:
                color = (37, 176, 243)
            triangle_x = x + (cue / self.engine.sound_length) * width
            pygame.draw.polygon(screen, color, [
                (triangle_x - 5, y - 6),
                (triangle_x, y - 1),
                (triangle_x + 5, y - 6)
            ])

class Button:
    def __init__(self, offset, text, text_color, width, height):
        self.offset = offset
        self.color = (200, 200, 200)
        self.text = text
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.width = width
        self.height = height
        self.rect = None
    
    def draw(self, screen, screen_width, screen_height):
        self.rect = pygame.Rect(screen_width // 2 + self.offset - self.width // 2, screen_height - self.height - 60, self.width, self.height)
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, tuple(x - 50 for x in self.color), self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Toggle:
    def __init__(self, offset, text, text_color, width, height):
        self.offset = offset
        self.rect = None
        self.color = (200, 200, 200)
        self.color_ON = (100, 250, 50)
        self.color_OFF = (150, 150, 150)
        self.text = text
        self.font = pygame.font.SysFont(None, 30)
        self.text_color = text_color
        self.width = width
        self.height = height
        self.isON = False

    def draw(self, screen, screen_width, screen_height):
        self.rect = pygame.Rect(screen_width // 2 + self.offset - self.width // 2, screen_height - self.height - 60, self.width, self.height)
        if(self.isON):
            left_rect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width // 3 * 2, self.rect.height)
            right_rect = pygame.Rect(self.rect.left + self.rect.width // 3 * 2, self.rect.top, self.rect.width // 3, self.rect.height)
            pygame.draw.rect(screen, self.color_ON, left_rect)
            pygame.draw.rect(screen, self.color, right_rect)
        else:
            left_rect = pygame.Rect(self.rect.left, self.rect.top, self.rect.width // 3, self.rect.height)
            right_rect = pygame.Rect(self.rect.left + self.rect.width // 3, self.rect.top, self.rect.width // 3 * 2, self.rect.height)
            pygame.draw.rect(screen, self.color, left_rect)
            pygame.draw.rect(screen, self.color_OFF, right_rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.isON = not self.isON
                return True
        return False
        
            


            
        


        


        
