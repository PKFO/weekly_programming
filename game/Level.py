import pygame
from map_settings import *
class Level:
    def _init_(Self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()
    def create_map(self):
        for row in WORLD_MAP:
            print(row)

    def run(self):
        pass
