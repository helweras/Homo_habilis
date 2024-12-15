import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 50  # Размер одного тайла
FPS = 30

# Цвета
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Camera Example")


# Класс камеры
class Camera:
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height

    def update(self, target_rect):
        # Центрируем камеру относительно персонажа
        self.offset_x = target_rect.centerx - self.width // 2
        self.offset_y = target_rect.centery - self.height // 2

    def apply(self, rect):
        # Смещаем прямоугольник объекта
        return rect.move(-self.offset_x, -self.offset_y)


# Класс персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed


# Класс карты
class TileMap:
    def __init__(self):
        self.tiles = []
        self.generate_map()

    def generate_map(self):
        for row in range(3):  # Генерация карты
            for col in range(3):
                tile_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                self.tiles.append(tile_rect)

    def draw(self, surface, camera):
        for tile in self.tiles:
            pygame.draw.rect(surface, WHITE, tile, 1)


# Инициализация объектов
player = Player(150, 150)
camera = Camera(800, 600)  # Размер карты
tile_map = TileMap()
clock = pygame.time.Clock()

# Основной игровой цикл
for i in tile_map.tiles:
    print(i)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Обновляем камеру
    camera.update(player.rect)

    # Отрисовка
    screen.fill((0, 0, 0))
    tile_map.draw(screen, camera)
    print(camera.apply(player.rect))
    # print('Camera = ', camera.apply(player.rect))
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
