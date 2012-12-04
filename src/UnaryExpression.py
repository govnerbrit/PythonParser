'''
Created on Dec 3, 2012

@author: Govener Brit
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