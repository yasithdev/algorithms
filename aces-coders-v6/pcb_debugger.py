def checkIfSC(connections, current):
    # determine if a circuit element is shorted
    if len(connections[current]) == 0 : return False
    
    for key in connections[current]:
        # if any other key of connection[current] is in connection[key], return true
        set1 = set(connections[key])
        set2 = connections[current][:]
        set2.remove(key)
        if key in set1 : return True
        if set1 != None and set2 != None:
            res = set1.intersection(set2)
            if len(res) > 0 and ('P' in res or current != 'P'): return True
        else:
            # check recursively in each connections[key] for current
            checkIfSC(connections[key], current)
    return False

def isSC(connections):
    for key in connections.keys():
        if checkIfSC(connections, key) == True: return True
    return False

def isOC(connections):
    # element keys with no value sets are already checked beforehand.
    # this method checks if some keys does not exist in any value sets
    valueset = []
    for key in connections.keys():
        valueset = set(valueset).union(set(connections[key]))
    return len(valueset) != len(connections.keys())

# Main method -------------------------------------------

n = int(input())
connections = {}
sc = False
oc = False

for i in range(n):
    array = input().split()
    try:
        connections[array[0]] = array[1].split(",")
    except:
        connections[array[0]] = []
        oc = True

sc = isSC(connections)
oc = oc or isOC(connections)

if sc == True and oc == True: print('OC SC')
elif sc == True: print('SC')
elif oc == True: print('OC')
else: print('W')
