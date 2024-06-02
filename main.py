import sys
from objects.board import Board, render_board
from shared_resources import *


def main():
    board = Board(size=GRID_SIZE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    board.move('up')
                elif event.key == pygame.K_DOWN:
                    board.move('down')
                elif event.key == pygame.K_LEFT:
                    board.move('left')
                elif event.key == pygame.K_RIGHT:
                    board.move('right')
                elif event.key == pygame.K_r:
                    board = Board(size=GRID_SIZE)

        render_board(board)
        clock.tick(30)


if __name__ == "__main__":
    main()
