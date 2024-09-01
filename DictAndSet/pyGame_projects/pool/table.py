import pygame

#own imports
from balls import Balls
from pole import Pole
from tablePhysics import TablePhysics


class Table:

    def __init__(self, width):
        self.width = width

        self.tablePhysics = TablePhysics(self.width)
        self.height = self.tablePhysics.height
        self.balls = Balls(self.width, self.height)

        self.pole = Pole(self.balls)


        self.tableImg = pygame.image.load('assets/table2.jpg')
        self.tableImg = self.tableImg.convert()
        self.tableImg = pygame.transform.scale(self.tableImg, (self.width, int(self.height)))


        self.preRender()

    def update(self):
        self.balls.update()
        self.pole.update()


        self.tablePhysics.intersectingLines = []
        for ball in self.balls.getMaybeIntersectingBalls(self.tablePhysics.horSpacing, self.tablePhysics.verSpacing):

            mirrorVectors, inHole = self.tablePhysics.getMirrorVektor(ball.index, ball.RADIUS)


            if inHole:
                self.balls.removeBall(ball)


            for mirrorVector in mirrorVectors:
                ball.mirror(mirrorVector[0], mirrorVector[1])

    def preRender(self):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.blit(self.tableImg, (0, 0))



    def render(self, screen, x, y):

        tableSurf = pygame.Surface((self.width, self.height))
        tableSurf.blit(self.surface, (0, 0))

        self.balls.render(tableSurf)
        screen.blit(tableSurf, (x, y))

        self.pole.render(screen, x, y)