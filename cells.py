import pygame

class Cell:
    open = False
    mine = False

    def __bool__(self):
        return self.mine

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[Cell() for _ in range(width)] for _ in range(height)]
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
                if cell.mine:
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

    def neighbours(self, y, x):
        rows = self.board[max(0, y-1):y+2]
        total = 0
        for row in rows:
            cells = row[max(0, x-1):x+2]
            total += sum(map(bool, cells))
        return total

    def next_generation(self):
        newgen = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                total = self.neighbours(x,y)
                if total == 3 or (self[x,y] and total == 4):
                    newgen[x][y] = True
        self.board = newgen

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


board = Board(10, 10)
# board.set_view(100, 100, 50)
running = True
mouse = (0, 0)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            cell = board.get_cell(event.pos)
            if event.button == 3:
                try:
                    # print(board.neighbours(*cell))
                    board[cell].mine = not board[cell].mine
                except IndexError:
                    print("Мимо!")
            elif event.button == 1:
                print(board.neighbours(*cell))
        # if event.type == pygame.KEYDOWN:
        #     board.next_generation()

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.draw.circle(screen, (255, 0, 0), mouse, 5)
    clock.tick(30)
    pygame.display.flip()

pygame.quit()