import sys
import re
import numpy as np
import color
import matrix

MAX_DEPTH = 3 # TODO: determine actual value

def Parse(inputData):
    # split file on newline
    dataLines = inputData.split('\n')

    # this will be returned
    dataLineList = []

    # process data
    for line in dataLines:
        # split on >= 1 spaces, or >= 1 tabs
        splitLine = re.split(" +|\t+", line)

        # remove empty entries
        for i in splitLine:
            if(len(i)==0):
                splitLine.remove(i)
                
        dataLineList.append(splitLine)
    return dataLineList


def PrintList(myList):
    for element in myList:
        print(element)

def PrintDivider(length):
    for i in range(length):
        print("-", end='')
    print()

def CheckArgs(numberOfArgs, filename):
    # exit program if number of arguments is wrong
    if numberOfArgs < 2:
        print(f" Usage: {filename} <inputFile>")
        sys.exit()

def Magnitude(v):
    return np.linalg.norm(v)

# Normalize a vector, which is a numpy array
def Normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def Dot(a, b):
    r = np.dot(a, b)
    return r

# Ambient, diffuste, specular lighting function
'''
PIXEL_COLOR[c] = Ka*Ia[c]*O[c] +
    for each point light (p) 
        { Kd*Ip[c]*(N dot L)*O[c]+Ks*Ip[c]*(R dot V)n } 
    + Kr*(Color returned from reflection ray)

PIXEL_COLOR[c] = Ka*Ia[c]*O[c] + Kd*Ip[c]*(N dot L)*O[c]+Ks*Ip[c]*(R dot V)n + Kr*(Color returned from reflection ray)
'''
def ADS(ka, kd, ks, pos, Lpos, N):
    print(" ADS()...")
    # might be function arguments...
    shine = 1
    N = np.array([0, 0, 0])
    pos = np.array([0, 0, 0]) 
    Lpos = np.array([0, 0, 0])

    L = Normalize(Lpos - pos)
    V = Normalize( -1 * pos)
    R = np.array([0, 0, 0]) # TODO: add reflection function

    lightDotNormal = max( Dot(L, N), 0.0 )
    diffuse = np.array([0, 0, 0])
    diffuse = kd * lightDotNormal # this is diffuseProduct (what's that?) * lightDotNormal

    base = max( Dot(R, V), 0.0 )
    reflectedDotViewShiny = np.power(base, shine)

    specular = np.array([0, 0, 0])
    specular = ks = reflectedDotViewShiny

    if ( Dot(L, N) < 0.0):
        specular = np.array([0, 0, 0])

    ambient = np.array([0, 0, 0])

    result = ambient + diffuse + specular

    return result

# Check if ray intersects with objects in the scene
# If there is an intersection, return the coordinates
# If there is no intersection, maybe return None
def Intersection(ray, sphereObjectList):
    isIntersection = False
    intersectPoint = np.array([0, 0, 0])

    # Check for each sphere
    for sphere in sphereObjectList:
        solutionCount = 0

        # Get sphere transformations

        translateMatrix = np.array([[1, 0, 0, sphere.posX],
                                    [0, 1, 0, sphere.posY],
                                    [0, 0, 1, sphere.posZ],
                                    [0, 0, 0, 1]])

        scaleMatrix = np.array([[sphere.scaleX, 0, 0, 0],
                                [0, sphere.scaleY, 0, 0],
                                [0, 0, sphere.scaleZ, 0],
                                [0, 0, 0, 1]])

        # Get inverted matrices
        invertTranslate = matrix.InvertMatrix(translateMatrix)
        invertScale = matrix.InvertMatrix(scaleMatrix)

        # Transform ray
        rayDir = ray.Direction()
        rayOrigin = ray.Origin()

        transformedRay = ray
        
        # make origin vector length 4 to do dot product
        tempOrigin = np.array([rayOrigin[0], rayOrigin[1], rayOrigin[2], 1])
        transformedPosition = Dot(tempOrigin, invertTranslate)

        # make scale vector lenght 4 to do dot product
        tempScale = np.array([rayDir[0], rayDir[1], rayDir[2], 0])
        transformedScale = Dot(tempScale, invertScale)

        # Now we have the transformed ray
        transformedRay.SetOrigin(transformedPosition)
        transformedRay.SetDirection(transformedScale)

        tRayDir = transformedRay.Direction()
        tRayDirV3 = np.array([tRayDir[0], tRayDir[1], tRayDir[2]])

        tRayOrigin = transformedRay.Origin()
        tRayOriginV3 = np.array([tRayOrigin[0], tRayOrigin[1], tRayOrigin[2]])

        '''
        a = np.square( Magnitude(tRayDirV3) )
        b = Dot(tRayOriginV3, tRayDirV3)
        c = np.square( Magnitude( tRayOriginV3 ) )
        '''

        # Calculate coefficients of the quadratic equation
        a = np.square(Magnitude(tRayDirV3))
        b = Dot(tRayOriginV3, tRayDirV3)
        c = np.square( Magnitude(tRayOriginV3) )

        #print(f"a: {a}, b: {b}, c: {c}")

        # Calculate the discriminant
        #discriminant = b ** 2 - 4 * a * c

        #print(f"Discriminant: {discriminant}")

        
        bsqu = np.square(b)
        ac = a * c
        discriminant = bsqu - ac # for determining number of solutions
        

        if discriminant > 0:
            #print("two solutions")
            solutionCount = 2
            isIntersection = True
            break
        elif discriminant < 0:
            #   print(f"b = {b}, ac = {ac}")
            #print("no solutions")
            solutionCount = 0
        else: # x == 0
            #print("one solution")
            solutionCount = 1
            isIntersection = True
            break

    # TODO: get intersection point
    if isIntersection:
        return intersectPoint
    else:
        return None

# Scale color value and cast to integer
def PpmColorScale(color):
    return (int)(color * 255)

# TODO: what arguments should this function take?
def Raytrace(ray, sphereObjectList, lightObjectList, background):

    c = np.array([0, 0, 0]) # color vector

    if ray.Depth() > MAX_DEPTH:
        print(f"{ray.Depth()} > {MAX_DEPTH}")
        return c
    
    # intersection of ray with object
    #intersectPoint = np.array([0, 0, 0])
    intersectPoint = Intersection(ray, sphereObjectList)

    if intersectPoint is None:
        # set background color
        for i in range( len(c) ):
            c[i] = background[i]
        return c
    else:
        # there is an intersection
        print("intersection")
        return c

    # TODO: pass c into ADS() somehow
    c = ADS(1, 1, 1, 1, 1, 1)

    return c
