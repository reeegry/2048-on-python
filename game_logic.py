from math import ceil
import pygame
import sys
import grid
import methods

GRID_SIZE = 4

SIZE_BLOCK = 400 // GRID_SIZE
MARGIN = ceil(SIZE_BLOCK * 0.02)
print(MARGIN)
WIDTH = HEIGHT = SIZE_BLOCK * GRID_SIZE + MARGIN * (GRID_SIZE + 1)

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

mas = [[0] * GRID_SIZE for i in range(GRID_SIZE)]

Grid = grid.BuildGrid(mas, SIZE_BLOCK, MARGIN, BLACK, WHITE, screen, '', GRID_SIZE, GRID_SIZE)

for j in range(GRID_SIZE):
    methods.random_number(Grid)

pygame.init()


def game_active_function():

    game_active = True
    add_2_or_4_on_grid = False
    count = 0

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                sys.exit()
            if event.type == pygame.KEYDOWN:

                massive_old = Grid.massive.copy()

                if event.key == pygame.K_LEFT:
                    for row in range(len(Grid.massive)):
                        row_sorted = methods.sort_row_for_move_up_and_left(Grid.massive[row])
                        Grid.massive[row] = methods.multiplication_by_2_left(row_sorted)

                if event.key == pygame.K_RIGHT:
                    for row in range(len(Grid.massive)):
                        row_sorted = methods.sort_row_for_move_down_and_right(Grid.massive[row])
                        Grid.massive[row] = methods.multiplication_by_2_right(row_sorted)

                elif event.key == pygame.K_UP:
                    # Add a list that swaps columns and rows
                    massive_for_move_up = []
                    massive_for_move_up_sorted = []

                    methods.column_to_row(massive_for_move_up, Grid.massive)

                    for j in massive_for_move_up:
                        # First sort the list, then multiply by 2
                        massive_sorted = methods.sort_row_for_move_up_and_left(j)
                        massive_for_move_up_sorted.append(methods.multiplication_by_2_left(massive_sorted))

                    # Transpose massive_for_move_up_sorted
                    Grid.massive = list(map(list, zip(*massive_for_move_up_sorted)))

                elif event.key == pygame.K_DOWN:
                    # Add a list swapping columns and rows
                    massive_for_move_down = []
                    massive_for_move_down_sorted = []

                    methods.column_to_row(massive_for_move_down, Grid.massive)

                    for j in massive_for_move_down:
                        # First sort the list, then multiply by 2
                        j = methods.sort_row_for_move_down_and_right(j)
                        massive_for_move_down_sorted.append(methods.multiplication_by_2_right(j))

                    # Transpose massive_for_move_down_sorted
                    Grid.massive = list(map(list, zip(*massive_for_move_down_sorted)))

                if massive_old == Grid.massive:
                    add_2_or_4_on_grid = False
                else:
                    add_2_or_4_on_grid = True

        Grid.build_grid()

        pygame.display.flip()

        if add_2_or_4_on_grid:
            pygame.time.delay(120)
            methods.random_number(Grid)
            add_2_or_4_on_grid = False


if __name__ == '__main__':
    game_active_function()
