import pygame
from pygame.sprite import Sprite


class Platform(Sprite):
    """Класс описывающий все необходимые параметры платформ по которым будет перемещаться игрок
    Любой объект наследованный от класса Sprite должен иметь атрибут с названием image"""

    def __init__(self, coord, size=(16, 16)):
        super().__init__()
        self.image = None  # Будет присвоен экземпляр класса surface
        self.rect = None
        self.set_surface(size, coord)

    def set_surface(self, size, coord):
        """Метод создающий объект Surface, устанавливает его размеры и текущие координаты
        Ожидает на входе:
        size - кортеж с 2-мя значениями размера в пикселях по x и y
        coord -кортеж с 2-мя значениями положения на экране x и y"""

        self.image = pygame.Surface(size)  # Создаем объект Surface
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()  # Получение координат Surface объекта
        # Установка координат
        self.rect.x = coord[0]
        self.rect.y = coord[1]
