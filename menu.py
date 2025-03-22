import pygame
import pictures
import food
import random
import buttons
import pygame.freetype
import clothes

import settings


class Menu_food:
    def __init__(self, game):
        self.picture = pictures.menu
        self.game = game
        self.food_objects = []
        for food_image in pictures.food_images:
            food_image = food.Food(self.game, food_image, random.randint(50, 500))
            self.food_objects.append(food_image)
        self.button_eat = buttons.Buttons('EAT ME', settings.SCREEN_WIDTH // 2 - pictures.button.get_width() // 2, 400,
                                          self.func_eat, self.game)
        self.button_next = buttons.Buttons('BACK', pictures.button.get_width() // 2, 400, self.func_back, self.game)
        self.button_back = buttons.Buttons('NEXT', 600, 400, self.func_next, self.game)
        self.buttons = [self.button_eat, self.button_next, self.button_back]
        self.index = 0
        self.font = pygame.freetype.Font(None, 30)

    def draw(self):
        self.game.screen.blit(self.picture, [0, 0])
        self.food_objects[self.index].draw()
        for button in self.buttons:
            button.draw()
        cost = self.food_objects[self.index].cost
        self.font.render_to(self.game.screen, [settings.SCREEN_WIDTH // 2 - 25, 170], f'{cost}', [0, 0, 0])

    def func_eat(self):
        if self.game.st_money.num >= self.food_objects[self.index].cost:
            self.game.st_money.num -= self.food_objects[self.index].cost
            if self.index == len(self.food_objects) - 1:
                self.game.st_health.num += random.randint(1, 10)
                if self.game.st_health.num >= 100:
                    self.game.st_health.num = 100
            else:
                self.game.st_hungry.num += random.randint(1, 10)
                if self.game.st_hungry.num >= 100:
                    self.game.st_hungry.num = 100

    def func_next(self):
        self.index += 1
        if self.index == len(self.food_objects):
            self.index = 0

    def func_back(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.food_objects) - 1

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hitbox.collidepoint(event.pos) == True:
                        button.click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.menu = None

    def update(self):
        pass

class Menu_clothes:
    def __init__(self, game):
        self.picture = pictures.menu
        self.game = game
        self.items_objects = []
        wear = open('wear.txt', 'r')
        buy = open('buy.txt', 'r')
        list_wear = wear.readlines()
        list_buy = buy.readlines()
        line = 0
        for cl_image in pictures.cl_images:
            cl_image = clothes.Clothes(self.game, cl_image, random.randint(50, 500),int(list_wear[line]),int(list_buy[line]))
            self.items_objects.append(cl_image)
            line += 1
        self.button_buy = buttons.Buttons('BUY', settings.SCREEN_WIDTH // 2 - pictures.button.get_width() // 2, 400,
                                          self.func_buy, self.game)
        self.button_next = buttons.Buttons('BACK', pictures.button.get_width() // 2, 400, self.func_back, self.game)
        self.button_back = buttons.Buttons('NEXT', 600, 400, self.func_next, self.game)
        self.buttons = [self.button_buy, self.button_next, self.button_back]
        self.index = 0
        self.font = pygame.freetype.Font(None, 30)

    def draw(self):
        self.game.screen.blit(self.picture, [0, 0])
        self.items_objects[self.index].draw()
        for button in self.buttons:
            button.draw()
        cost = self.items_objects[self.index].cost
        self.font.render_to(self.game.screen, [settings.SCREEN_WIDTH // 2 - 25, 170], f'{cost}', [0, 0, 0])

    def func_buy(self):
        if self.game.st_money.num >= self.items_objects[self.index].cost:
            self.game.st_money.num -= self.items_objects[self.index].cost
            self.items_objects[self.index].buy = True

    def func_wear(self):
        self.items_objects[self.index].wear = not self.items_objects[self.index].wear

    def func_next(self):
        self.index += 1
        if self.index == len(self.items_objects):
            self.index = 0


    def func_back(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.items_objects) - 1

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hitbox.collidepoint(event.pos) == True:
                        button.click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.menu = None

    def update(self):
        if self.items_objects[self.index].buy == True:
            if self.items_objects[self.index].wear == False:
                self.button_buy.ch_text('WEAR')
                self.button_buy.func = self.func_wear
            if self.items_objects[self.index].wear == True:
                self.button_buy.ch_text('TAKE OFF')
                self.button_buy.func = self.func_wear

        else:
            self.button_buy.ch_text('BUY')
            self.button_buy.func = self.func_buy

    def save(self):
        file_wear = open('wear.txt','w')
        for cl in self.items_objects:
            file_wear.write(f'{int(cl.wear)}\n')
        file_wear.close()
        file_buy = open('buy.txt','w')
        for cl in self.items_objects:
            file_buy.write(f'{int(cl.buy)}\n')
        file_buy.close()

