for a in range(9,0,-1):
    for c in range (1,10-a):
        print (end="       ")
    for b in range (a,0,-1):
        print ("%d*%d=%-2d" % (a,b,a*b),end=' ')
    print("")


