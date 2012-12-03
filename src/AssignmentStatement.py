'''
Created on Dec 2, 2012

@author: Govener Brit
'''

class AssignmentStatement(object):
      
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr
          
    def execute(self):
        self.Memory.store(self.var.getChar(), self.expr.getValue())