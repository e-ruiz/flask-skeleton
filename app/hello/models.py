# -*- coding: utf-8 -*-

class Hello():

    GREETING = 'Aloha'

    def sayHelloTo(self, name=None):
        return self.GREETING + ' ' + name if name else self.GREETING
        
        
