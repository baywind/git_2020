import pygame

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        y = self.top
        for row in self.board:
            x = self.left
            for cell in row:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (x, y, self.cell_size, self.cell_size), 1)
                if cell:
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (x + 2, y + 2, self.cell_size - 4, self.cell_size - 4), )

                x += self.cell_size
            y += self.cell_size

    def get_cell(self, pos):
        x_ref = pos[0] - self.left
        y_ref = pos[1] - self.top
        x = x_ref // self.cell_size
        y = y_ref // self.cell_size
        if x < 0 or x >= self.width or y < 0 or y > self.height:
            raise IndexError()
        return y, x

    def __getitem__(self, item):
        x, y = item
        return self.board[x][y]

    def __setitem__(self, key, value):
        x, y = key
        self.board[x][y] = value


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


board = Board(4, 3)
board.set_view(100, 100, 50)
running = True
while running:
    screen.fill((0, 0, 0))
    board.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen,(255,0,0),event.pos,10)
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                cell = board.get_cell(event.pos)
                board[cell] = not board[cell]
            except IndexError:
                print("Мимо!")

    pygame.display.flip()


pygame.quit()