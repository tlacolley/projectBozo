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
    def __init__(self,name,effect):
        Item.__init__(self,name)
        pass


class Chouffe(Consomable):
    def __init__(self):
        Consomable.__init__(self,"Chouffe","Bourrer")

    def use(self,user):
        user.hp = user.hp/2
        user.mp = user.mp/2
        user.str = user.str/2
        user.int = user.int/2
        user.res = user.res/2
