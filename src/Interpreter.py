'''
CS3150
PythonParser
@author: SabrinaCown
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