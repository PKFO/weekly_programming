import pygame
from map_settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/character/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
