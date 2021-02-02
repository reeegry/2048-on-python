import pygame

class BuildGrid:

    empty_block = ''

    def __init__(self, massive, SIZE_BLOCK, MARGIN, BLACK, WHITE, screen, empty_block):
        self.massive = massive
        self.SIZE_BLOCK = SIZE_BLOCK
        self.MARGIN = MARGIN
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.screen = screen
        self.empty_block = empty_block
        self.empty_block = ''

    def build_grid(self):
        for row in range(4):
            for column in range(4):
                x = column * self.SIZE_BLOCK + (column + 1) * self.MARGIN
                y = row * self.SIZE_BLOCK + (row + 1) * self.MARGIN
                pygame.draw.rect(self.screen, self.WHITE, (x, y, self.SIZE_BLOCK, self.SIZE_BLOCK))
                font = pygame.font.SysFont('stxingkai', 80)
                if self.massive[row][column] == 0:
                    text_1 = font.render(str(self.empty_block), True, self.BLACK)
                else:
                    text_1 = font.render(str(self.massive[row][column]), True, self.BLACK)
                self.screen.blit(text_1, (x, y))