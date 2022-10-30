from math import floor
import pygame
from tile import Tile
from map_settings import *
from player import Player
class level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = camera()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()
    def create_map(self):
        # for row_index,row in enumerate(WORLD_MAP):
        #     for col_index,col in enumerate(row):
        #         x = col_index * TILESIZE
        #         y = row_index * TILESIZE
        #         if col == 'x':
        #             Tile((x,y),[self.visible_sprites,self.obstacles_sprites])
        #         if col == 'p':
        #             self.player = Player((x,y),[self.visible_sprites],self.obstacles_sprites)
        self.player = Player((2000,1500),[self.visible_sprites],self.obstacles_sprites)
    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
class camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/floor.png')
        self.floor_rect =   self.floor_surface.get_rect(topleft = (0,0))
    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos) 
