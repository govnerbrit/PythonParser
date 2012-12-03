'''
Created on Nov 30, 2012

@author: Govener Brit
'''

class DisplayStatement(object):
    def __init__(self, var):
        self.var = var
    
    def execute(self):
        print(self.var)