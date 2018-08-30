#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Code(object):# les damage sont un ratio de l int du perso
    def __init__(self, name, description, damage, cost):
        self.name = name
        self.description = description
        self.damage = damage
        self.cost = cost

    def execute(self,user,target):
        #Must be implemented in child classes
        raise

class Html(Code):
    def __init__(self):
        Code.__init__(self,"HTML","Kes ke vou XV ¡!¿? jeu C code ¡!", 0.5, 1)

    def execute(self, user, target):
        print user.name + " execute le code " + self.name
        print self.description
        user.mp = user.mp - self.cost
        target.hp = target.hp - (user.int * self.damage)
        print "Depité par la mediocrité de ce code, " + target.name + " perd bon gré mal gré "+ str(user.int * self.damage) + " point de vitalité"
        print "Il reste " + str(target.hp) + " point de vitalité á " + target.name


class Html3(Code):
    def __init__(self):
        Code.__init__(self,"HTML3","Que croyez vous? Un jour je serai le meilleur codeur!!! ", 1, 3)

    def execute(self,user,target):
        print user.name+"execute le code"+self.name
        print self.description
        user.mp = user.mp - self.cost
        target.hp = target.hp - (user.int * self.damage)
        print "Rassuré par l´acceptabilité de ce code, " + target.name + " perd "+ str(user.int * self.damage) + "point de vitalité"


class Html5(Code):
    def __init__(self):
        Code.__init__(self,"HTML5","Je me suis tellement accoutumé ces jours passés à détacher mon esprit des sens, et j’ai si exactement remarqué qu’il y a fort peu de choses que l’on connaisse avec certitude touchant les choses corporelles, qu’il y en a beaucoup plus qui nous sont connues touchant l’esprit humain, et beaucoup plus encore de Dieu même, qu’il me sera maintenant aisé de détourner ma pensée de la considération des choses sensibles ou imaginables, pour la porter à celles qui, étant dégagées de toute matière, sont purement intelligibles.", 2, 5)

    def execute(self,user,target):
        print user.name+": Corniquedouille, une joute ! "
        print self.description
        user.mp = user.mp - self.cost
        target.hp = target.hp - (user.int * self.damage)
        print "Depité par la mediocrité de ce code, " + target.name + " perd bon gré mal gré "+ str(user.int * self.damage) + "point de vitalité"








# gros python
