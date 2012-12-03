'''
Created on Dec 2, 2012

@author: Govener Brit
'''

class WhileStatement(object):
    '''
    classdocs
    '''


    def __init__(self, expr, l):
        '''
        Constructor
        '''
        self.expr = expr
        self.l = l
    
    def execute(self):
        while self.expr.getValue():
            self.l.execute()