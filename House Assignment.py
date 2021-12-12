#House Assignment
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(100, 100)

import math

import pygame
pygame.init()

#Colours that will be used
SKY = (145, 202, 255)
SUN = (255, 255, 0)
GRASS = (136, 222, 150)
HOUSE = (189, 129, 130)
FENCE = (178, 103, 0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EASTER_PINK = (255, 152, 204)
EASTER_BLUE = (0, 222, 255)
EASTER_GREEN = (0, 255, 186)
EASTER_YELLOW = (255, 237, 0)
EASTER_PURPLE = (216, 164, 255)


SIZE = (1000, 700) #defines the variable for the size of the screen
screen = pygame.display.set_mode(SIZE)

#Create sky
screen.fill (SKY) #Makes the sky a blue colour

#Create sun
pygame.draw.circle(screen, SUN, (930,70), 50)

#Create Clouds
pygame.draw.arc(screen, BLACK, (367, 20, 120, 210), math.radians(120), math.radians(210), 6)

#Create Grass
pygame.draw.rect(screen, GRASS, (0, 380, 1000, 340))

#Create House
pygame.draw.rect(screen, HOUSE, (290, 300, 500, 200))

#Create Dog House
pygame.draw.polygon(screen, EASTER_PURPLE, ((50, 470), (890, 490), (990, 490)))
pygame.draw.rect(screen, EASTER_PINK, (890, 415, 100, 25))
pygame.draw.rect(screen, EASTER_BLUE, (890, 440, 100, 25))
pygame.draw.rect(screen, EASTER_GREEN, (890, 465, 100, 25))
pygame.draw.rect(screen, EASTER_YELLOW, (890, 490, 100, 25))




# Update the interface
pygame.display.flip()
pygame.event.get()

pygame.time.wait(200000)  # pause for three seconds so we can see it
pygame.quit()           # pygame likes to crash computers when you don't
            # quit()
