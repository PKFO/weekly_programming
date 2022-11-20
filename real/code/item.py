import pygame
from main import *
vec = pygame.math.Vector2
blood_width = 30
items = pygame.transform.scale(pygame.image.load("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/test/real/item/blood.png"), (blood_width, blood_width))
class Items(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Items
        self.rect = self.image.get_rect() #figures out rectangle hitbox based on image 
        #self.rect.center =  
    def update(self):
        if self.rect.y > HEIGHT:
            Items.remove(self)
            all_sprites.remove(self)
        #if 