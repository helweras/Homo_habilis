from MP import MainPlayer
import pygame
import sys
import pathlib
from Camera import Camera
import Map
from Tree import Tree


class Game:
    """Основной класс в котором будут происходить взаимодействия других классов друг с другом"""

    def __init__(self):
        pygame.init()  # Инициализация модулей pygame
        # Создаем группу спрайтов
        self.mp_spr = pygame.sprite.Group()

        self.mp = None
        self.map = Map.Map()

        self.screen_size = self.get_screen_size(1200, 700)  # Ширина и Высота экрана в пикселях
        self.camera = Camera(screen_size=self.screen_size, size=350, coord=(1000, 1000))

        self.tree_group_spr = pygame.sprite.Group()
        self.screen = None
        self.fps = None
        self.clock = pygame.time.Clock()
        self.set_screen(self.screen_size, "Homo Habilis")

    def draw_tiles_surface(self):
        """Отрисовка тайлов поверхности с учетом отклонения от игрока"""
        for s in self.map.surface_spr:
            x, y = self.camera.apply(s.rect)[0], self.camera.apply(s.rect)[1]
            if x <= 1200 and y <= 800:
                self.screen.blit(s.image, self.camera.apply(s.rect))

    def tree(self):
        tree = Tree()
        self.tree_group_spr.add(tree)

    def set_screen(self, params: tuple, name_screen: str, fps=20):
        """Создает экран и устанавливает его параматры:
        - Размеры
        - FPS
        - Имя окна"""
        self.screen = pygame.display.set_mode(params)  # Установка размеров
        pygame.display.set_caption(name_screen)  # Установка имени
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

    def add_mp_spr(self, mp_spr):
        """Добавляет mp_spr (Главного персонажа) в группу спрайтов
        и присваивет атрибуту mp экземпляр класса MainPlayer"""
        self.mp_spr.add(mp_spr)
        self.mp = self.mp_spr.sprites()[0]

    def create_mp_spr(self):
        """Создает экземпляр класса MainPlayer"""
        img = self.get_list_name_file('mp_image')
        return MainPlayer(img[0])

    def start_game(self):
        self.add_mp_spr(self.create_mp_spr())  # Создание главного персонажа
        self.camera.update_target(self.mp.rect)
        self.tree()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.mp.update_position()  # Вызов функции перемещения персонажа
            self.camera.track_target(self.mp)  # Слежение камеры за игроком
            self.camera.update_camera()  # Центрирование камеры по экрану
            self.screen.fill((0, 0, 0))

            self.draw_tiles_surface()

            for i in self.tree_group_spr:
                if i.rect.bottom < self.mp.rect.bottom + 5:
                    self.screen.blit(i.image, self.camera.apply(i.rect))
                    self.screen.blit(self.mp.image, self.camera.apply(self.mp.rect))
                else:
                    self.screen.blit(self.mp.image, self.camera.apply(self.mp.rect))
                    self.screen.blit(i.image, self.camera.apply(i.rect))
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start_game()
