# ALGO
def mincount(x, a, b, ptr):
    if (ptr == len(x)) : return 0;
    clr = x[ptr];
    if (clr != a and clr != b):
        return 1 + min(mincount(x, clr, b, ptr + 1), mincount(x, a, clr, ptr + 1));
    else:
        return mincount(x, a, b, ptr + 1);

# MAIN
t = int(input());
for i in range(t):
    n = int(input());
    x = [int(i) for i in input().split()]
    print (mincount(x, 0, 0, 0))
