import pathlib
import pygame
import random


class Support:
    @staticmethod
    def get_list_name_file(path) -> list:
        """Возвращает список с тайлами (Объектами типа Surface)"""
        folder_path = pathlib.Path(path)
        name_list = [f'{path}/{f.name}' for f in folder_path.iterdir() if
                     f.is_file()]  # Генерация списка с названиями файлов по пути path
        return [pygame.image.load(img) for img in name_list]  # Возвращение списка с объектами Surface

    @staticmethod
    def random_num():
        """Мтетод возыращает число в заданной вероятности"""
        num = random.random()
        if num <= 0.5:
            return 0
        elif 0.5 < num < 0.8:
            return 3
        elif 0.8 < num < 0.9:
            return 2
        else:
            return 1
