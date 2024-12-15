import pygame
from pygame.sprite import Sprite
from Support import Support


class MainPlayer(Sprite):
    support = Support()

    def __init__(self, image, size=(64, 64), coord=(0, 0)):
        super().__init__()
        self.image = self.support.get_list_name_file('mp_image')[0]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = coord
        self.speed = 10
        self.old_position = self.rect.center
        self.update_position()

    def move_control(self, x, y):
        """Для движения по нажатию кнопки"""
        self.rect.x += self.speed * x
        self.rect.y += self.speed * y

    def update_position(self):
        self.old_position = self.rect.center  # Сохраняем старую позицию
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move_control(-1, 0)
        if keys[pygame.K_d]:
            self.move_control(1, 0)
        if keys[pygame.K_w]:
            self.move_control(0, -1)
        if keys[pygame.K_s]:
            self.move_control(0, 1)

    def draw_in_screen(self, screen):
        screen.blit(self.image, self.rect.topleft)
