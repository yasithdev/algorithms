# inputs and storing
T = int(raw_input())
H,W,R = [],[],[]

for t in range(T):
    
    frow = [int(x) for x in raw_input().split()]
    H.append(frow[0])
    W.append(frow[1])

    matrix = []
    for h in range(H[t]):
        matrix.append([int(x) for x in raw_input().split()])
    R.append(matrix)


# for each test case
for i in range(T):
    
    # check for contiguous blocks
    # starting from each point increasing right -> down

    for j in range(H):
        for k in range(W):
            


def getmaxarea(A, xval, yval):
    H = len(A)
    W = len(A[0])
    
    for x in range(H):
        for y in range(W):
            
    
