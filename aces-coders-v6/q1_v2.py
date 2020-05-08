# cost per kg
def cost(a,b,c):
    return (150*a + 10*b + c)/(a+b+c)

# max stars for passed array and weight
def maxstars(weight, offset):
    global arr
    temp = []
    offset = int(offset)

    if weight == 0: return 0

    for i in (1,2,3):
        if arr[offset - 1 + i] == 0:
            temp += [0]
            continue
        # star ratings with deduction for cost
        temp += [ (10 + i) * weight - int((arr[offset - 1 + i] / 5) * weight)]
    
    # if material is selected should remove it from the array!
    arr[offset + temp.index(max(temp))] = 0
    return (max(temp))
    
def maxstarratingperm(ins, perm):
    # prices for each type by star rating
    # calculation
    return maxstars(ins[var(perm[0])], perm[0]) + maxstars(ins[var(perm[1])], perm[1]) + maxstars(ins[var(perm[2])], perm[2]) + maxstars(ins[var(perm[3])], perm[3])

def var(x):
    if int(x) == 0 : return 0
    elif int(x) == 2 : return 1
    elif int(x) == 3: return 2
    elif int(x) == 4 : return 3

def maxstarrating(ins):
    # prices for each type by star rating
    # calculation
    return maxstars(ins[0], 0) + maxstars(ins[1], 2) + maxstars(ins[2], 3) + maxstars(ins[3], 4)

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + elements[0:1] + perm[i:]


# main code --------------------
originalarr = [cost(1,5,10), cost(1,4,8), cost(1,3,6), cost(1,2,4), cost(1,1.5,3), cost(1,1,2), cost(1,1,1.5)]
inval = input().split()
for i in range(len(inval)) : inval[i] = int(inval[i])

##arr = originalarr[:]
##print(maxstarrating(inval), arr)
## screed 0
## beam 2
## slab 3
## column 4

answerslist = []
for per in all_perms("0234"):
    global arr
    arr = originalarr[:]
    answerslist += [maxstarratingperm(inval, per)]
##print(answerslist)
print(max(answerslist))


