'''
Created on Dec 1, 2012

@author: Govener Brit
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
        while self.line != "":
            self.lexemes += self.line
            self.line = f.readline()
        f.close()
        self.l = self.lexemes.split()
        
    def getLookAheadToken(self):
        if self.l == "":
            lexeme = "$"
        else:
            lexeme = self.l.pop(0)
            self.l.insert(0, lexeme)
        return lexeme
    
    def getToken(self):
        lexeme = self.l.pop(0)
        return lexeme
    
            
        
        