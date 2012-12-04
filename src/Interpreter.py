'''
Created on Dec 2, 2012

@author: Govener Brit
'''

from Parser import *
def main():
    try:
        prog = Parser("../test1.txt")
        progFinal = Program(prog)
        progFinal.execute()      
    except IOError:
        print("File not Found")
    except ParserException: 
        print(ParserException)
        
main()    
    

    