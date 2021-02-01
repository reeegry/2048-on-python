import pygame
import sys
import grid
import methods

SIZE_BLOCK = 100
MARGIN = 5
WIDTH = HEIGHT = SIZE_BLOCK * 4 + MARGIN * 5

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

mas = [[0] * 4 for i in range(4)]

Grid = grid.BuildGrid(mas, SIZE_BLOCK, MARGIN, BLACK, WHITE, screen)

for j in range(3):
    methods.random_number(Grid)

pygame.init()


def game_active_function():

    game_active = True

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for row in Grid.massive:
                        row.sort(reverse=True)

                if event.key == pygame.K_RIGHT:
                    for row in Grid.massive:
                        row.sort()

                elif event.key == pygame.K_UP:
                    # Add a list that swaps columns and rows
                    massive_for_move_up = []
                    massive_for_move_up_sorted = []

                    for column in range(len(mas)):
                        massive_for_add = []
                        for row in range(len(mas)):
                            # Adding a row to Massive_for_move_up that was a column in mas
                            massive_for_add.append(Grid.massive[row][column])
                        massive_for_move_up.append(massive_for_add)

                    for j in massive_for_move_up:
                        massive_for_move_up_sorted.append(methods.sort_row_for_move_up(j))

                    # Transpose massive_for_move_up_sorted
                    Grid.massive = list(map(list, zip(*massive_for_move_up_sorted)))

                elif event.key == pygame.K_DOWN:
                    # Add a list swapping columns and rows
                    massive_for_move_down = []
                    massive_for_move_down_sorted = []

                    for column in range(len(mas)):
                        massive_for_add = []
                        for row in range(len(mas)):
                            # Add to massive_for_move_up a line that was a column in mas
                            massive_for_add.append(Grid.massive[row][column])
                        massive_for_move_down.append(massive_for_add)

                    for j in massive_for_move_down:
                        massive_for_move_down_sorted.append(methods.sort_row_for_move_down(j))

                    # Transpose massive_for_move_dow_sorted
                    Grid.massive = list(map(list, zip(*massive_for_move_down_sorted)))

        Grid.build_grid()

        pygame.display.flip()


if __name__ == '__main__':
    game_active_function()
