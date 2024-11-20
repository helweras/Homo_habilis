import random

import pygame
import sys
import pathlib
import Platform
import Surfaces


class Game:
    """Основной класс в котором будут происходить взаимодействия других классов друг с другом"""

    def __init__(self):
        pygame.init()  # Инициализация модулей pygame
        self.platform_spr = pygame.sprite.Group()  # Создаем группу спрайтов
        self.surface_spr = pygame.sprite.Group()
        self.surface_image = self.get_list_name_file('tiles')
        self.screen_size = self.get_screen_size(1200, 700)  # Ширина и Высота экрана в пикселях
        self.screen = None
        self.fps = None
        self.clock = pygame.time.Clock()
        self.set_screen(self.screen_size, "Homo Habilis")

    def set_screen(self, params: tuple, name_screen: str, fps=20):
        """Создает экран и устанавливает его параматры:
        - Размеры
        - FPS
        - Имя окна"""
        self.screen = pygame.display.set_mode(params)  # Установка размеров
        pygame.display.set_caption(name_screen)  # Установка имени
        self.screen.fill('#ffffff')  # Установка цвета заднего фонв
        self.fps = fps  # Установка FPS

    @staticmethod
    def get_screen_size(size_x=0, size_y=0):
        """Получение параметров экрана.
        Вовращает размеры экрана в пикселях"""
        if size_x and size_y:
            return size_x, size_y
        info = pygame.display.Info()
        return info.current_w, info.current_h

    @staticmethod
    def get_list_name_file(path) -> list:
        """Возвращает список с тайлами (Объектами типа Surface)"""
        folder_path = pathlib.Path(path)
        name_list = [f'{path}/{f.name}' for f in folder_path.iterdir() if
                     f.is_file()]  # Генерация списка с названиями файлов по пути path
        return [pygame.image.load(img) for img in name_list]  # Возвращение списка с объектами Surface

    def add_platform_spr(self, platform_sprite):
        """Добавляет спрайт платформы в группу спрайтов платформ"""
        self.platform_spr.add(platform_sprite)

    def add_surface_spr(self, surface_sprite):
        self.surface_spr.add(surface_sprite)

    def create_platform_spr(self):
        new_platform = Platform.Platform((100, 100))
        return new_platform

    def create_surface_spr(self, coord):
        ind = self.random_num()
        image = self.surface_image[ind]
        # image = random.choice(self.surface_image)
        new_surface = Surfaces.Surface(image, coord)
        return new_surface

    @staticmethod
    def random_num():
        num = random.random()
        if num <= 0.5:
            return 0
        elif 0.5 < num < 0.8:
            return 3
        elif 0.8 < num < 0.9:
            return 2
        else:
            return 1

    def add_in_grop_surface(self):
        """Добавление тайлов поверхности в группу спрайтов для поверхности"""
        size_x, size_y = self.screen_size
        for y in range(0, size_y + 50, 50):
            for x in range(0, size_x + 50, 50):
                self.add_surface_spr(self.create_surface_spr((x, y)))

    def start_game(self):
        self.add_platform_spr(self.create_platform_spr())
        self.add_in_grop_surface()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # self.platform_spr.draw(self.screen)
            self.surface_spr.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.start_game()
