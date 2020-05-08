def findminsum(array, xvalues, yvalues):
    innersum = 0;
    minx = []
    miny = []

    if (xvalues == [] or yvalues == []): return 0

    for x in xvalues:
        for y in yvalues:
            value = array[x][y]

            newxvalues = [xx for xx in xvalues if xx != x]
            newyvalues = [yy for yy in yvalues if yy != y]
            newminsum = innersum + findminsum(array, newxvalues, newyvalues)
            if newminsum != 0:
                innersum = min(newminsum, innersum)

    return float(innersum)

# init
N = int(input())
P = []
T = []
A = []

# inputs
for n in range(N):
    v = [int(x) for x in raw_input().split()]
    P.append(v[0])
    T.append(v[1])

    matrix = []
    for x in range(v[0]):
        matrix.append([float(x) for x in raw_input().split()])
    A.append(matrix)

# calculation
for n in range(N):
    minsumval = findminsum(A[n], range(P[n]), range(T[n]))
    print "%.2f" % (minsumval/P[n])
