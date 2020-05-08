import math

# cost per kg
def cost(a,b,c):
    return (150*a + 10*b + c)/(a+b+c)

# max stars for passed array and weight
def maxstars(array, weight):
    temparray = []
    if weight == 0:
        return 0
    for i in (3,2,1):
        if array[i-1] == 0: continue
        # star ratings with deduction for cost
        temparray += [math.ceil(((10 + i) - (array[i-1] / 5)) * weight)]
        # if material is selected should remove it from the array!
    array[temparray.index(max(temparray))] = 0
    # print(temparray)
    return max(temparray)
    
def maxstarrating(ins, a):
    # prices for each type by star rating
    screed =    a[0:3]
    beam =      a[2:5]
    slab =      a[3:6]
    column =    a[4:7]
    # calculation
    return maxstars(screed, int(ins[0])) + maxstars(beam, int(ins[1])) + maxstars(slab, int(ins[2])) + maxstars(column, int(ins[3]))


# main code --------------------
arr = [cost(1,5,10), cost(1,4,8), cost(1,3,6), cost(1,2,4), cost(1,1.5,3), cost(1,1,2), cost(1,1,1.5)]
inval = input().split()
print (maxstarrating(inval, arr))
print (arr)



