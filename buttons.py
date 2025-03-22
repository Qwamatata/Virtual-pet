import pygame
import pictures
import pygame.freetype



class Buttons:
    def __init__(self, text:str, x:int, y:int, func ,game):
        self.picture = pictures.button
        self.size = self.picture.get_size()
        self.hitbox = pygame.Rect([x,y],self.picture.get_size())
        self.text = text
        self.game = game
        font = pygame.freetype.Font(None, 20)
        picture_hitbox_text = font.render(self.text)
        self.pic_t = picture_hitbox_text[0]
        self.hitbox_t = picture_hitbox_text[1]
        self.hitbox_t.center = self.hitbox.center
        self.click_moment = 0
        self.func = func
    def draw(self):
        self.game.screen.blit(self.picture,self.hitbox)
        self.game.screen.blit(self.pic_t,self.hitbox_t)
        if self.game.fp >= self.click_moment + 20:
            self.picture = pictures.button
    def click(self):
        self.picture = pictures.button_pr
        self.click_moment = self.game.fp
        self.func()

    def ch_text(self,text):
        font = pygame.freetype.Font(None, 20)
        picture_hitbox_text = font.render(text)
        self.pic_t = picture_hitbox_text[0]
        self.hitbox_t = picture_hitbox_text[1]
        self.hitbox_t.center = self.hitbox.center




