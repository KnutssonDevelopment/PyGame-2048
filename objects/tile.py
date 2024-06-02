from shared_resources import *

font = pygame.font.Font(FONT_PATH, FONT_SIZE)
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)


class Tile:
    def __init__(self, row, column, height, width):
        self.row = row
        self.column = column
        self.height = height
        self.width = width
        self.direction = None
        self.x = column * self.width
        self.y = row * self.height
        self.value = 0
        self.color = (255, 255, 255)
        self.rect = None

    def set_direction(self, direction):
        if direction in ["left", "right", "up", "down"]:
            self.direction = direction

    def move(self):

        if self.direction == 'left':
            self.x -= TILE_MOVEMENT_SPEED
            if self.x <= (self.column - 1) * self.width:
                self.column -= 1
                self.x = self.column * self.width
                self.direction = None

        elif self.direction == 'right':
            self.x += TILE_MOVEMENT_SPEED
            if self.x >= (self.column + 1) * self.width:
                self.column += 1
                self.x = self.column * self.width
                self.direction = None

        elif self.direction == 'up':
            self.y -= TILE_MOVEMENT_SPEED
            if self.y <= (self.row - 1) * self.height:
                self.row -= 1
                self.y = self.row * self.height
                self.direction = None

        elif self.direction == 'down':
            self.y += TILE_MOVEMENT_SPEED
            if self.y >= (self.row + 1) * self.height:
                self.row += 1
                self.x = self.column * self.height
                self.direction = None

    def set_value(self, value):
        if value > -1:
            self.value = value
            self.color = TILE_COLORS.get(self.value, (60, 58, 50))

    def draw(self):
        self.move()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
        if self.value != 0:
            text = font.render(str(self.value), True, FONT_COLOR)
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)
