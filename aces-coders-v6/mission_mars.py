import math

planetweights = [float(i) for i in input().split()]
unorderedc = []

for i in range(len(planetweights)):
    unorderedc += [float(i) for i in input().split()]
    
factor = (6.674 * 106000)

r = []
thetaz = []
psix = []

for i in range(0, len(unorderedc), 3) :
    r += [unorderedc[i]]
    psix += [unorderedc[i+1]]
    thetaz += [unorderedc[i+2]]

forces = [factor * (planetweights[i] / (r[i]**2)) for i in range(len(planetweights))]

resx = sum([forces[i] * math.sin(thetaz[i]) * math.cos(psix[i]) for i in range(len(planetweights))])
resy = sum([forces[i] * math.sin(thetaz[i]) * math.sin(psix[i]) for i in range(len(planetweights))])
resz = sum([forces[i] * math.cos(thetaz[i]) for i in range(len(planetweights))])

# correct here


resultant =  (math.sqrt(resx**2 + resy**2 + resz**2))

psiresx = math.atan(resy/resx)
thetaresz = math.atan(math.sqrt(resx**2 + resy**2) / resz)

# prs = [math.sqrt((r[i] * 10**6 * math.sin(thetaz[i]) * math.cos(psix[i]) - math.sin(thetaresz) * math.cos(psiresx)) ** 2 + (r[i] * 10**6 * math.sin(thetaz[i]) * math.sin(psix[i]) - math.sin(thetaresz) * math.sin(psiresx)) ** 2 + (r[i] * 10 ** 6 * math.cos(thetaz[i]) - math.cos(thetaresz))** 2)  for i in range(len(planetweights))]
# prs = [math.sqrt((r[i] * 10**6 * math.sin(psix[i]) * math.cos(thetaz[i]) - math.sin(psiresx) * math.cos(thetaresz)) ** 2 + (r[i] * 10**6 * math.sin(psix[i]) * math.sin(thetaz[i]) - math.sin(psiresx) * math.sin(thetaresz)) ** 2 + (r[i] * 10 ** 6 * math.cos(psix[i]) - math.cos(psiresx))** 2)  for i in range(len(planetweights))]
# prs = [math.sqrt((r[i] * 10**6 * math.sin(thetaz[i])*(math.cos[psix[i]] - math.sin(psix[i]/tan[psiresx] )))**2 + (r[i] * 10**6 * math.sin(psix[i])/(math.sin(psiresx)*math.tan(thetaresz)) - (r[i] * 10**6 * math.cos(thetaz[i])))**2 for i in range(len(planetweights)))]

print()
print(round(resultant,3))
print ()




    
