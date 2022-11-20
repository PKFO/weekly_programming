import pygame
import random
import sys
import numpy
from math import sin
from menu import *
from game import *
from item import *
WIDTH = 900
HEIGHT = 1000
FPS = 60


#game constants
player_vel = 35
player_width = 150
player_health = 100
asteroid_width = 100
asteroid_kill_count = 0
scrolling_speed = 5
asteroids = [] #starts out empty and asteroid objects are appended to the list
big_asteroids = []
big_asteroid_health = 5
laser_width = 50
laser_height = 80
laser_vel = 20
enemy_laser_width = 10
enemy_laser_height = 70
laser_delay = 10
aliens = []
lasers = []
items = []
items_2 = []
items_3 = []
laser_count = 0
alien_width = 100
alien_health = 5
alien_vel = 4
boss_width = 500
boss_height = 250
bosses = []
boss_vel = 3
boss_health = 100
boss_spawned = False
boss_death_count = 0
blood_width = 50
vec = pygame.math.Vector2
count = 0
alien_frame_count = 0
item_width = 200
damage = 1
#defining colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
YELLOW = (224, 149, 0)
#loading sprites
background = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/space_background.gif'), (WIDTH, HEIGHT)) #loads and scales image to window size
player = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/player/spaceship.png'), (player_width, player_width))
player_Right = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/player/spaceship_right.png'), (player_width, player_width))
player_Left = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/player/spaceship_left.png'), (player_width, player_width))
big_asteroid = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/meteor.png'), (asteroid_width, asteroid_width))
laser = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/laser/2.png'), (laser_width, laser_height)) 
flaming_meteor = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/flaming_meteor.png'), (asteroid_width, asteroid_width))
#alien 1 
alien_1 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy1/1.png'), (alien_width, alien_width))
alien_2 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy1/2.png'), (alien_width, alien_width))
alien_3 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy1/3.png'), (alien_width, alien_width))
alien_4 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy1/4.png'), (alien_width, alien_width))
alien_5 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy1/5.png'), (alien_width, alien_width))
alien_6 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy1/6.png'), (alien_width, alien_width))
alien1_sprites = [alien_1, alien_2,alien_3,alien_4,alien_5,alien_6]
#alien 2
alien_7 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy2/1.png'), (alien_width, alien_width))
alien_8 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy2/2.png'), (alien_width, alien_width))
alien_9 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy2/3.png'), (alien_width, alien_width))
alien_10 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy2/4.png'), (alien_width, alien_width))
alien2_sprites = [alien_7,alien_8,alien_9,alien_10]
#alien 3 
alien_11 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy3/1.png'), (alien_width, alien_width))
alien_12 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy3/2.png'), (alien_width, alien_width))
alien_13 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy3/3.png'), (alien_width, alien_width))
alien_14 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy3/4.png'), (alien_width, alien_width))
alien_15 = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/enemy3/5.png'), (alien_width, alien_width))
alien3_sprites = [alien_11,alien_12,alien_13,alien_14,alien_15]
boss_image = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/boss/1.png'), (boss_width, boss_height))
item = pygame.transform.scale(pygame.image.load("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/item/blood.png"), (blood_width, blood_width))
id2 = pygame.transform.scale(pygame.image.load("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/item/item2.png"),(blood_width,blood_width))
id3 = pygame.transform.scale(pygame.image.load("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/item/item3.png"),(item_width,item_width))
#boss2_image = pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/enemy/boss/1.png'))
#initialize pygame and create window
#player health

