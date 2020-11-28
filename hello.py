import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True

    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))

    allpos = []
    save = True
    red = 0, 0

    fon = pygame.Surface(screen.get_size())

    while running:
        screen.fill((0, 0, 0))
        events = pygame.event.get()
        screen.blit(fon, (0, 0))
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                save = not save
            if event.type == pygame.MOUSEMOTION:
                if save:
                    pygame.draw.circle(fon, (0, 0, 255), event.pos, 20)
                    screen.blit(fon, (0, 0))
                else:
                    pygame.draw.circle(screen, (255, 0, 0), event.pos, 20)

        pygame.display.flip()
        clock.tick(60)
    print(len(allpos))

    pygame.quit()