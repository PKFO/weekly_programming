import pygame
import sys
from menu import *

start_width = 300
start_Height = 100
boss_death_count = 0
score = 0
game_over = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/UI/GAME_OVER.png'),(start_width ,start_Height))

class Game():
    def __init__(self):
        pygame.init()
        self.img = game_over
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 900, 1000
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/code/8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
    
    def updateScore(self,data):
        self.score = data
    def game_loop(self):
        global player_health
        game_over = True
        pygame.mixer.music.stop()
        pygame.mixer.Channel(3).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/game_over.wav'))
        self.options.load_file()
        self.options.add_data(self.score)
        self.options.save_file()
        while game_over:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0,0))
            self.window.blit(self.img,(self.DISPLAY_W/2 - 150,self.DISPLAY_H/2))
            self.running = False
            pygame.display.update()
            self.reset_keys()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                    self.main_menu.show_start = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    def win(self):
        global boss_death_count
        boss_death_count += 1
        if boss_death_count + 1 >= 150:
            boss_death_count = 0
        win = True
        pygame.mixer.music.stop()
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/victory_end.wav'))
        while win:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.draw_text('YOU WIN', 35, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)