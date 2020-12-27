import pygame
import sys, os, math, random

FPS = 50
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Марио')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

class Cell:
    box = load_image("box.png")
    grass = load_image("grass.png")
    open = False
    mine = False

    def __init__(self, type):
        if type == '#':
            self.image = Cell.box
            self.can_walk = False
        elif type == '.':
            self.image = Cell.grass
            self.can_walk = True


class Board:
    # создание поля
    def __init__(self, level):
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 50

        self.width = len(level[0])
        self.height = len(level)

        self.board = []
        for y,s in enumerate(level):
            row = []
            for x,c in enumerate(s):
                if c == '@':
                    c = '.'
                    self.player = Player(y, x, self.cell_size)
                row.append(Cell(c))
            self.board.append(row)


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
                screen.blit(cell.image, (x, y))
                x += self.cell_size
            y += self.cell_size
        self.player.draw(self)

    # def get_cell(self, pos):
    #     x_ref = pos[0] - self.left
    #     y_ref = pos[1] - self.top
    #     x = x_ref // self.cell_size
    #     y = y_ref // self.cell_size
    #     if x < 0 or x >= self.width or y < 0 or y > self.height:
    #         raise IndexError()
    #     return y, x

    def __getitem__(self, item):
        x, y = item
        return self.board[x][y]

    def __setitem__(self, key, value):
        x, y = key
        self.board[x][y] = value


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def level():
    level_map = load_level("level.txt")
    board = Board(level_map)
    screen.fill((0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # начинаем игру
                elif event.key == pygame.K_UP:
                    new_y = board.player.y - 1
                    if board.board[new_y][board.player.x].can_walk:
                        board.player.y -= 1
                elif event.key == pygame.K_DOWN:
                    board.player.y += 1
                elif event.key == pygame.K_LEFT:
                    board.player.x -= 1
                elif event.key == pygame.K_RIGHT:
                    board.player.x += 1

        w_c = width // 2
        c_c = board.cell_size // 2
        p_l = board.cell_size * board.player.x

        board.left = w_c - (c_c + p_l)

        board.top = height // 2 - (board.cell_size // 2 + board.cell_size * board.player.y)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)

class Player:
    image = load_image("mar.png")

    def __init__(self, y, x, cell_size):
        self.y = y
        self.x = x
        self.dy = cell_size // 2 - Player.image.get_height() // 2
        self.dx = (cell_size - Player.image.get_width()) // 2

    def draw(self, board: Board):
        draw_y = board.top + board.cell_size * self.y + self.dy
        draw_x = board.left + board.cell_size * self.x + self.dx
        screen.blit(Player.image, (draw_x,draw_y))


while True:
    start_screen()
    level()