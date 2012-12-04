'''
Created on Dec 3, 2012

@author: Govener Brit
'''
from Memory import Memory
from Parser import *
class Id(object):
    def __init__(self, ch):
        self.ch = ch
    def getValue(self, ch):
        return Parser.fetch(self.ch)
    def getChar(self, ch):
        self.var = ch
        return self.var
