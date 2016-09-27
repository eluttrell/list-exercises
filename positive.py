# Positive Numbers
#
# Given an list of numbers, print each number in the list that is greater than zero.

def positive(x):
    for i in range(len(x)):
        pos = ''
        if x[i] > 0:
            pos += str(x[i])
            print pos
        else:
            pass

a = [-3,-2,-1,0,1,2,3,4]
positive(a)
