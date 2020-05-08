"""
nums = []
nlist=[]
index=0
number=0
counter1=0
n1=1
for num in range(2,10):#2 is because I know 1million is in 2's set
    for i in range(0,181440): #9!/2 in order to go in 2's ("#for last part" already have done)
        nums = ['0','1','2','3','4','5','6','7','8','9']
        nlist.append(nums[num])
        nlist.append(nums[num])
        


           
        for i2 in range(0,2):
            nums = ['0','1','2','3']
            del nums[num]
            nlist[index]+=nums[i]   
            del nums[i]
            nlist[index]+=nums[i2]    #concatenate the number before last
            del nums[i2]
            nlist[index]+=nums[0]    #concatenate the last number
            index+=1
        if index>7:
            number=nlist[7]
            break
        
print number
print nlist
       
            

nums = []
nlist=[]
index=0
n=0
for num in range(0,4):
    for i in range(0,3):
        nums = ['0','1','2','3']
        nlist.append(nums[num]) #adding the first number
        nlist.append(nums[num])

        for i2 in range(0,2):
            nums = ['0','1','2','3']
            del nums[num]
            nlist[index]+=nums[i]   
            del nums[i]
            nlist[index]+=nums[i2]    #concatenate the number before last
            del nums[i2]
            nlist[index]+=nums[0]    #concatenate the last number
            index+=1
        if index>7:
            n=nlist[7]
            #break
        
print n
print nlist
"""
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(perm)+1):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


a=[]
for i in all_perms("1234"):
    a.append(i)
    
print a




