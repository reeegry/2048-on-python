import pygame

class BuildGrid:

    def __init__(self, massive, SIZE_BLOCK, MARGIN, BLACK, WHITE, screen, empty_block, row, column, UP_BLOCK, score):
        self.massive = massive
        self.SIZE_BLOCK = SIZE_BLOCK
        self.MARGIN = MARGIN
        self.BLACK = BLACK
        self.WHITE = WHITE
        self.screen = screen
        self.empty_block = empty_block
        self.empty_block = ''
        self.row = row
        self.column = column
        self.UP_BLOCK = UP_BLOCK
        self.score = score

    def build_grid(self):
        for row in range(self.row):
            for column in range(self.column):
                x = column * self.SIZE_BLOCK + (column + 1) * self.MARGIN
                y = row * self.SIZE_BLOCK + (row + 1) * self.MARGIN + self.UP_BLOCK
                pygame.draw.rect(self.screen, self.WHITE, (x, y, self.SIZE_BLOCK, self.SIZE_BLOCK))
                font = pygame.font.SysFont('stxingkai', 320 // self.row)
                if self.massive[row][column] == 0:
                    text_1 = font.render(str(self.empty_block), True, self.BLACK)
                else:
                    text_1 = font.render(str(self.massive[row][column]), True, self.BLACK)
                self.screen.blit(text_1, (x, y))

    def score_count(self):
        font = pygame.font.SysFont('stxingkai', self.UP_BLOCK - 5)
        width = self.SIZE_BLOCK * self.column + self.MARGIN * (self.column + 1)
        height = self.UP_BLOCK
        up_block_surface = pygame.Surface((width, height))
        score_text = font.render(str(self.score), True, self.WHITE)
        score_place = score_text.get_rect(center=(width // 2, self.UP_BLOCK // 2))
        up_block_surface.blit(score_text, score_place)
        self.screen.blit(up_block_surface, (0, 0))

