'''
CS3150
PythonParser
@author: SabrinaCown
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
    
    def execute(self, parser):
        if self.expr.BooleanExpression.getValue():
            self.l1.execute()
        else:
            self.l2.execute()
        