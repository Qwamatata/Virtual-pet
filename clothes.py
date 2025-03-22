import pygame
import settings


class Clothes:
    def __init__(self, game, picture: pygame.Surface, cost: int, wear, buy):
        self.game = game
        self.picture = picture
        self.cost = cost
        self.hitbox = pygame.Rect([0, 0], self.picture.get_size())
        self.hitbox.center = settings.SIZE[0] // 2, settings.SIZE[1] // 2
        self.buy = buy
        self.wear = wear

    def draw(self):
        if self.game.menu != None and self.game.clothes_menu.index in [5, 2, 3]:
            self.game.screen.blit(self.picture, [self.hitbox.x, self.hitbox.y + 70])
        else:
            self.game.screen.blit(self.picture, self.hitbox)
