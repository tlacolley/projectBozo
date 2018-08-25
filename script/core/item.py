#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name):
        self.name = name
        # self.use =

    def use(self,user):
        #Must be implemented in child classes
        raise


class Consomable(Item):
    def __init__(self,name, description, effect):
        Item.__init__(self,name)
        pass


class Chouffe(Consomable):
    def __init__(self):
        Consomable.__init__(self,"Chouffe", "La bière belge du lutin au bonnet rouge ! A l'oeil Robe blonde dorée avec une épaisse mousse blanche.Au nez Arômes d'épices et d'agrumes. A la bouche Notes houblonnées, fruitées et épicées.","Bourrer")

    def use(self,user):
        user.hp = user.hp/2
        user.mp = user.mp/2
        user.str = user.str/2
        user.int = user.int/2
        user.res = user.res/2


class Clothes(Item):
                        #                       Pour la duration je sais pas si on le fait en nb de combat ou en resistance 
    def __init__(self,name, description, effect, duration):
        Item.__init__(self, name)

    def wear(self,user):
        #Must be implemented in child classes
        raise


class BeetlejuiceSuit(Clothes):
    def __init__(self)
        Vetement.__init__(self,"Costume Beetlejuice", "Une grande robe sans coupe rayé noir et blanc", "Beetlejuice Petwor", 5)

    def wear(self, user):
        user.int = user.int-1
        user.sexe= "undefined"
        user.mp = user.mp + 2   