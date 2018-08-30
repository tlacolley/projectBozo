#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Character(object):
    #                   ""  /255 /255/255 /99 /? (2^8-1)
    def __init__(self, name, sexe, hp, mp, str, int, res, lvl, xp ):
        self.name = name
        self.sexe = sexe
        self.hp = hp
        self.mp = mp
        self.str = str
        self.int = int
        self.res = res
        self.lvl = lvl
        self.xp = xp
        self.inventory = []
        self.x = None
        self.y = None

    def use(self,item):
        print user.name + "utilise" + item.name
        item.use(self)

    def attack(self,target):
        target.hp = target.hp - (self.str * 0.5)
        print  self.name + " lance une attaque et inflige "+ str(self.str * 0.5) + " point de dégats"
        print "Il reste " + str(target.hp) + " point de vitalité á " + target.name

    def execute(self, code, target):
        code.execute(self, target)

    def random(self):
        return random.random()


#  Class Starter     "name" /15 /15 /15 /15
class YaYou(Character):
    def __init__(self):
        Character.__init__(self, "YaYou", "Male", 6, 12, 5, 15, 10, 1, 0)
        self.inventory = ["Zippo","FFBE"]


class Grognon(Character):
   def __init__(self):
        Character.__init__(self,"Grognon", "Male", 8, 10, 10, 10, 8, 1, 0)
        self.inventory = ["Dick","Knife","FFBE"]


class Carolin(Character):
   def __init__(self):
        Character.__init__(self,"Carolin", "Female", 10, 8, 7, 8, 7, 1, 0)
        self.inventory = ["serviette hygienique"]


alban = Character("Alban aka Galban l´aigrie", "Male Alpha", 255, 255, 255, 255, 255, 100, 100)
alban.inventory = ["Chouffe"]
# Gandalf l aigrie lance son gros python
