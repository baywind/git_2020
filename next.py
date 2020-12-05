import pygame


sch = 0
if False and __name__ == '__main__':
    c = input().split(" ")
    b = c[1]
    a = c[0]
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Неправильный формат ввода")
        sch = 1
        pygame.quit()
    if sch == 0:
        pygame.init()
        size = width, height = a, b
        screen = pygame.display.set_mode(size)

if sch == 0:
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, a - 2, b - 2), 0)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
pygame.quit()
