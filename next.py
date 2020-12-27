import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    running = True
    sch = 1
    while running:
        f = pygame.font.Font(None, 100)
        t = f.render(str(sch), False, (255, 0, 0))
        screen.blit(t, (80, 70))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWEVENT_HIDDEN:
                sch += 1
                f = pygame.font.Font(None, 100)
                t = f.render(str(sch), False, (255, 0, 0))
                screen.blit(t, (80, 70))
                pygame.display.update()
        pygame.display.update()
    pygame.quit()
