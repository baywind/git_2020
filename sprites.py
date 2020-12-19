import pygame
import os, math

pygame.init()
pygame.display.set_caption('Спрайты')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill((200, 200, 0))

class Zombie(pygame.sprite.Sprite):
    path = os.path.join('images', "zombie.png")

    image = pygame.image.load(path)
    newidth = 100
    newhight = newidth * image.get_height() // image.get_width()
    image = pygame.transform.scale(image,(newidth,newhight))
    image = image.convert_alpha()

    def __init__(self, center, r, v, *group):
        super().__init__(*group)
        self.image = Zombie.image
        self.center = center
        self.r = r
        self.v = v
        self.a = 0
        self.rect = pygame.Rect(self.pos(),(self.newidth, self.newhight))

    def pos(self):
        x = self.center[0] + self.r * math.cos(self.a) - self.newidth // 2
        y = self.center[1] + self.r * math.sin(self.a) - self.newhight // 2
        return x,y

    def update(self, pos):
        self.a += self.v
        self.rect.x = self.center[0] + self.r * math.cos(self.a) - self.newidth // 2
        self.rect.y = self.center[1] + self.r * math.sin(self.a) - self.newhight // 2
        if pos and self.rect.collidepoint(pos):
            self.v = -self.v



fps = 60
clock = pygame.time.Clock()

running = True
all_sprites = pygame.sprite.Group()

monsters = pygame.sprite.Group()

zomb = Zombie((300,300), 150, 0.1, all_sprites, monsters)


while running:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

    screen.fill((0, 200, 200))
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()

    monsters.update(pos)

pygame.quit()
