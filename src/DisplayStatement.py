'''
CS3150
PythonParser
@author: Sabrina Cown
'''
class DisplayStatement(object):
    def __init__(self, var):
        self.var = var
    
    def execute(self, parser):
        print(self.var)