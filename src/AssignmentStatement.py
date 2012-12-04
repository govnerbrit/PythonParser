'''
CS3150
PythonParser
@author: Sabrina cown
'''
from Parser import *
from Id import *
class AssignmentStatement(object):
      
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
          
    def execute(self, parser):
        assign = self.expr
        ch = self.var
        print(self.expr)
        parser.store(ch, assign)
        