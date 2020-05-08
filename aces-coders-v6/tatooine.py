# laser movement logic for given angle. return next position
def nextstep(x, y, angle):
    if angle == 45:
        return x+1, y-1, angle
    elif angle == 135:
        return x+1, y+1, angle
    elif angle == 225:
        return x-1, y+1, angle
    elif angle == 315:
        return x-1, y-1, angle


# return list of occupied coordinates when placed a cube
def placecube(x,y):
    occupiedc = []
    for i in (0,1,2):
        for j in (0,1,2):
            occupiedc += [[x+i, y+j]]
    return occupiedc

# only for convenience. same as placecube literally
def placelavawell(x,y):
    return placecube(x,y)


# check if cube coordinates and laser coordinates coincide
def iscoincided(x, y, cubex, cubey):
    return [x,y] in placecube(cubex, cubey)


# check if edge coincided cube with laser this case should be AVOIDED!!
def iscornercoincided(x, y, cubex, cubey):
    return [x,y] in [[cubex, cubey], [cubex+2,cubey], [cubex,cubey+2], [cubex+2,cubey+2]]

# check if two cubes lie on each other
def doescubescoincide(x1,y1, x2,y2):
    return placecube(x1,y1) in placecube(x2,y2)


# reflect laser beam if coincided and return new angle after reflection
def reflect(x, y, angle, cubex, cubey):
    # depending on which surface the laser coincided, returned angle changes

    # horizontal surface
    if iscoincided(x+1, y, cubex, cubey) and iscoincided(x-1, y, cubex, cubey):
        if angle == 45 : return 135
        elif angle == 135: return 45
        elif angle == 225: return 315
        elif angle == 315: return 225

    # vertical surface
    elif iscoincided(x, y+1, cubex, cubey) and iscoincided(x, y-1, cubex, cubey):
        if angle == 45 : return 315
        elif angle == 135: return 225
        elif angle == 225: return 135
        elif angle == 315: return 45


def generateoccupiedcoordinates()

# MAIN -------------------

#getting inputs

gridx, gridy = input().split()      #str

cubeqty = int(input())

lavawellqty = int(input())

unorderedc = input().split()
lavawellc = []
for i in range(0, lavawellqty + 1, 2):
    lavawellc += [[int(unorderedc[i]), int(unorderedc[i+1])]]

laserx, lasery = input().split()    #str

laserangle = int(input())

markerx, markery = input().split()  #str

# --------------------------------------
# calculating position of cubes

laserpos = laserx, lasery, laserangle
lavawellcoordinates = lavawellc



                
                
        
            

