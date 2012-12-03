'''
Created on Dec 2, 2012

@author: Govener Brit
'''

class BooleanExpression(object):
    '''
    classdocs
    '''


    def __init__(self, left, right):
        '''
        Constructor
        '''
        self.left = left
        self.right = right
        
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    def getValue(self):
        pass
    
class EQExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() == self.getRight()
    
class GEExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() >= self.getRight()   

class GTExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() > self.getRight()
    
class LEExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() <= self.getRight()  
     
class LTExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() < self.getRight()       
     
class NEExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() != self.getRight()   
