import operators as o
import tables as t

# o.or_(o.im(1, 1), o.iff(0, 0))

def mp(a, b): # modus ponens
    x = o.im(o.and_(a, o.im(a, b)), b)
    return(x)

def mt(a, b): # modus tollens
    x = o.im(o.im(not(b), o.im(a, b)), not(a))
    return(x)

# def hs(): # hypothetical syllogism
# def ds(): # disjunctive syllogism
# def vI(): # addiciton
# def andE(): # simplification
# def andI(): # conjunction