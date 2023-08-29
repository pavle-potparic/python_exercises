import pygame

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
                if self.rect.collidepoint(event.pos):
                    self.callback()


def on_click():
    print("ovo radi")


pygame.init()
screen = pygame.display.set_mode((650, 600))

sprite = ClickableSprite(pygame.Surface((20, 20)), 150, 45, on_click)
a1 = pygame.sprite.GroupSingle(sprite)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    a1.update(events)
    screen.fill((255, 255, 255))
    a1.draw(screen)
    pygame.display.update()

pygame.quit()