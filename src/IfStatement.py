'''
Created on Dec 2, 2012

@author: Govener Brit
'''

class IfStatement(object):
    '''
    classdocs
    '''


    def __init__(self, expr, l1, l2):
        '''
        Constructor
        '''
        self.expr = expr
        self.l1 = l1
        self.l2 = l2
    
    def execute(self):
        if self.expr.BooleanExpression.getValue():
            self.l1.execute()
        else:
            self.l2.execute()
        