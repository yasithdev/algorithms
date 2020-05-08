n = raw_input().split()
N = int(n[0])

if (len(n) > 1):
    W = int(n[1])
    
else:
    W = int(raw_input())
    
A = [int(x) for x in raw_input().split()]

s = 1
sums = []

if (N>0 and W>0 and N <= 100000 and W <= N/3):
  while(s <= N):
      summ = 0
      for i in xrange(s - W, s):
          if i < 0: continue
          summ += A[i]
      s += 1
      sums += [summ]
  for s in sums:
      print s,
else:
    print 0
