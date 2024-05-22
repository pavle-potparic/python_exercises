import pygame

pygame.init()

width = 650
height = 600

screen = pygame.display.set_mode((width, height))

screen.fill((9, 72, 189))

pygame.display.update()

pygame.display.update()


class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.index):
                    self.callback()


def on_click():
    print("majmune")



pygame.init()
screen = pygame.display.set_mode((width, height))

sprite1 = ClickableSprite(pygame.Surface((150, 45)), 20, 20, on_click)
a1 = pygame.sprite.GroupSingle(sprite1)

sprite2 = ClickableSprite(pygame.Surface((150, 45)), 40, 70, on_click)
a2 = pygame.sprite.GroupSingle(sprite2)

sprite3 = ClickableSprite(pygame.Surface((150, 45)), 60, 120, on_click)
a3 = pygame.sprite.GroupSingle(sprite3)

sprite4 = ClickableSprite(pygame.Surface((150, 45)), 80, 170, on_click)
a4 = pygame.sprite.GroupSingle(sprite4)

sprite5 = ClickableSprite(pygame.Surface((150, 45)), 100, 220, on_click)
a = pygame.sprite.GroupSingle(sprite5)

sprite6 = ClickableSprite(pygame.Surface((150, 45)), 485, 20, on_click)
b1 = pygame.sprite.GroupSingle(sprite6)

sprite7 = ClickableSprite(pygame.Surface((150, 45)), 465, 70, on_click)
b2 = pygame.sprite.GroupSingle(sprite7)

sprite8 = ClickableSprite(pygame.Surface((150, 45)), 445, 120, on_click)
b3 = pygame.sprite.GroupSingle(sprite8)

sprite9 = ClickableSprite(pygame.Surface((150, 45)), 425, 170, on_click)
b4 = pygame.sprite.GroupSingle(sprite9)

sprite10 = ClickableSprite(pygame.Surface((150, 45)), 405, 220, on_click)
b = pygame.sprite.GroupSingle(sprite10)

sprite11 = ClickableSprite(pygame.Surface((150, 45)), 20, 535, on_click)
c1 = pygame.sprite.GroupSingle(sprite11)

sprite12 = ClickableSprite(pygame.Surface((150, 45)), 40, 485, on_click)
c2 = pygame.sprite.GroupSingle(sprite12)

sprite13 = ClickableSprite(pygame.Surface((150, 45)), 60, 435, on_click)
c3 = pygame.sprite.GroupSingle(sprite13)

sprite14 = ClickableSprite(pygame.Surface((150, 45)), 80, 385, on_click)
c4 = pygame.sprite.GroupSingle(sprite14)

sprite15 = ClickableSprite(pygame.Surface((150, 45)), 100, 335, on_click)
c = pygame.sprite.GroupSingle(sprite15)

sprite16 = ClickableSprite(pygame.Surface((150, 45)), 485, 535, on_click)
d1 = pygame.sprite.GroupSingle(sprite16)

sprite17 = ClickableSprite(pygame.Surface((150, 45)), 465, 485, on_click)
d2 = pygame.sprite.GroupSingle(sprite17)

sprite18 = ClickableSprite(pygame.Surface((150, 45)), 445, 435, on_click)
d3 = pygame.sprite.GroupSingle(sprite18)

sprite19 = ClickableSprite(pygame.Surface((150, 45)), 425, 385, on_click)
d4 = pygame.sprite.GroupSingle(sprite19)

sprite20 = ClickableSprite(pygame.Surface((150, 45)), 405, 335, on_click)
d = pygame.sprite.GroupSingle(sprite20)

sprite21 = ClickableSprite(pygame.Surface((160, 40)), 245, 280, on_click)
end = pygame.sprite.GroupSingle(sprite21)


def run_sprite(velicina, x, y):
    char = ClickableSprite(pygame.Surface(velicina), x, y, on_click)
    return char


running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    sprite1.image.fill("Blue")
    a1 = pygame.sprite.GroupSingle(sprite1)
    a1.update(events)
    screen.fill((9, 72, 189))
    a1.draw(screen)

    a2 = pygame.sprite.GroupSingle(sprite2)
    a2.update(events)
    screen.fill((9, 72, 189))
    a2.draw(screen)

    a3 = pygame.sprite.GroupSingle(sprite3)
    a3.update(events)
    screen.fill((9, 72, 189))
    a3.draw(screen)

    a4 = pygame.sprite.GroupSingle(sprite4)
    a4.update(events)
    screen.fill((9, 72, 189))
    a4.draw(screen)

    a = pygame.sprite.GroupSingle(sprite5)
    a.update(events)
    screen.fill((9, 72, 189))
    a.draw(screen)

    b1 = pygame.sprite.GroupSingle(sprite6)
    b1.update(events)
    screen.fill((9, 72, 189))
    b1.draw(screen)

    b2 = pygame.sprite.GroupSingle(sprite7)
    b2.update(events)
    screen.fill((9, 72, 189))
    b2.draw(screen)

    b3 = pygame.sprite.GroupSingle(sprite8)
    b3.update(events)
    screen.fill((9, 72, 189))
    b3.draw(screen)

    b4 = pygame.sprite.GroupSingle(sprite9)
    b4.update(events)
    screen.fill((9, 72, 189))
    b4.draw(screen)

    b = pygame.sprite.GroupSingle(sprite10)
    b.update(events)
    screen.fill((9, 72, 189))
    b.draw(screen)

    c1 = pygame.sprite.GroupSingle(sprite11)
    c1.update(events)
    screen.fill((9, 72, 189))
    c1.draw(screen)

    c2 = pygame.sprite.GroupSingle(sprite12)
    c2.update(events)
    screen.fill((9, 72, 189))
    c2.draw(screen)

    c3 = pygame.sprite.GroupSingle(sprite13)
    c3.update(events)
    screen.fill((9, 72, 189))
    c3.draw(screen)

    c4 = pygame.sprite.GroupSingle(sprite14)
    c4.update(events)
    screen.fill((9, 72, 189))
    c4.draw(screen)

    c = pygame.sprite.GroupSingle(sprite15)
    c.update(events)
    screen.fill((9, 72, 189))
    c.draw(screen)

    d1 = pygame.sprite.GroupSingle(sprite16)
    d1.update(events)
    screen.fill((9, 72, 189))
    d1.draw(screen)

    d2 = pygame.sprite.GroupSingle(sprite17)
    d2.update(events)
    screen.fill((9, 72, 189))
    d2.draw(screen)

    d3 = pygame.sprite.GroupSingle(sprite18)
    d3.update(events)
    screen.fill((9, 72, 189))
    d3.draw(screen)

    d4 = pygame.sprite.GroupSingle(sprite19)
    d4.update(events)
    screen.fill((9, 72, 189))
    d4.draw(screen)

    d = pygame.sprite.GroupSingle(sprite20)
    d.update(events)
    screen.fill((9, 72, 189))
    d.draw(screen)

    end = pygame.sprite.GroupSingle(sprite21)
    end.update(events)
    screen.fill((9, 72, 189))
    end.draw(screen)

pygame.quit()
