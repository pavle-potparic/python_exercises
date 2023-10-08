import pygame
import numpy as np


class Pole:
    POLE_LENGTH = 50
    MIN_AIM_LEN = 4
    MAX_AIM_LENGTH = 50
    POLE_WIDTH = 5

    def __init__(self, balls):
        self.balls = balls

        self.aiming = False
        self.mouseStart = 0
        self.mousePos = 0
        self.mouseTrav = 0
        self.ballPos = 0
        self.point1 = 0
        self.point2 = 0
        self.aimLen = 0


    def aim(self, pos):
        self.aiming = True
        self.mouseStart = pos

    def shoot(self):
        self.aiming = False
        self.balls.shoot(self.mouseTrav * -1 / 10)

    def setPos(self, pos):
        self.mousePos = pos


    def updateIfMoved(self):
        self.mouseTrav = self.mousePos - self.mouseStart
        self.aimLen = np.linalg.norm(self.mouseTrav)

        if self.aiming and self.aimLen > self.MIN_AIM_LEN:
            gameBall = self.balls.getGameBall()
            self.ballPos = gameBall.pos

            startRadius = self.aimLen + self.balls.RADIUS
            endRadius = startRadius + self.POLE_LENGTH


            uv = self.mouseTrav / self.aimLen

            self.point1 = (uv * startRadius) + self.ballPos
            self.point2 = (uv * endRadius) + self.ballPos

    def update(self):
        self.updateIfMoved()



    def render(self, screen, x, y):
        if self.aiming and self.aimLen > self.MIN_AIM_LEN:
            pygame.draw.line(screen, (200, 200, 200), (self.point1[0] + x, self.point1[1] + y), (self.point2[0] + x, self.point2[1] + y), self.POLE_WIDTH)