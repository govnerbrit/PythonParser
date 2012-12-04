'''
CS3150
PythonParser
@author: sabrina cown
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
    
    def execute(self, parser):
        while self.expr.getValue():
            self.l.execute()