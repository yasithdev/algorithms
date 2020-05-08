def shush(string):
    
    s = string[:]
    ssrep = "ss" in s
    hhrep = "hh" in s

    while(ssrep or hhrep):
        # intelligently replace
        if "sss" in s:
            shush(s.replace("hss", "hh")
            shush(s.replace("ssh", "hh")
        else:
            s = s.replace("ss", "h")
        s = s.replace("hh", "s")
        ssrep = "ss" in s
        hhrep = "hh" in s
    
    return countsh(s)

def countsh(string):
    if string != "":
        return [string.count('h'), string.count('s')]
    else:
        return [0,0]

N = int(input())
strings = []
for i in range(N):
    strings.append(raw_input())


for s in strings:
    sh =  shush(s)
