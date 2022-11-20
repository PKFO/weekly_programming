import pygame
import sys

start_width = 200
start_Height = 50
rank_image_width = 100
rank_image_Height = 80
rank = []
image = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/UI/START .png'), (start_width, start_Height))
rank_image = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/UI/ranking.png'), (rank_image_width, rank_image_Height))
class Menu():
    def __init__(self, game):
        self.game = game
        self.img = image
        self.rank_img =  rank_image
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 120

    def draw(self):
        self.game.window.blit(self.image,(self.rect.x,self.rect.y))

   
    def draw_cursor(self):
        self.game.draw_text('*', 30, self.cursor_rect.x - 50, self.cursor_rect.y + 50)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        if self.game.main_menu.show_start:
            self.game.window.blit(self.img,(self.mid_w - 100,self.mid_h + 60))
            self.game.window.blit(self.rank_img,(self.mid_w- 62,self.mid_h + 150))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.show_start = True
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    def draw(self):
        self.game.window.blit(self.image,(self.rect.x,self.rect.y))

    def display_menu(self):
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Perawat kosit 65010768',20,220,20)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset + 50, self.optionsy + 90)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            
        elif self.game.UP_KEY:
            if self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset + 50, self.optionsy + 90)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.run_display = False
                self.running = True
            elif self.state == 'Options':
                self.show_start = False
                self.game.options.display_menu()
            elif self.state == 'Credits':
                self.show_start = False
                self.game.credits.display_menu()
    def run(self):
        self.display_menu() 
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        self.load_file()
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text("No1 " + str(rank[4]) , 50, self.volx, self.voly - 200)
            self.game.draw_text("No2 "+ str(rank[3]), 50, self.volx, self.voly - 100)
            self.game.draw_text("No3 "+str(rank[2]), 50, self.volx, self.voly) 
            self.game.draw_text("No4 " + str(rank[1]), 50, self.volx, self.voly+ 100)  
            self.game.draw_text("No5 "+str(rank[0]), 50, self.volx, self.voly+ 200)   
            self.draw_cursor()
            self.blit_screen()
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass
    def add_data(self,data):
        rank.append(data)
        rank.sort()
        rank.pop(0)
    def load_file(self):
        f = open("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/code/score.txt",'r') 
        rank.append(int(f.readline()))
        rank.append(int(f.readline()))
        rank.append(int(f.readline()))
        rank.append(int(f.readline()))
        rank.append(int(f.readline()))
        f.close()
    def save_file(self):
        f = open("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/code/score.txt",'w')   
        for score in rank:
            f.write(str(score) + "\n")
        f.close()

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

