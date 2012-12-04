'''
CS3150
PythonParser
@author: Sabrina Cown
'''

class LexicalAnalyzer(object):
    '''
    classdocs
    '''

    def __init__(self, file):
        '''
        Constructor
        '''
        f = open(file, "r")
        self.lexemes = ""
        self.line = f.readline()
        while self.line:
            self.lexemes += self.line
            self.line = f.readline()
        self.l = self.lexemes.split()
        f.close()
        
    def getLookAheadToken(self):
        if self.l == "":
            lexeme = "$"
        else:
            lexeme = self.l.pop(0)
            self.l.insert(0, lexeme)
        return lexeme
    
    def getToken(self):
        if self.l == "":
            lexeme = "$"
        else:
            lexeme = self.l.pop(0)
        return lexeme
    
            
        
        