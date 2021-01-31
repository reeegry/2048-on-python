import pygame

class BuildGrid:
    def __init__(self, massive, SIZE_BLOCK, MARGIN, BLACK, WHITE, screen):
        self.massive = massive
        self.SIZE_BLOCK = SIZE_BLOCK
        self.MARGIN = MARGIN
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.screen = screen

    def build_grid(self):
        for row in range(4):
            for column in range(4):
                x = column * self.SIZE_BLOCK + (column + 1) * self.MARGIN
                y = row * self.SIZE_BLOCK + (row + 1) * self.MARGIN
                pygame.draw.rect(self.screen, self.WHITE, (x, y, self.SIZE_BLOCK, self.SIZE_BLOCK))
                font = pygame.font.SysFont('stxingkai', 80)
                text_1 = font.render(str(self.massive[row][column]), True, self.BLACK)
                self.screen.blit(text_1, (x, y))