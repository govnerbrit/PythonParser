'''
CS3150
PythonParser
@author: Sabrina Cown
'''
class BinaryExpression(object):
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    
class AddExpression(BinaryExpression):
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BinaryExpression(op1, op2)
    def getValue(self):
        return self.getLeft() + self.getRight()

class SubExpression(BinaryExpression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BinaryExpression(op1, op2)
    def getValue(self):
        return self.getLeft() - self.getRight()

class MulExpression(BinaryExpression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BinaryExpression(op1, op2)
    def getValue(self):
        return self.getLeft() * self.getRight()

class DivExpression(BinaryExpression):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
        BinaryExpression(op1, op2)
    def getValue(self):
        return self.getLeft() / self.getRight()    
