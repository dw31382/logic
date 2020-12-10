# t = []
# i = 0
# for i in range(16):
#     x.append(list(bin(i)[2:].zfill(4)))

def con(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(0)
 
def nor(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(1)
        
def ncim(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(0)

def nota(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(1)
        
def nim(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(0)

def notb(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(1)

def xor(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(0)
        
def nand(a, b):
    if (a == 1) and (b == 1):
        return(0)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(1)
        
def and_(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(0)
        
def iff(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(1)
        
def q_(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(0)

def im(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(0)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(1)
        
def a_(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(0)
        
def cim(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(0)
    if (a == 0) and (b == 0):
        return(1)

def or_(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(0)

def tau(a, b):
    if (a == 1) and (b == 1):
        return(1)
    if (a == 1) and (b == 0):
        return(1)
    if (a == 0) and (b == 1):
        return(1)
    if (a == 0) and (b == 0):
        return(1)
