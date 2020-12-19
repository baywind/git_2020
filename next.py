import pygame

try:
    size = width, height = tuple(map(int, input().split()))
except ValueError:
    print('Неправильный формат ввода')
else:
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Прямоугольник')
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, width - 2, height - 2), 0)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
