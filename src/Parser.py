'''
Created on Dec 1, 2012

@author: Govener Brit
'''
from LexicalAnalyzer import *
from BinaryExpression import *
from AssignmentStatement import *
from DisplayStatement import *
from WhileStatement import *
from BooleanExpression import *
from IfStatement import *
from UnaryExpression import UnaryExpression
from Memory import Memory
from Id import *

class Parser(object):
    '''
    classdocs
    '''


    def __init__(self, file):
        '''
        Constructor
        '''
        self.file = file
        self.lex = LexicalAnalyzer(file)
        self.mem = Memory()
        self.parse(self.lex)
        
    def parse(self, lex):
        lex = self.lex
        Parser.match(self, "main")
        Parser.match(self, "(")
        Parser.match(self, ")")
        l = self.getStatementList()
        s = lex.getToken()
        if s == "$":
            raise ParserException("Garbage at Main")
        Parser.execute(self, l)
    
    def getStatementList(self):
        l = []
        s = self.getStatement()
        l.append(s)
        tok = self.lex.getToken()
        while tok == "/n":
            tok = self.lex.getToken()
            s = self.getStatement()
            l.append(s)
            tok = self.lex.getToken()
        return l
    
    def getStatement(self):
        s = self.lex.getToken()
        if s == "if":
            stmt = self.getIfStatement()
        elif s == "while":
            stmt = self.getWhileStatement()
        elif s == "display":
            stmt = self.getDisplayStatement()
        else:
            stmt = self.getAssignmentStatement(s)
        return stmt
    
    def getAssignmentStatement(self, var): 
        self.var = var
        self.match("<-")
        expr = self.getArithmeticExpression()
        return AssignmentStatement(var, expr)
    
    def getArithmeticExpression(self):
        s = self.lex.getToken()
        if self.isValidArithmeticOp(s):
            op = self.lex.getToken()
            op1 = self.getOperand()
            op2 = self.getOperand()
            expr = self.createBinaryExpression(op, op1, op2)
        else: 
            op = self.getOperand()
            expr = UnaryExpression(op)
        return expr
    
    def createBinaryExpression(self, op, op1, op2):
        if op == "+":
            expr = BinaryExpression.AddExpression(op1, op2)
        elif op == "-":
            expr = BinaryExpression.SubExpression(op1, op2)
        elif op == "*":
            expr = BinaryExpression.MulExpression(op1, op2)
        else:
            expr = BinaryExpression.DivExpression(op1, op2)
        return expr
    
    def getDisplayStatement(self):
        self.match("display")
        self.match("(")
        var = self.getId()
        self.match(")")
        return DisplayStatement(var)
    
    def getId(self):
        s = self.lex.getToken()
        if s == "" or len(s) > 1:
            raise ParserException("id expected, received " + s)
        return Id(s)
    
    def getWhileStatement(self):
        self.match("while")
        expr = self.getBooleanExpression()
        self.match("do")
        l = self.getStatementList()
        self.match("end")
        return WhileStatement(expr, l)
    
    def getBooleanExpression(self):
        s = self.lex.getToken()
        if self.isValidBooleanOperator(s):
            op = self.lex.getToken()
            op1 = self.getOperand()
            op2 = self.getOperand()
            return self.createBooleanExpression(op, op1, op2)
    
    def createBooleanExpression(self, op, op1, op2):
        self.op = op
        self.op1 = op1
        self.op2 = op2
        if self.op == "=":
            expr = BooleanExpression.EQExpression(op1, op2)
        elif op == "/=":
            expr = BooleanExpression.NEExpression(op1, op2)
        elif op == ">":
            expr = BooleanExpression.GTExpression(op1, op2)
        elif op == ">=":
            expr = BooleanExpression.GEExpression(op1, op2)
        elif op == "<":
            expr = BooleanExpression.LTExpression(op1, op2)
        else:
            expr = BooleanExpression.LEExpression(op1, op2)
        return expr
    
    def getOperand(self):
        s = self.lex.getLookAheadToken()
        if s == "":
            raise ParserException("Operand Expected")
        if s.isdigit():
            op = self.getLiteralInteger()
        else:
            op = self.getId()
        return op
    
    def getLiteralInteger(self):
        s = self.lex.getToken()
        try:
            return int(s)
        except ValueError:
            raise ParserException("literal integer expected")
        
    def getIfStatement(self):
        self.match("if")
        expr = self.getBooleanExpression()
        self.match("then")
        l1 = self.getStatementList()
        self.match("else")
        l2 = self.getStatementList()
        self.match("end")
        return IfStatement(expr, l1, l2)
    
    def isValidBooleanOperator(self, s):
        self.s = s
        if s == "=" or s == "/=" or s == ">" or s == "<" or s == ">=" or s == "<=":
            return True
        else:
            return False
         
    def isValidArithmeticOp(self, s):
        self.s = s
        if s == "+" or s == "-" or s =="*" or s == "/":
            return True
        else: 
            return False
    
    def match(self, expected):
        self.expected = expected
        self.tok = self.lex.getToken()
        if expected != self.tok:
            raise ParserException("token equals " + self.tok + " and " +self.expected + " expected")
    
    def execute(self, statementList):
        self.statementList = statementList
        i = 0
        while statementList != "" :
            s = statementList.pop(i)
            s.execute()
            
    def store(self, ch, value):
        self.mem.insert((ord(ch)-ord('a')), value)
    
    def fetch(self, ch):
        return self.mem(ord(ch)-ord('a'))
            
class ParserException(Exception):
    
    def __init__(self, message):
        self.message = message
        print(self.message)

class Program(object):
    def __init__(self, l):
        self.l = l
