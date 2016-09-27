# Positive Numbers II
#
# Given an list of numbers, create a new list which contains every number in the given list which # is positive.

def positive(x):
    pos = []
    for i in range(len(x)):
        if x[i] > 0:
            pos.append(x[i])
        else:
            pass
    print pos

a = [-3,-2,-1,0,1,2,3,4]
positive(a)
