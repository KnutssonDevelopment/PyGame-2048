import pygame

# Initialize Pygame
pygame.init()
WINDOW_SIZE = 1200
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("2048 Game")

# Define constants
BACKGROUND_COLOR = (187, 173, 160)
GRID_SIZE = 4
TILE_SIZE = WINDOW_SIZE // GRID_SIZE
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
FONT_COLOR = (119, 110, 101)
FONT_SIZE = 80

TITLE_FONT_COLOR = (0, 0, 0)
TITLE_FONT_SIZE = WINDOW_SIZE // 7
TILE_MOVEMENT_SPEED = 40

FONT_PATH = "res/fonts/Roboto/Roboto-Regular.ttf"
