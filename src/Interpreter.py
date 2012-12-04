'''
Created on Dec 2, 2012

@author: Govener Brit
'''

from Parser import *
def main():
    try:
        prog = Parser("../test1.txt")
        
    except IOError:
        print("File not Found")
    except ParserException: 
        print(ParserException)
        
main()    
    

    