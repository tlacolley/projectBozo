#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.use =

    def use(self,user):
        #Must be implemented in child classes
        raise


class Consumable(Item):
    def __init__(self, effect):
        Item.__init__(self, name, description)
        pass


class Drink(Consumable):
    def __init__(self,):
        Consumable.__init__(self, name, description, effect)
    def use(self,user):
        self._consume()
# _function : polymorphe d´une fonction permet d´utiliser cette fonction en interne
#  tout les objets aurons une fonction use mais celle ci sera different par class
    def _consume(self,user):
        #Must be implemented in child classes
        raise

#  rajouter des effect secondaire sans preciser au joueur effect. parcequ on est des putes :p    PET WHORE !!!
class Cola(Drink):
    def __init__(self):
        Consumable.__init__(self, "Cola", "Coca-Cola is the biggest-selling soft drink in history, as well as one of the most recognizable brands in the world.", "Wake Up")

    def consume(self, user):
        user.hp = user.hp + 10
        print user.name

class Chouffe(Drink):
    def __init__(self):
        Drink.__init__(self,"Chouffe", "La bière belge du lutin au bonnet rouge ! A l'oeil Robe blonde dorée avec une épaisse mousse blanche.Au nez Arômes d'épices et d'agrumes. A la bouche Notes houblonnées, fruitées et épicées.","Bourrer")

    def consume(self,user):
        user.hp = user.hp/2
        user.mp = user.mp/2
        user.str = user.str/2
        user.int = user.int/2
        user.res = user.res/2









# -------------------------------------------------------------------------
# class Miscelaneous(Item):
#                         #                     Pour la duration  duree en tour
#         Item.__init__(self, name, description)
#         pass
#
#
#
#
# class BeetlejuiceSuit(Miscelaneous):
#     def __init__(self, effect, duration):
#         Vetement.__init__(self,"Costume Beetlejuice", "Une grande robe sans coupe rayé noir et blanc, d´un gout douteux", "BeetlejuiceSuit", 5)
#
#     def wear(self, user):
#         user.int = user.int-1
#         user.sexe= "undefined"
#         user.mp = user.mp + 2
