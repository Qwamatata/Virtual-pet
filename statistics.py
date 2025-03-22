import pygame
import pygame.freetype
import pictures


class Statistics:
    def __init__(self,dest:list[int],picture:pygame.surface.Surface,number:int,game):
        self.picture = picture
        self.hitbox = pygame.Rect(dest,self.picture.get_size())
        self.num = number
        self.game = game
        self.font = pygame.freetype.Font(None,35)
    def draw(self):
        self.game.screen.blit(self.picture,self.hitbox)
        self.font.render_to(self.game.screen,[self.hitbox.x + 100,self.hitbox.y + 50],f'{self.num}',[12, 35, 242])