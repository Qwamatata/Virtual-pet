import pygame
import os

import settings

back =  pygame.image.load('images/background.png')
back = pygame.transform.scale(back,[900,550])

dog = pygame.image.load('images/dog.png')
dog = pygame.transform.scale(dog,[200,400])

happy = pygame.image.load('images/happiness.png')
happy = pygame.transform.scale(happy,[100,100])

health = pygame.image.load('images/health.png')
health = pygame.transform.scale(health,[100,100])

satiety = pygame.image.load('images/satiety.png')
satiety = pygame.transform.scale(satiety,[100,100])

money = pygame.image.load('images/money.png')
money = pygame.transform.scale(money,[100,100])

button = pygame.image.load('images/button.png')
button = pygame.transform.scale(button,[200,75])

button_pr = pygame.image.load('images/button_clicked.png')
button_pr = pygame.transform.scale(button_pr,[200,75])

menu = pygame.image.load('images/menu/menu_page.png')
menu = pygame.transform.scale(menu,[900,550])

game_back = pygame.image.load('images/game_background.png')
game_back = pygame.transform.scale(game_back, settings.SIZE)

food_files_names = os.listdir('images/food')
food_images = []

for file in food_files_names:
    image = pygame.image.load(f'images/food/{file}')
    image = pygame.transform.scale(image, [150,150])
    food_images.append(image)

cl_files_names = os.listdir('images/items')
cl_images = []

for file in cl_files_names:
    image = pygame.image.load(f'images/items/{file}')
    image = pygame.transform.scale(image,[200,400])
    cl_images.append(image)

toys_files_names = os.listdir('images/toys')
toys_images = []

for file in toys_files_names:
    image = pygame.image.load(f'images/toys/{file}')
    image = pygame.transform.scale(image,[90,90])
    toys_images.append(image)

