import pygame

class Level:
    def __init__(self):

        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprite = pygame.sprite.Group()
        self.obstables_sprites = pygame.sprite.Group()

    def run(self):
        # update an draw the game
        pass