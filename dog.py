import pygame
import pictures
import settings


class Dog:
    def __init__(self, game):
        self.picture = pictures.dog
        self.hitbox = pygame.Rect([0, 0], self.picture.get_size())
        self.hitbox.center = settings.SIZE[0] // 2, settings.SIZE[1] // 2
        self.game = game

    def draw(self):
        self.game.screen.blit(self.picture, self.hitbox)


class Dog_mini(Dog):

    def __init__(self, game):
        super().__init__(game)
        self.picture = pygame.transform.scale(self.picture, [self.hitbox.width // 3, self.hitbox.height // 3])
        self.hitbox = pygame.Rect([0, 0], self.picture.get_size())
        self.hitbox_collide = pygame.Rect([0, 0], [self.hitbox.width // 1.5, self.hitbox.height // 1.5])
        self.hitbox.center = settings.SIZE[0] // 2, settings.SIZE[1] // 1.25

    def update(self):
        cond_all = pygame.key.get_pressed()
        if cond_all[pygame.K_LEFT] and self.hitbox.x > 0:
            self.hitbox.x -= 2
        elif cond_all[pygame.K_RIGHT] and self.hitbox.right < settings.SCREEN_WIDTH:
            self.hitbox.x += 2
        self.hitbox_collide.center = self.hitbox.center
