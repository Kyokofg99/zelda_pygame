import pygame

from settings import *
from player import Player

class UI:
    def __init__(self):
        
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame

    def display(self, player:Player):
        pass