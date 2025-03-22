import pygame
import settings


class Food:
    def __init__(self, game, picture:pygame.Surface, cost:int):
        self.game = game
        self.picture = picture
        self.cost = cost
        self.hitbox = pygame.Rect([0,0],self.picture.get_size())
        self.hitbox.center = settings.SIZE[0]//2,settings.SIZE[1]//2
    def draw(self):
        self.game.screen.blit(self.picture,self.hitbox)
