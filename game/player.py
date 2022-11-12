import pygame
from map_settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_magic):
        super().__init__(groups)
        self.image = pygame.image.load("C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/character/Player1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.obstacle_sprites = obstacle_sprites

        # magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # stats
        self.stats = {'health': 100, 'energy': 100, 'magic': 5, 'speed': 3}
        self.health = self.stats['health'] * 0.5
        self.energy = self.stats['energy'] * 0.8
        self.exp = 123
        self.speed = self.stats['speed']

    def import_player_assets(self):
        character_path = 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/character/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 'idle_up': [], 'idle_right': [], 'idle_left': [], 'idle_down': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

        # magic
        if keys[pygame.K_SPACE]:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            style = list(magic_data.keys())[self.magic_index]
            strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
            cost = list(magic_data.values())[self.magic_index]['cost']
            self.create_magic(style, strength, cost)

            print('attack')

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = 'idle_' + self.status 
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
