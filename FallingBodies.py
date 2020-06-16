"""Code simulates falling balls with air drag proportional to velocity square."""

### Sahil Islam ###
### 16/06/2020 ###

import pygame
import numpy as np

pygame.init()
width = 800
height = 650
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height / 2.))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
lightblue = (153, 217, 234)
clock = pygame.time.Clock()


def ball(x, y, m):
    r = m  # Radius and mass are made proportional for visual understanding.
    pygame.draw.circle(screen, black, (int(x), int(y)), r, 2)


def drag(cd, v, m):
    a = float(cd * v * v) / m
    return a


g = 9.8
c = 1.1

no_of_balls = 5
xPos = np.random.randint(20, width - 20, no_of_balls)
mass = np.random.randint(10, 50, no_of_balls)
yPos = np.zeros(no_of_balls)

xVel = np.zeros(no_of_balls)
yVel = np.zeros(no_of_balls)

xAcc = np.zeros(no_of_balls)
yAcc = np.zeros(no_of_balls)

dt = 0.1  # Time step for better prcession.

while True:

    screen.fill(white)
    surface.fill(lightblue)
    screen.blit(surface, (0, height / 2.))
    for i in range(len(xPos)):

        ball(xPos[i], yPos[i], mass[i])

        yAcc[i] = +g - drag(0, yVel[i], mass[i])

        if yPos[i] + mass[i] >= height / 2.0:
            yAcc[i] = +g - drag(c, yVel[i], mass[i])

        xPos[i] += dt * xVel[i]
        yPos[i] += dt * yVel[i]
        xVel[i] += dt * xAcc[i]
        yVel[i] += dt * yAcc[i]

        if yPos[i] + mass[i] >= height:
            yVel[i] *= 0
            xVel[i] *= 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()
    clock.tick(50)
