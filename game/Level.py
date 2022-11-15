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
from particles import AnimationPlayer
from magic import MagicPlayer


class level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = camera()
        self.obstacles_sprites = pygame.sprite.Group()

        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.create_map()

        self.ui = UI()

        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

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
                                 if col == '210':monster_name = 'demon'
                                 elif col == '22':monster_name = 'ghost'
                                 Enemy(monster_name,(x,y),[self.visible_sprites],self.obstacles_sprites)
    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

        if style == 'flame':
            self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

    
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
            if self.attack_sprites:
                for attack_sprite in self.attack_sprites:
                    collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                    if collision_sprites:
                        for target_sprite in collision_sprites:
                            if target_sprite.sprite_type == 'grass':
                                target_sprite.kill()
                            else:
                                target_sprite.get_damage(self.player,attack_sprite.sprite_type)
    def damage_player(self,amount,attack_type):
            if self.player.vulnerable:
                self.player.health -= amount
                self.player.vulnerable = False
                self.player.hurt_time = pygame.time.get_ticks()
			# spawn particles
    def trigger_death_particles(self,pos,particle_type):

        self.animation_player.create_particles(particle_type,pos,self.visible_sprites)


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)


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

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
