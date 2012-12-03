'''
Created on Dec 2, 2012

@author: Govener Brit
'''

from Parser import *
if __name__ == '__main__': 
    try:
        prog = Parser("C:/Users/Govener Brit/Documents/test1.txt")
        prog.parse()
        prog.execute()
    except IOError:
        print("File not Found")
    except ParserException.ParserException: 
        s = ParserException.ParserException.message
        print(s)
    
    

    