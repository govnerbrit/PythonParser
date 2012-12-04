'''
CS3150
PythonParser
@author: sabrina cown
'''
class UnaryExpression(object):
    '''
    classdocs
    '''


    def __init__(self, op):
        '''
        Constructor
        '''
        self.op = op
        
    def getValue(self):
        return self.op