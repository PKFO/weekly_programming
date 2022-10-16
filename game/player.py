import pygame
from map_settings import *

class Player(pygame.Sprite.Sprite):
    def _init_(self,pos,groups):
        super()._init_(groups)
        self.image = pygame.image.load("main character.png")
        self.rect = self.image.get_rect(topleft = pos)