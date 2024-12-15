import pygame
from pygame.sprite import Sprite


class Surface(Sprite):
    """Класс описывающий поведение поверхности на которой будут находиться объекты"""

    def __init__(self, image, coord, size=(50, 50)):
        super().__init__()
        self.image = image  # Картинка по умолчанию
        self.surface = pygame.Surface(size)  # Создание класс Surface
        self.rect = self.surface.get_rect()
        # Присваивание координат
        self.rect.x = coord[0]
        self.rect.y = coord[1]
