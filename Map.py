import pygame
import Surfaces
from Support import Support


class Map:
    support = Support()

    def __init__(self):
        self.size_x, self.size_y = 2000, 1000
        self.surface_image_grass = self.support.get_list_name_file(r'tiles\grass')
        self.surface_image_sand = self.support.get_list_name_file(r'tiles\sand')
        self.surface_spr = pygame.sprite.Group()
        self.add_in_grop_surface(16, 3)

    def create_surface_spr(self, coord, type_surface: list):
        """Возвращает новый тайл поверхности"""
        ind = self.support.random_num()  # Получение случайного числа (индекса)
        image = type_surface[ind]  # Получение картинки со случайным индексом
        new_surface = Surfaces.Surface(image, coord)
        return new_surface

    def add_surface_spr(self, surface_sprite):
        """Добавляет спрайт поверхности в группу спрайтов"""
        self.surface_spr.add(surface_sprite)

    def add_in_grop_surface(self, grass, sand):
        """Добавление тайлов поверхности в группу спрайтов для поверхности"""
        count_tiles = 0
        for y in range(0, self.size_y, 250):
            for x in range(0, self.size_x, 250):
                if grass > count_tiles:
                    self.add_surface_spr(self.create_surface_spr((x, y), self.surface_image_grass))
                else:
                    self.add_surface_spr(self.create_surface_spr((x, y), self.surface_image_sand))
                count_tiles += 1
