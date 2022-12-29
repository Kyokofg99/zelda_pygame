import enum
from re import X
import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout

class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstables_sprites = pygame.sprite.Group()

        # sprite set up
        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('map/map_FloorBlocks.csv')
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index *  TILESIZE
                    
                        if style == 'boundary':
                            Tile((x,y), [self.visible_sprites, self.obstables_sprites], 'invisible')
        #        if col == 'x':
        #            Tile((x,y), [self.visible_sprites, self.obstables_sprites])
        #        if col == 'p':
        #            self.player : Player = Player((x,y), [self.visible_sprites], self.obstables_sprites)
        self.player : Player = Player((2000,1430), [self.visible_sprites], self.obstables_sprites)

    def run(self):
        # update an draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        # debug info
        debug(self.player.direction)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creando suelo
        self.floor_surface : pygame.Surface = pygame.image.load('./graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0,0))

    def custom_draw(self, player : Player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset # no longer a Vector, but pygame still likes Tuple
            self.display_surface.blit(sprite.image, offset_pos)
