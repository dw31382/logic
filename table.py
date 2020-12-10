blah1 = [
    [1, 0, 1, 0],
    [1, 1, 0, 0]]

def inputs():
    print(blah1[0])
    print(blah1[1])

def function(x):
    inputs()
    print()
    y = map(x, blah1[0], blah1[1])
    print(list(y))

blah2 = [
    [1, 1, " ", 0, 0, 0, 0, 0, 0, 0, 0, " ", 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, " ", 0, 0, 0, 0, 1, 1, 1, 1, " ", 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, " ", 0, 0, 1, 1, 0, 0, 1, 1, " ", 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, " ", 0, 1, 0, 1, 0, 1, 0, 1, " ", 0, 1, 0, 1, 0, 1, 0, 1]
]

def complete():
    print(blah2[0])
    print(blah2[1])
    print(blah2[2])
    print(blah2[3])