pygame.mixer.pre_init(44100, -16, 1, 512) #prevents sound delay
pygame.init()
my_font = pygame.font.SysFont("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/code/8-BIT WONDER.TTF", 70) #this needs to be after pygame.init()
game_over_font = pygame.font.SysFont("bell", 120, bold=True) #game over font
win_font = pygame.font.SysFont('cambrian', 120, bold=True)
#pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deadline")
clock = pygame.time.Clock()
class Items(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = item
        self.rect = self.image.get_rect(center = pos) #figures out rectangle hitbox based on image 
        #self.rect.center =  
    def update(self):
        self.rect.y += 10
        if self.rect.y > HEIGHT:
            #item.remove(self)
            all_sprites.remove(self)
class Items2(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = id2
        self.rect = self.image.get_rect(center = pos) #figures out rectangle hitbox based on image 
        #self.rect.center =  
    def update(self):
        self.rect.y += 10
        if self.rect.y > HEIGHT:
            #id2.remove(self)
            all_sprites.remove(self)

class Items3(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = id3
        self.rect = self.image.get_rect(center = pos) #figures out rectangle hitbox based on image 
        #self.rect.center =  
    def update(self):
        self.rect.y += 10
        if self.rect.y > HEIGHT:
            #id2.remove(self)
            all_sprites.remove(self)
class Background1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = background
        self.rect = self.image.get_rect() #figures out rectangle based on image
        self.rect.center = (WIDTH/2, HEIGHT/2)
    
    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT
        else:
            self.rect.y += scrolling_speed

class Background2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = background
        self.rect = self.image.get_rect() #figures out rectangle based on image
        self.rect.center = (WIDTH/2, -HEIGHT/2)
    
    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT
        else:
            self.rect.y += scrolling_speed

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.image1 = player_Right
        self.image2 = player_Left
        self.rect = self.image.get_rect() #figures out rectangle based on image
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/1.1)
        self.can_laser = True
        self.double_damage = True
        self.start_time = 0 
        self.start1_time = 0
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 200
    def cooldown(self):
        cur_time = pygame.time.get_ticks()
        if(cur_time - self.start_time > 5000):
            self.can_laser = True
            global laser_vel
            laser_vel = 20
        if(cur_time - self.start1_time > 5000):
            self.double_damage = True
            global asteroid_width
            asteroid_width = 20
        if not self.vulnerable:
                if cur_time - self.hurt_time >= self.invulnerability_duration:
                    self.vulnerable = True
        if not self.vulnerable:
                alpha = self.wave_value()
                self.image.set_alpha(alpha)
        else:
                self.image.set_alpha(255)
    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0: 
            return 255
        else: 
            return 0
    def update(self):
        global player_health, count, laser_delay, counts
        self.cooldown()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - player_width:
            self.image = self.image1
            self.rect.x += player_vel
        else:
            self.image = self.image 
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.image = self.image2
            self.rect.x -= player_vel
        else:
            self.image = self.image       
        count += 1 # adds a delay to the lasers (for holding down the button)
        if keys[pygame.K_SPACE] and count%laser_delay == 0:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/laser_sound.wav'))
            all_sprites.add(Laser())#space bar adds a laser sprite every time it is pressed
        
        #when an asteroid hits the player
        for asteroid in asteroids:
            if pygame.sprite.collide_rect(self, asteroid):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/space_ship_hit.wav'))
                asteroids.remove(asteroid)
                all_sprites.remove(asteroid)
                self.hurt_time = pygame.time.get_ticks()
                self.vulnerable = False
                player_health -= 1
        
        for asteroid in big_asteroids:
            if pygame.sprite.collide_rect(self, asteroid):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/space_ship_hit.wav'))
                big_asteroids.remove(asteroid)
                all_sprites.remove(asteroid)
                self.hurt_time = pygame.time.get_ticks()
                self.cooldown()
                self.vulnerable = False
                player_health -= 1

        for laser in lasers:
            if pygame.sprite.collide_rect(self, laser):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/space_ship_hit.wav'))
                lasers.remove(laser)
                all_sprites.remove(laser)
                self.hurt_time = pygame.time.get_ticks()
                self.cooldown()
                self.vulnerable = False
                player_health -= 1

        for item in items:
            if pygame.sprite.collide_rect(self,item):
                items.remove(item)
                all_sprites.remove(item)
                if player_health < 5:
                    player_health += 1

        for item in items_2:
            if pygame.sprite.collide_rect(self,item) and self.can_laser:
                items_2.remove(item)
                all_sprites.remove(item)
                self.start_time = pygame.time.get_ticks()
                self.can_laser = False
                global laser_vel
                laser_vel = 45 

        for item in items_3:
            if pygame.sprite.collide_rect(self,item):
                items_3.remove(item)
                all_sprites.remove(item)
                self.start1_time = pygame.time.get_ticks()
                global damage
                damage = 2

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_7
        self.rect = self.image.get_rect() #figures out rectangle hitbox based on image
        self.rect.center = (random.randrange(0, WIDTH-asteroid_width), 0)
        self.asteroid_vel = [random.randrange(-1,2), random.randrange(2, 12)]
        self.frame_count = 0
    
    def update(self): #asteroid movement (asteroids disappear when the hit the edge of the screen)
        self.rect.y += self.asteroid_vel[1]
        self.rect.x += self.asteroid_vel[0]
        if self.rect.y > HEIGHT:
            asteroids.remove(self)
            all_sprites.remove(self)
        self.frame_count += 1
        if self.frame_count + 1 >= 60:  
            self.frame_count = 0
        self.image = alien2_sprites[self.frame_count//15]

class BigAsteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien_11
        self.rect = self.image.get_rect() #figures out rectangle hitbox based on image
        self.rect.center = (random.randrange(0, WIDTH-asteroid_width), 0)
        self.asteroid_vel = [random.randrange(-1,2), random.randrange(2, 12)]
        self.big_asteroid_health = big_asteroid_health
        self.frame_count = 0
    
    def update(self): #asteroid movement (asteroids disappear when the hit the edge of the screen)
        self.rect.y += self.asteroid_vel[1]
        self.rect.x += self.asteroid_vel[0]
        if self.rect.y > HEIGHT:
            big_asteroids.remove(self)
            all_sprites.remove(self)
        self.frame_count += 1
        if self.frame_count + 1 >= 60:
            self.frame_count = 0
        self.image = alien3_sprites[self.frame_count//15]

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_image
        self.rect = self.image.get_rect() #figures out rectangle hitbox based on image
        self.rect.center = (WIDTH/2, -boss_height/2)
        self.boss_health = boss_health
    
    def update(self):
        global boss_vel
        if self.rect.y < HEIGHT/20:
            self.rect.y += boss_vel
        else:
            self.rect.x += boss_vel
            if self.rect.x + boss_width > WIDTH:
                boss_vel *= -1
            elif self.rect.x < 0:
                boss_vel *= -1

#adds an asteroid at a random location to all_sprites and appends it to the list asteroids if the asteroid list is less than 10
def add_asteroid():
    if random.random() < 0.1 and len(asteroids) < 4:
        asteroids.append(enemy())
        for asteroid in asteroids:
            all_sprites.add(asteroid)

def add_big_asteroid():
    if random.random() < 0.05 and len(big_asteroids) < 3:
        big_asteroids.append(BigAsteroid())
        for asteroid in big_asteroids:
            all_sprites.add(asteroid)

def add_alien():
    if random.random() < 0.01 and len(aliens) < 1:
        aliens.append(Alien())
        for alien in aliens:
            all_sprites.add(alien)

def add_boss():
    global boss_spawned
    if len(bosses) < 1 and random.random() < 0.005:
        bosses.append(Boss())
        boss_spawned = True
        for boss in bosses:
            all_sprites.add(boss)
def add_item(pos):
    items.append(Items(pos))
    for item in items:
        all_sprites.add(item)
def add_item2(pos):
    items_2.append(Items2(pos))
    for item2 in items_2:
        all_sprites.add(item2)
def add_item3(pos):
    items_3.append(Items3(pos))
    for item3 in items_3:
        all_sprites.add(item3)
def add_laser():
    global laser_count
    laser_count += 1
    if len(lasers) < 10 and laser_count + 1 >= 60:
        laser_count = 0
        if len(aliens) > 0 :
            lasers.append(EnemyLaser())
        if len(asteroids) > 0 :
            lasers.append(LaserTOOM())
        for laser in lasers:
            all_sprites.add(laser)

def draw_text():
    health = str(player_health)
    killed = str(asteroid_kill_count)
    health_label = my_font.render('Health: ' + health, 1, WHITE)
    screen.blit(health_label, (0, 0))
    killed_label = my_font.render('Points: ' + killed, 1, WHITE)
    screen.blit(killed_label, (0, HEIGHT/18))

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser
        self.rect = self.image.get_rect() #figures out rectangle hitbox based on image
        self.rect.center = player.rect.center
    
    def update(self):
        global asteroid_kill_count
        self.rect.y -= laser_vel 
        
        #if a laser collides with an asteroid, the asteroid and laser disappear
        for asteroid in asteroids:
            if pygame.sprite.collide_rect(self, asteroid):
                pygame.mixer.Channel(2).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/asteroid_explosion.wav'))
                asteroids.remove(asteroid)
                random_chance = numpy.random.uniform(1,100)
                if random_chance >= 1 and random_chance <= 10:
                    add_item2(asteroid.rect.center)
                if random_chance >= 10 and random_chance <= 20:
                    add_item3(asteroid.rect.center)
                all_sprites.remove(asteroid)
                all_sprites.remove(self) #removes laser after it hits the asteroid
                asteroid_kill_count += 1
        
        for asteroid in big_asteroids: #big asteroids take more than one hit
            if pygame.sprite.collide_rect(self, asteroid):
                asteroid.big_asteroid_health -= damage
                all_sprites.remove(self) #removes laser after it hits the asteroid
                if asteroid.big_asteroid_health < 1:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/asteroid_explosion.wav'))
                    big_asteroids.remove(asteroid)
                    all_sprites.remove(asteroid)
                    asteroid_kill_count += 3
                else:
                    pygame.mixer.Channel(4).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/big_asteroid_hit.wav'))
        
        for alien in aliens: #aliens take more than one hit
            if pygame.sprite.collide_rect(self, alien):
                alien.alien_health -= damage
                all_sprites.remove(self) #removes laser after it hits the alien
                if alien.alien_health < 1:
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/alien_killed.wav'))
                    aliens.remove(alien)
                    add_item(alien.rect.center)
                    all_sprites.remove(alien)
                    asteroid_kill_count += 10
                else:
                    pygame.mixer.Channel(5).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/alien_hit.wav'))
        
        for boss in bosses: #aliens take more than one hit
            if pygame.sprite.collide_rect(self, boss):
                boss.boss_health -= damage
                all_sprites.remove(self) #removes laser after it hits the alien
                if boss.boss_health < 1:
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/boss_death.wav'))
                    bosses.remove(boss)
                    all_sprites.remove(boss)
                    asteroid_kill_count += 1000
                else:
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/boss_hit.wav'))
        if self.rect.y < 0:
            all_sprites.remove(self)
class LaserTOOM(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #required
        self.image = pygame.Surface((enemy_laser_width,enemy_laser_height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect() #figures out rectangle based on image
        if len(asteroids) > 0:
            x = random.randrange(0,len(asteroids))
            self.rect.center = asteroids[x].rect.center 
    
    def update(self):
        self.rect.y += 20
        
        if self.rect.y > HEIGHT:
            lasers.remove(self)
            all_sprites.remove(self)
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #required
        self.image = pygame.Surface((enemy_laser_width,enemy_laser_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() #figures out rectangle based on image
        if len(aliens) > 0:
            self.rect.center = aliens[0].rect.center
    
    def update(self):
        self.rect.y += 20
        
        if self.rect.y > HEIGHT:
            all_sprites.remove(self)
    
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = alien1_sprites[0]
        self.rect = self.image.get_rect() #figures out rectangle hitbox based on image
        if random.random() < 0.5:
            self.rect.center = (0, HEIGHT/4)
            self.alien_vel = alien_vel
        else:
            self.rect.center = (WIDTH, HEIGHT/4)
            self.alien_vel = alien_vel * -1
        self.alien_health = alien_health
    
    def update(self): #asteroid movement (asteroids disappear when the hit the edge of the screen)
        global alien_frame_count
        self.rect.x += self.alien_vel
        if self.rect.x > WIDTH or self.rect.x < -alien_width:
            aliens.remove(self)
            all_sprites.remove(self)
        
        #makes alien image animated
        alien_frame_count += 1
        if alien_frame_count + 1 >= 60:
            alien_frame_count = 0
        self.image = alien1_sprites[alien_frame_count//10]
def game_over():
    global player_health
    game_over = True
    pygame.mixer.music.stop()
    pygame.mixer.Channel(3).play(pygame.mixer.Sound( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/game_over.wav'))
    while game_over:
        screen.fill(WHITE)
        label = game_over_font.render('GAME OVER', 1, BLACK)
        screen.blit(label, (WIDTH/3.7, HEIGHT/3))
        score_label = game_over_font.render('Your Score: ' + str(asteroid_kill_count), 1, BLACK)
        screen.blit(score_label, (WIDTH/4, HEIGHT/2.5))
        screen.blit(pygame.transform.scale(pygame.image.load( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/alien_boss.png'), (600, 300)), (WIDTH/2 - 300, HEIGHT/2))
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def win():
    global boss_death_count
    boss_death_count += 1
    if boss_death_count + 1 >= 150:
        boss_death_count = 0
        
        win = True
        pygame.mixer.music.stop()
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/victory_end.wav'))
        while win:
            screen.fill(WHITE)
            label = win_font.render('YOU WON!', 1, BLACK)
            score_label = win_font.render('Your Score: ' + str(asteroid_kill_count), 1, BLACK)
            screen.blit(label, (WIDTH/2.9, HEIGHT/3))
            screen.blit(score_label, (WIDTH/4, HEIGHT/2.5))
            screen.blit(pygame.transform.scale(pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/player_ship.png'), (300, 300)), (WIDTH/2 - 150, HEIGHT/2))
            pygame.display.update()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
title_font = pygame.font.SysFont("Times New Roman", 80, bold=True)

song = pygame.mixer.music.load( 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/electroman_theme.mp3')
pygame.mixer.music.play(-1)

all_sprites = pygame.sprite.Group()
all_sprites.add(Background1())
all_sprites.add(Background2())
player = Player()
all_sprites.add(player)
g = Game()
#Game Loop      
def main():
    global bosses
    g.curr_menu.run()
    while g.curr_menu.running:
        #keeps loop running at the right speed
        clock.tick(FPS)
        #process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN: #this is for if you want to spam the space bar
                if event.key == pygame.K_SPACE or event.key == pygame.K_DOWN :
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/laser_sound.wav'))
                    all_sprites.add(Laser())
        # Update
        all_sprites.update()
        add_asteroid()
        
        if len(asteroids) > 0 :
            add_laser()
        
        if asteroid_kill_count > 30: #49
            add_big_asteroid()
            pass
        if asteroid_kill_count > 40: #99
            add_alien()
            if len(aliens) > 0:
                add_laser()
        
        if asteroid_kill_count > 80 and not boss_spawned:  #179
            add_boss()
            if len(bosses) > 0:
                pass #add lasers here if you want the boss to shoot lasers
        
        if boss_spawned and len(bosses) < 1:
            g.win()
        
        if player_health < 1:
            g.updateScore(asteroid_kill_count)
            g.game_loop()
        
        # Draw / render
        all_sprites.draw(screen)
        draw_text()
        pygame.display.update()

    pygame.quit()
main()