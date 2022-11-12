from math import floor
import pygame
from tile import Tile
from map_settings import *
from player import Player
from random import choice
from debug import debug
from support import *
from ui import UI
from enemy import Enemy


class level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = camera()
        self.obstacles_sprites = pygame.sprite.Group()
        self.create_map()
        self.ui = UI()

    def create_map(self):
        layout = {
            'boudary': import_csv_layout('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/gameproject_Floorblock_Floorblock.csv'),
            'detail': import_csv_layout('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/gameproject_Floorblock_detail.csv'),
            'Entities': import_csv_layout('C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/gameproject_enemy.csv')
        }
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boudary':
                            Tile((x, y), [self.obstacles_sprites], 'invisible')
                        if style == 'detail':
                            Tile((x, y), [self.obstacles_sprites], 'invisible')
                        if style == 'Entities':
                            if col == '21':
                                self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites, self.create_magic)
                            else:
                                Enemy('ghost',(x,y),[self.visible_sprites])


    def create_magic(self, style, strenght, cost):
        print(style)
        print(strenght)
        print(cost)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        #self.visible_sprites.enemy_update(self.player)
        #self.ui.display(self.player)


class camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surface = pygame.image.load(
            'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/floor.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
