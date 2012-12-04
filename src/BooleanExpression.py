'''
CS3150
PythonParser
@author: Sabrina Cown
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
    
    def __init__(self, parser, op1, op2):
        self.op1 = str(op1)
        if self.op1.isdigit():
            self.op1 = int(op1)
        else:
            parser.fetch(self.op1)
        self.op2 = str(op2)
        if self.op2.isalnum():
            self.op2 = parser.fetch(self.op2)
        else:
            self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.op1 < self.op2
class NEExpression(BooleanExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BooleanExpression(op1, op2)
    def getValue(self):
        return self.get.Left() != self.getRight()   
