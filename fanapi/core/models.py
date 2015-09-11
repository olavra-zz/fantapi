# -*- coding: utf-8 -*-
from django.db import models
import random


class Map(models.Model):

    name = models.CharField(max_length="100")
    map = []
    width = models.IntegerField()
    height = models.IntegerField()

    def generate(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(width)] for x in range(height)]

        for ypos in range(height):
            for xpos in range(width):
                tile = Terrain(x=xpos, y=ypos, map=self)
                tile.randomize()
                #tile.save()
                self.map[ypos][xpos] = tile

        self.generate_river(0, 0)

    def generate_river(self, x, y):

        print x, y
        while x < self.width and y < self.height:
            self.map[y][x].material = 3
            y = y + random.randint(0, 1)
            x = x + random.randint(0, 1)




    def display(self):
        for y in range(len(self.map)-1):
            for x in range(len(self.map[y])-1):
                print self.map[y][x].display(),
            print ""

class Terrain(models.Model):

    TERRAIN_TYPES = (
        (0, 'Field'),
        (1, 'Grass'),
        (2, 'Rock'),
        (3, 'River'),
    )

    x = models.IntegerField()
    y = models.IntegerField()
    material = models.IntegerField(choices=TERRAIN_TYPES)
    map = models.ForeignKey(Map)

    def randomize(self):
        self.material = random.randint(0, 2)

    def display(self):
        if self.material == 0:
            return "#"
        elif self.material == 1:
            return "^"
        elif self.material == 2:
            return "*"
        elif self.material == 3:
            return "~"





