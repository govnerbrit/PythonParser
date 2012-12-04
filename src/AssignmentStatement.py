'''
Created on Dec 2, 2012

@author: Govener Brit
'''
from Parser import *
from Id import *
class AssignmentStatement(object):
      
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
          
    def execute(self):
        assign = self.expr.getValue()
        ch = self.var
        Parser.store(ch, assign)
        