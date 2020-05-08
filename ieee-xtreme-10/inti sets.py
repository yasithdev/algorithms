import math

def getModulo(strn, modVal):
    slicen = 3000;
    while (len(strn) > slicen): 
        temp = int(strn[:slicen]) % modVal;
        strn = strn[slicen:];
        strn = str(temp) + strn;

    else:
        print (int(strn) % modVal);


def factors(n):
    ls = [ ];
    if n!=1:
        ls.append([i, n // i ] for i in range(1, int(n**0.5) + 1) if n % i == 0);
    return ls;
    
t = int(input());
for i in range(t):
    N,A,B = [int(x) for x in input().split()];

    facs = list(factors(N));
    print (facs[i]);
    allintsum = B/2*(B+1) - A/2*(A-1)
    factorsum = 0

    for i in range(len(facs)):
        print (facs[i]);
        factor = int(facs[i])
        low = A/factor
        high = B/factor
        factorsum += (high/2*(high+1) - low/2*(low-1))*factor;


    print(allintsum - factorsum);
