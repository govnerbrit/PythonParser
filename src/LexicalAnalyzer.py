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
        f = open(file)
        lexemes = f.readline()
        while lexemes:
            lexemes.add(f.readline())
        f.close()
        
    def getLookAheadToken(self):
        lexemes = self.lexemes
        if not lexemes:
            lexeme = "$"
        else:
            lexeme = lexemes(0)
        return lexeme
    
    def getToken(self):
        lexemes = self.lexemes
        if not lexemes: 
            lexeme = "$"
        else: 
            lexeme = lexemes.pop(0)
        return lexeme
    
            
        
        