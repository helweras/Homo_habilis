import pygame
from pygame.sprite import Sprite
import pathlib


class Tree(Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.get_list_name_file('tree')[0]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.surface = pygame.Surface((100, 100))
        self.rect = self.surface.get_rect()
        self.rect.x = 200
        self.rect.y = 200

    @staticmethod
    def get_list_name_file(path) -> list:
        """Возвращает список с тайлами (Объектами типа Surface)"""
        folder_path = pathlib.Path(path)
        name_list = [f'{path}/{f.name}' for f in folder_path.iterdir() if
                     f.is_file()]  # Генерация списка с названиями файлов по пути path
        return [pygame.image.load(img) for img in name_list]  # Возвращение списка с объектами Surface
