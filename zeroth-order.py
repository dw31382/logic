#!/usr/bin/python3

# Propositions
class Prop:
  def __init__(self, str, val):
    self.str = str
    self.val = val

# Truth functions
def con(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(False)
 
def nor(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(True)
        
def ncim(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(False)

def nota(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(True)
        
def nim(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(False)

def notb(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(True)

def xor(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(False)
        
def nand(a, b):
  if (a == True) and (b == True):
    return(False)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(True)
        
def and_(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(False)
        
def iff(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(True)
        
def q_(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(False)

def im(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(False)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(True)
        
def a_(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(False)
        
def cim(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(False)
  if (a == False) and (b == False):
    return(True)

def or_(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(False)

def tau(a, b):
  if (a == True) and (b == True):
    return(True)
  if (a == True) and (b == False):
    return(True)
  if (a == False) and (b == True):
    return(True)
  if (a == False) and (b == False):
    return(True)
