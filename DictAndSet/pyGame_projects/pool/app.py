import pygame


class App:
    WIDTH = 1300
    HEIGHT = 850
    FPS = 120
    TITLE = "Snake"

    def __init__(self, startScene):
        self.startScene = startScene
        self.activeScene = 0
        self.running = True
        self.screen = 0

    def changeScene(self, newScene):
        if self.activeScene and self.activeScene.isActive:
            self.activeScene.stop()
        self.activeScene = newScene(self, self.WIDTH, self.HEIGHT)
        self.activeScene.start()

    def stop(self):
        self.running = False

    def start(self):

        clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(self.TITLE)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.changeScene(self.startScene)

        while self.running:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.activeScene.handleEvent(events)
            self.activeScene.update()
            self.activeScene.render(self.screen)

            pygame.display.flip()

            clock.tick_busy_loop(self.FPS)
