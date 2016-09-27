def even(x):
    even = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            even.append(x[i])
        else:
            pass
    print even
a = [1,2,3,4,5,6,7,7,7,7,7,8,8,8,8,8,]
even(a)
