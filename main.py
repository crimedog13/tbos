import pygame
import sys
import time
import random
import colorsys
import math
from pygame.math import Vector2
from pygame.locals import *
from bird import Bird

def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((640,480), 0, 32)
    pygame.display.set_caption("Two Birds, One Stone")
    pygame.display.set_icon(Bird().sprite)




