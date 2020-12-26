import pygame
import os, math, random

pygame.init()
pygame.display.set_caption('Спрайты')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill((200, 200, 0))

balls = pygame.sprite.Group()

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, r=10):
        super().__init__(all_sprites, balls)
        self.image = pygame.Surface((r*2, r*2), flags=pygame.SRCALPHA)
        pygame.draw.circle(self.image,(255,0,0),(r,r),r)
        self.rect = pygame.Rect(x - r, y - r, r*2, r*2)
        self.vx = random.randint(-5,5)
        self.vy = random.randint(-5, 5)
        self.radius = r
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, pos):
        self.rect = self.rect.move(self.vx, self.vy)


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
        self.mask = pygame.mask.from_surface(self.image)

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
            self.image = pygame.transform.flip(self.image,True,False)
        if pygame.sprite.spritecollide(self,
                        balls, True, collided=pygame.sprite.collide_mask):
            # pygame.transform.flip(self.image, False, True)
            screen.fill((0, 0, 0))



fps = 60
clock = pygame.time.Clock()

running = True
all_sprites = pygame.sprite.Group()

monsters = pygame.sprite.Group()

zomb = Zombie((300,300), 150, 0.01, all_sprites, monsters)


while running:
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if event.button == 3:
                Ball(*event.pos, 10)

    screen.fill((0, 200, 200))
    clock.tick(fps)
    all_sprites.update(pos)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()
