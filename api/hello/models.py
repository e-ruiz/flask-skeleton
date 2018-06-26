# -*- coding: utf-8 -*-

class Hello():

    GREETING = 'Aloha'

    def __init__(self):
        pass
    
    def sayHelloTo(self, name=None):
        return self.GREETING + ' ' + name if name else self.GREETING
        
        