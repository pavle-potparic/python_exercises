import pygame
import numpy as np
from numpy.linalg import norm
import math
import sys

class TablePhysics:
    OUTER_WIDTH = 272
    OUTER_HEIGHT = 155
    INNER_WIDTH = 234
    INNER_HEIGHT = 117

    HOLE_WIDTH = 15
    HOLE_HEIGHT = 15
    CHAMFER = 4

    holeLineIndexes = [1, 6, 11, 15, 20, 25]

    def __init__(self, width):
        self.width = width

        scaleFactor = self.width / self.OUTER_WIDTH
        self.height = scaleFactor * self.OUTER_HEIGHT
        self.horSpacing = (self.OUTER_WIDTH - self.INNER_WIDTH) / 2 * scaleFactor
        self.verSpacing = (self.OUTER_HEIGHT - self.INNER_HEIGHT) / 2 * scaleFactor


        self.HOR_SPACING = (self.OUTER_WIDTH - self.INNER_WIDTH) // 2
        self.VER_SPACING = (self.OUTER_HEIGHT - self.INNER_HEIGHT) // 2

        self.HOLE_WIDTH_T = math.sqrt(1/2) * self.HOLE_WIDTH
        self.HOLE_HEIGHT_T = math.sqrt(1/2) * self.HOLE_HEIGHT


        startPoint = np.array([self.HOR_SPACING, self.VER_SPACING])


        self.pointList = []


        p1 = np.array([startPoint[0], startPoint[1] + self.HOLE_WIDTH_T])
        p2 = np.array([p1[0] - self.HOLE_HEIGHT_T, p1[1] - self.HOLE_HEIGHT_T])
        p3 = np.array([p2[0] + self.HOLE_WIDTH_T, p2[1] - self.HOLE_WIDTH_T])
        p4 = np.array([startPoint[0] + self.HOLE_WIDTH_T, startPoint[1]])

        p5 = np.array([startPoint[0] + self.INNER_WIDTH / 2 - self.HOLE_WIDTH / 2 - self.CHAMFER, startPoint[1]])
        p6 = np.array([startPoint[0] + self.INNER_WIDTH / 2 - self.HOLE_WIDTH / 2, startPoint[1] - self.CHAMFER])

        p7 = np.array([p6[0], p6[1] - self.HOLE_HEIGHT + self.CHAMFER])

        self.pointList.append(p1)
        self.pointList.append(p2)
        self.pointList.append(p3)
        self.pointList.append(p4)
        self.pointList.append(p5)
        self.pointList.append(p6)
        self.pointList.append(p7)


        for point in reversed(self.pointList):
            newPoint = np.array([self.OUTER_WIDTH - point[0], point[1]])
            self.pointList.append(newPoint)

        for point in reversed(self.pointList):
            newPoint = np.array([point[0], self.OUTER_HEIGHT - point[1]])
            self.pointList.append(newPoint)


        self.pointList = self.scalePointList(self.pointList, scaleFactor)


        self.intersectingLines = []

    def scalePointList(self, pointList, scale):
        newPoints = []
        for point in pointList:
            point = point * scale
            newPoints.append(point)
        return newPoints

    def calcDistPointToLine(self, p1, p2, p3):
        return abs(np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1))



    def isCircleInLine(self, p1, p2, p3, radius):
        intersecting = False
        mirrorVektor = 0
        intersectionLength = 0

        pointToLineDiagDist = self.calcDistPointToLine(p1, p2, p3) - radius

        if pointToLineDiagDist <= 0:

            lineDir = p1-p2


            diagonalVec = np.array([-lineDir[1], lineDir[0]])


            dp1 = p1 + diagonalVec
            dp2 = p2 + diagonalVec

            dLineDist1 = self.calcDistPointToLine(p1, dp1, p3)
            dLineDist2 = self.calcDistPointToLine(p2, dp2, p3)

            lineDist1 = np.linalg.norm(p1 - p3)
            lineDist2 = np.linalg.norm(p2 - p3)

            if dLineDist1 + dLineDist2 <= np.linalg.norm(p2-p1) + 1:
                intersecting = True
                mirrorVektor = p2 - p1
                intersectionLength = abs(pointToLineDiagDist)


            elif lineDist1 <= radius:
                intersecting = True
                mirrorVektor = p1 - p3
                mirrorVektor = np.array([-mirrorVektor[1], mirrorVektor[0]])
                intersectionLength = abs(np.linalg.norm(p1 - p3) - radius)

            elif lineDist2 <= radius:
                intersecting = True
                mirrorVektor = p2 - p3
                mirrorVektor = np.array([-mirrorVektor[1], mirrorVektor[0]])
                intersectionLength = abs(np.linalg.norm(p2 - p3) - radius)

        return intersecting, intersectionLength, mirrorVektor


    def getMirrorVektor(self, point, radius):
        mirrorVektors = []
        inHole = False
        for i in range(0, len(self.pointList)):


            p1 = self.pointList[i]
            p2Index = i + 1
            if p2Index >= len(self.pointList):
                p2Index = 0
            p2 = self.pointList[p2Index]

            intersecting, howMuch, mirrorVektor = self.isCircleInLine(p1, p2, point, radius)

            if intersecting:



                for lineIndex in self.holeLineIndexes:
                    if lineIndex == i:
                        inHole = True
                        break


                mirrorVektors.append((mirrorVektor, howMuch))
                self.intersectingLines.append((p1, p2))
                break

        return mirrorVektors, inHole

    def update(self):
        pass


    def render(self, screen):
        pygame.draw.polygon(screen, (0, 0, 0), self.pointList, 1)

        for line in self.intersectingLines:
            pygame.draw.line(screen, (255, 0, 0), line[0], line[1], 1)



if __name__ == "__main__":
    tablePhysics = TablePhysics(1000)