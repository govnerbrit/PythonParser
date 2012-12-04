'''
CS3150
PythonParser
@author: Sabrina Cown
'''
from Parser import *

class Id(object):
    def __init__(self, ch):
        self.ch = ch
    def getValue(self, ch):
        return Parser.fetch(self.ch)
    def getChar(self, ch):
        self.var = ch
        return self.var
