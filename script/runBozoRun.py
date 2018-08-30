#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from core.character import Character, YaYou, Grognon, alban
from core.item import Item, Consumable, Drink, Cola, Chouffe
from core.code import Code, Html, Html3, Html5

Html = Html()
YaYou = YaYou()
Grognon = Grognon()

print YaYou.name
print Grognon.name

print YaYou.name + " defie " + Grognon.name + " !"
print "C´EST L´ HEURE DU  DUDUDUDUDUDELLLLLLL!!!!!"

Grognon.attack(YaYou)
YaYou.execute(Html,Grognon)

rdm = random.random()
# print str(rdm)
# YaYou.random()
# rdmG= Grognon.random()
if Grognon.random() > YaYou.random() :
    Grognon.attack(YaYou)

else:
    YaYou.execute(Html,Grognon)

# print str(rdmG)
# print str(rdmY)
