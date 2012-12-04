'''
Created on Dec 3, 2012

@author: Govener Brit
'''
from array import array
class Memory(object):
    def __init__(self):
        self.mem = array('i', [])
        
    def store(self, ch, value):
        self.mem.insert((ord(ch)-ord('a')), value)
                
    def fetch(self, ch):
        return self.mem(ord(ch)-ord('a'))