import math

def func(n, k):
    result = 0
    if n == 0: result = 0
    elif n < k: result = n
    else:
        string = str(int(str(n), k))
        result = int(string[0]) + sum(int (x) for x in string[1:])
    return result

# init
K, B = [int(x) for x in raw_input().split()]

Num = 1
Max = 0
MaxN = None

while(Num < B):
    if func(Num, K) > Max :
        Max = func(Num, K)
        MaxN = Num
    Num += 1

print MaxN
