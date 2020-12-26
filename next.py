import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[False] * width for _ in range(height)]
        self.x0 = 20
        self.y0 = 20
        self.c_size = 50

    def set_view(self, left, top, cell_size):
        self.x0 = left
        self.y0 = top
        self.c_size = cell_size

    def render(self, scr):
        y = self.y0
        for n in range(len(self.board)):
            x = self.x0
            for m in range(len(self.board[0])):
                if self.board[n][m]:
                    pygame.draw.rect(scr, (255, 255, 255), (y + 1, x + 1, self.c_size - 1, self.c_size - 1), 0)
                else:
                    pygame.draw.rect(scr, (0, 0, 0), (y + 1, x + 1, self.c_size - 1, self.c_size - 1), 0)
                pygame.draw.rect(scr, (255, 255, 255), (y, x, self.c_size, self.c_size), 1)
                x += self.c_size
            y += self.c_size

    def get_cell(self, pos):
        x_f = pos[1] - self.x0
        y_f = pos[0] - self.y0
        if not (0 <= x_f <= self.width * self.c_size and 0 <= y_f <= self.height * self.c_size):
            return None
        x = x_f // self.c_size
        y = y_f // self.c_size
        return y, x

    def change_cell(self, pos):
        cell = board.get_cell(pos)
        if cell is not None:
            y, x = cell
            for j in range(0, len(self.board[0])):
                self.board[y][j] = not (self.board[y][j])
            for i in range(0, len(self.board)):
                if i != y:
                    self.board[i][x] = not (self.board[i][x])


pygame.init()
size = w, h = 400, 400
screen = pygame.display.set_mode(size)
pygame.display.flip()
board = Board(5, 6)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.change_cell(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
