import pygame

if __name__ == '__main__':
    try:
        w, n = map(int, input().split())
        if w == 0:
            raise ValueError
    except:
        print('Неправильный формат ввода')
    else:
        pygame.init()
        size = x, x = w * n * 2 + 1, w * n * 2 + 1
        scr = pygame.display.set_mode(size)
        pygame.display.set_caption('Вы же не снизите за цвета флага Российской Империи, верно?')
        while pygame.event.wait().type != pygame.QUIT:
            scr.fill((255, 255, 255))
            for i in range(n):
                clr = ['black', 'orange', 'white']
                pygame.draw.circle(scr, pygame.Color(clr[i % 3]), (x // 2 + 1, x // 2 + 1), w * (n - i))
            pygame.display.flip()

        pygame.quit()