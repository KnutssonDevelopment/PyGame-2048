import random
import pygame

from shared_resources import *
from objects.tile import Tile


pygame.display.set_caption("2048 Game")




class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[None] * size for _ in range(size)]
        self.movement = False
        self.automation = False
        self.gravity = 0.9
        self.min_speed = 0.1
        self.move_speed = 10
        self.game_over = False

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                tile = Tile(r, c, TILE_SIZE, TILE_SIZE)
                self.grid[r][c] = tile

        self.add_new_tile()
        #self.add_new_tile()

    def add_new_tile(self):
        empty_tiles = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c].value == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            value = 2 if random.random() < 0.9 else 4
            tile = Tile(r, c, TILE_SIZE, TILE_SIZE)
            tile.set_value(value)
            self.grid[r][c] = tile

    @staticmethod
    def can_merge(a, b):
        return a == b and a != 0

    def slide_and_merge_row_horizontal(self, row, direction):
        new_row = [num for num in row if num != 0]
        if direction == 'right':
            new_row.reverse()
        merged_row = []
        skip = False
        for i in range(len(new_row)):
            if skip:
                skip = False
                continue
            if i + 1 < len(new_row) and self.can_merge(new_row[i], new_row[i + 1]):
                merged_row.append(new_row[i] * 2)
                skip = True
            else:
                merged_row.append(new_row[i])

        if direction == 'left':
            merged_row.extend([0] * (self.size - len(merged_row)))

        elif direction == 'right':
            merged_row.reverse()
            for i in range(self.size - len(merged_row)):
                merged_row.insert(0, 0)

        return merged_row

    @staticmethod
    def convert_rows_to_columns(rows):
        columns = []
        for c in range(len(rows)):
            column = []
            for r in range(len(rows[0])):
                column.append(rows[r][c])

            columns.append(column)

        return columns

    @staticmethod
    def convert_columns_to_rows(columns):
        rows = []
        for r in range(len(columns[0])):
            row = []
            for c in range(len(columns)):
                row.append(columns[c][r])

            rows.append(row)

        return rows

    def move(self, direction):
        if self.movement:
            return
        elif not self.can_move():
            self.game_over = True
            return

        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                tile = self.grid[r][c]
                tile.direction = direction
                self.movement = True

        """
        new_grid = []

        if direction == 'left' or direction == 'right':
            for row in self.grid:
                new_grid.append(self.slide_and_merge_row_horizontal(row, direction))

        elif direction == 'up' or direction == 'down':
            new_columns = []
            columns = self.convert_rows_to_columns(self.grid)

            for column in columns:
                if direction == 'down':
                    new_columns.append(self.slide_and_merge_row_horizontal(column, 'right'))
                elif direction == 'up':
                    new_columns.append(self.slide_and_merge_row_horizontal(column, 'left'))
                    
            new_grid = self.convert_columns_to_rows(new_columns)
        """

    def is_full(self):
        return all(cell.value != 0 for row in self.grid for cell in row)

    def can_move(self):
        if not self.is_full():
            return True
        for row in self.grid:
            for i in range(self.size - 1):
                if self.can_merge(row[i].value, row[i + 1].value):
                    return True
        for c in range(self.size):
            for r in range(self.size - 1):
                if self.can_merge(self.grid[r][c].value, self.grid[r + 1][c].value):
                    return True
        return False

    def draw(self):
        tiles = []
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                tile = self.grid[r][c]
                tiles.append(tile)

        [tile.draw() for tile in tiles if tile.direction is None]
        [tile.draw() for tile in tiles if tile.direction is not None]


def render_board(board):
    screen.fill(BACKGROUND_COLOR)

    if board.movement:
        board.movement = False
        for r in range(len(board.grid)):
            for c in range(len(board.grid[r])):
                tile = board.grid[r][c]
                if tile.direction is not None:
                    board.movement = True

        if not board.movement:
            board.add_new_tile()

    board.draw()

    if board.game_over:
        text = title_font.render("GAME OVER", True, TITLE_FONT_COLOR)
        rect = pygame.Rect(0, 0, WINDOW_SIZE, WINDOW_SIZE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

        text = font.render("Press R to restart game", True, TITLE_FONT_COLOR)
        rect = pygame.Rect(0, 0 + TITLE_FONT_SIZE, WINDOW_SIZE, WINDOW_SIZE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    pygame.display.update()
