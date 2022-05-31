import pygame as pg
import os
import main as main
import load as load

class Bird(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load.loadSprite()
