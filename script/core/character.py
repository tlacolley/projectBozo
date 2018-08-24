#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Character(object):
    #                   ""  /255 /255/255 /99 /?
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

    def attack(self):
        pass

class Alban(Character):
    def __init__(self):
        Character.__init__(self, "Alban", "Male Alpha", 255, 255, 255, 255, 255, 100, 100)
        self.inventory = ["Chouffe"]


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




# Gandalf l aigrie lance son gros python