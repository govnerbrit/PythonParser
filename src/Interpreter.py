'''
Created on Dec 2, 2012

@author: Govener Brit
'''

from Parser import *
def main():
    try:
        prog = Parser("C:/Users/Govener Brit/Desktop/CS 3150/python/Parser/test1.txt")
        prog.execute()
    except IOError:
        print("File not Found")
    except ParserException: 
        s = ParserException.message
        print(s)
    
    

    