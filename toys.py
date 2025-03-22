import pygame
import pictures
import random
import settings

class Toys:
    def __init__(self, game):
        self.picture = pictures.toys_images[random.randint(0,len(pictures.toys_images) - 1)]
        self.hitbox = pygame.Rect([random.randint(0, settings.SCREEN_WIDTH),0], self.picture.get_size())
        self.game = game

    def draw(self):
        self.game.screen.blit(self.picture,self.hitbox)

    def update(self):
        self.hitbox.y += 1