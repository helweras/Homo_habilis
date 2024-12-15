import pygame
from pygame import Rect


class Camera:
    """Класс камеры которая следит за игроком"""

    def __init__(self, screen_size, size, coord):
        self.offset_x = 0
        self.offset_y = 0
        self.size = size
        self.coord_x, self.coord_y = coord
        self.screen_width, self.screen_height = screen_size
        self.state = Rect(0, 0, self.screen_width, self.screen_height)
        self.camera_rect = Rect(self.coord_x, self.coord_y, size, size)  # Следящий квадрат камеры

    def update_camera(self):
        """Метод отвечает за центрирование квадрата камеры по середине экрана"""
        # Центрируем камеру относительно персонажа
        self.offset_x = self.camera_rect.centerx - self.screen_width // 2
        self.offset_y = self.camera_rect.centery - self.screen_height // 2

    def update_target(self, target_rect):
        """Метод отвечает за центрирование камеры по игроку
        При применениии этого метода картинка игрока будет строго посередине экрана"""
        # Центрируем камеру относительно персонажа
        self.camera_rect.center = target_rect.center

    def apply(self, rect):
        """Метод смещает rect относительно посчитанных отклонений от цели"""
        # Смещаем прямоугольник объекта
        return rect.move(-self.offset_x, -self.offset_y)

    def track_target(self, target):
        """Метод двигает камеру за игроком"""
        target_rect = target.rect  # Получаем rect цели
        old_x, old_y = target.old_position  # Получаем старую позицию цели
        x_midl, y_midl, = self.camera_rect.center  # Получаем координаты центра камеры
        x_target, y_target = target_rect.center  # Получаем координаты центра цели
        x_vector, y_vector = x_target - old_x, y_target - old_y  # Считаем вектор движения цели
        # Считаем смещение центра цели от центра камеры
        x_offset = x_midl - x_target
        y_offset = y_midl - y_target
        # Если смещение превышает заданное значение то смещаем камеру по направлению к цели
        if abs(x_offset) >= self.size // 2 or abs(y_offset) >= self.size // 2:
            self.camera_rect = self.camera_rect.move(x_vector, y_vector)
