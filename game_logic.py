from math import ceil
import pygame
import sys
import grid
import methods
import my_menu

GRID_SIZE = 4

SIZE_BLOCK = 400 // GRID_SIZE
MARGIN = ceil(SIZE_BLOCK * 0.02)
WIDTH = HEIGHT = SIZE_BLOCK * GRID_SIZE + MARGIN * (GRID_SIZE + 1)
UP_BLOCK = 40

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255

screen = pygame.display.set_mode((WIDTH, HEIGHT + UP_BLOCK))
pygame.display.set_caption('2048')

mas = [[0] * GRID_SIZE for i in range(GRID_SIZE)]

Grid = grid.BuildGrid(mas, SIZE_BLOCK, MARGIN, BLACK, WHITE, screen, '', GRID_SIZE, GRID_SIZE, UP_BLOCK, 0)

methods.create_start_numbers(GRID_SIZE, Grid)

pygame.init()


def start_the_game():

    game_active = True
    add_2_or_4_on_grid = False

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:

                massive_old = Grid.massive.copy()

                if event.key == pygame.K_LEFT:
                    for row in range(len(Grid.massive)):
                        row_sorted = methods.sort_row_for_move_up_and_left(Grid.massive[row])
                        Grid.massive[row] = methods.multiplication_by_2_left(row_sorted, Grid)

                if event.key == pygame.K_RIGHT:
                    for row in range(len(Grid.massive)):
                        row_sorted = methods.sort_row_for_move_down_and_right(Grid.massive[row])
                        Grid.massive[row] = methods.multiplication_by_2_right(row_sorted, Grid)

                elif event.key == pygame.K_UP:
                    # Add a list that swaps columns and rows
                    massive_for_move_up = []
                    massive_for_move_up_sorted = []

                    methods.column_to_row(massive_for_move_up, Grid.massive)

                    for j in massive_for_move_up:
                        # First sort the list, then multiply by 2
                        massive_sorted = methods.sort_row_for_move_up_and_left(j)
                        massive_for_move_up_sorted.append(methods.multiplication_by_2_left(massive_sorted, Grid))

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
                        massive_for_move_down_sorted.append(methods.multiplication_by_2_right(j, Grid))

                    # Transpose massive_for_move_down_sorted
                    Grid.massive = list(map(list, zip(*massive_for_move_down_sorted)))

                if massive_old == Grid.massive:
                    add_2_or_4_on_grid = False
                else:
                    add_2_or_4_on_grid = True

        Grid.build_grid()
        Grid.score_count()

        pygame.display.flip()

        no_zeroes = 0
        # Change the column with a row to check for identity
        left_column_to_row_multiplication_check = []
        row_column_to_row_check = []
        methods.column_to_row(left_column_to_row_multiplication_check, Grid.massive)
        methods.column_to_row(row_column_to_row_check, Grid.massive)
        for row in range(len(Grid.massive)):
            if 0 not in Grid.massive[row]:
                no_zeroes += 1
            # If it is not possible to multiply a row or column by 2 (the rows are equal)
            # Then we reset the list, show the menu, reset the points
            if no_zeroes == GRID_SIZE and methods.multiplication_by_2_right(Grid.massive[row]) == Grid.massive[row]\
                    and methods.multiplication_by_2_right(left_column_to_row_multiplication_check[row]) == \
                                                          row_column_to_row_check[row]:
                Grid.massive = [[0] * GRID_SIZE for i in range(GRID_SIZE)]
                methods.create_start_numbers(GRID_SIZE, Grid)
                Grid.score = 0
                pygame.time.delay(750)
                my_menu.create_menu(start_the_game, screen)

        if add_2_or_4_on_grid:
            pygame.time.delay(120)
            methods.random_number(Grid)
            add_2_or_4_on_grid = False


if __name__ == '__main__':
    my_menu.create_menu(start_the_game, screen)
