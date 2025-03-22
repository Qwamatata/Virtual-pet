import pygame as pg
import pictures
import dog
import settings
import statistics as st
import random
import buttons
import menu
import mini_game
from settings import *
import pygame.freetype

pg.init()


class Game:
    def __init__(self):
        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.dog = dog.Dog(self)

        file = open('statistics.txt', 'r')
        lines = file.readlines()
        money = int(lines[0])
        hungry = int(lines[1])
        happy = int(lines[2])
        health = int(lines[3])

        self.st_happy = st.Statistics([0, 0], pictures.happy, happy, self)
        self.st_hungry = st.Statistics([0, 100], pictures.satiety, hungry, self)
        self.st_health = st.Statistics([0, 200], pictures.health, health, self)
        self.st_money = st.Statistics([0, 300], pictures.money, money, self)
        self.button_menu_game = buttons.Buttons('MINI GAME', 700, 0, self.button_menu_game_func, self)
        self.button_menu_food = buttons.Buttons('FOOD', 700, 100, self.button_menu_food_func, self)
        self.button_menu_shop_cl = buttons.Buttons('SHOP CLOTHES', 700, 200, self.button_menu_shop_cl_func, self)
        self.button_menu_upgrade = buttons.Buttons('UPGRADE', 700, 300, self.button_menu_upgrade_func, self)
        self.buttons = [self.button_menu_game, self.button_menu_food, self.button_menu_shop_cl,
                        self.button_menu_upgrade]
        self.fp = 0
        self.rand_happy = random.randint(100, 500)
        self.rand_health = random.randint(100, 500)
        self.rand_hungry = random.randint(100,500)
        self.food_menu = menu.Menu_food(self)
        self.clothes_menu = menu.Menu_clothes(self)
        self.mini_game_menu = mini_game.Mini_game(self)
        self.menu = None
        self.value_for_while = True
        self.clock = pg.time.Clock()
        upgrade_file = open('upgrade.txt', 'r')
        upgrade_list = upgrade_file.readlines()
        self.upgrade_price = int(upgrade_list[0])
        self.step = int(upgrade_list[1])
        self.font = pygame.freetype.Font(None, 36)
        self.condition = True
        self.lose_hit_text_pic = self.font.render('You LOSE! Press ESC for restart')
        self.lose_pic = self.lose_hit_text_pic[0]
        self.lose_hit = self.lose_hit_text_pic[1]
        self.lose_hit.center = [settings.SCREEN_WIDTH//2,settings.SCREEN_HEIGHT//2]
        self.run()

    def run(self):
        while self.value_for_while == True:
            self.screen.blit(pictures.back, [0, 0])
            if self.menu == None:
                self.event()
                if self.condition == True:
                    self.update()
                self.draw()
            else:
                self.menu.update()
                self.menu.draw()
                self.menu.event()
            self.fp += 1
            pg.display.flip()
            self.clock.tick(100)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                file = open('statistics.txt', 'w')

                file.write(f'{self.st_money.num}\n')
                file.write(f'{self.st_hungry.num}\n')
                file.write(f'{self.st_happy.num}\n')
                file.write(f'{self.st_health.num}\n')

                file.close()

                file = open('upgrade.txt', 'w')
                file.write(f'{self.upgrade_price}\n{self.step}\n')
                file.close()

                self.clothes_menu.save()
                self.value_for_while = False
            if self.condition == True:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.dog.hitbox.collidepoint(event.pos) == True:
                        self.st_money.num += self.step
                    for button in self.buttons:
                        if button.hitbox.collidepoint(event.pos) == True:
                            button.click()
            if self.condition == False:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.condition = True
                        self.step = 1
                        self.st_money.num = 0
                        self.st_happy.num = 100
                        self.st_health.num = 100
                        self.st_hungry.num = 100
                        self.upgrade_price = 100
                        for clothe in self.clothes_menu.items_objects:
                            clothe.buy = False
                            clothe.wear = False

    def update(self):
        if self.fp % self.rand_happy == 0:
            self.st_happy.num -= random.randint(1, 5)
            if self.st_happy.num <= 0:
                self.st_happy.num = 0
        if self.fp % self.rand_health == 0:
            if self.st_happy.num <= 50 or self.st_hungry.num <= 50:
                self.st_health.num -= random.randint(1, 5)

            if self.st_health.num <= 0:
                self.st_health.num = 0
                self.condition = False
        if self.fp % self.rand_hungry == 0:
            self.st_hungry.num -= random.randint(1,5)
            if self.st_hungry.num <= 0:
                self.st_hungry = 0
    def button_menu_game_func(self):
        self.menu = self.mini_game_menu
        self.mini_game_menu.catch = 0
        self.mini_game_menu.toys = []

    def button_menu_food_func(self):
        self.menu = self.food_menu

    def button_menu_shop_cl_func(self):
        self.menu = self.clothes_menu
        print('SHOP MENU')

    def button_menu_upgrade_func(self):
        if self.st_money.num >= self.upgrade_price:
            self.step += 1
            self.st_money.num -= self.upgrade_price
            self.upgrade_price *= 3

    def draw(self):
        self.dog.draw()
        self.st_happy.draw()
        self.st_money.draw()
        self.st_health.draw()
        self.st_hungry.draw()
        for button in self.buttons:
            button.draw()

        for cl in self.clothes_menu.items_objects:
            if cl.wear == True:
                cl.draw()
        self.font.render_to(self.screen, [800, 400], f'{self.upgrade_price}')

        if self.condition == False:
            self.screen.blit(self.lose_pic,self.lose_hit)


if __name__ == "__main__":
    Game()
