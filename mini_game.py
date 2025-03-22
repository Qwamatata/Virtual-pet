import pygame
import pictures
import dog
import toys

class Mini_game:
    def __init__(self, game):
        self.game = game
        self.picture = pictures.game_back
        self.dog = dog.Dog_mini(self.game)
        self.toys = []
        self.catch = 0

    def draw(self):
        self.game.screen.blit(self.picture, [0,0])
        self.dog.draw()
        for toy in self.toys:
            toy.draw()
            toy.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.game.value_for_while = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.menu = None
                    self.game.st_happy.num += self.catch
                    if self.game.st_happy.num > 100:
                        self.game.st_happy.num = 100

    def update(self):
        self.dog.update()
        if self.game.fp%50 == 0:
            toy = toys.Toys(self.game)
            self.toys.append(toy)
        for toy in self.toys:
            if self.dog.hitbox_collide.colliderect(toy.hitbox):
                self.toys.remove(toy)
                self.catch += 1