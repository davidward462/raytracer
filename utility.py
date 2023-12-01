import sys
import re
import numpy as np
import color

MAX_DEPTH = 2 # TODO: determine actual value

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

def IsVerboseOutput(numberOfArgs, fileArgs):
    if numberOfArgs == 3:
        flag = fileArgs[2]
        if flag == "-v":
            return True
    return False

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

# DRAFT
# Check if ray intersects with objects in the scene
# If there is an intersection, return the coordinates
# If there is no intersection, maybe return None?
# TODO: determine exactly how this function will work
def Intersection(ray, sphereObjectList):
    isIntersection = False
    intersectPoint = np.array([0, 0, 0])

    for sphere in sphereObjectList:
        x = 0

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

    if ray.GetDepth() > MAX_DEPTH:
        print(f"{ray.GetDepth()} > {MAX_DEPTH}")
        return c
    
    # intersection of ray with object
    #intersectPoint = np.array([0, 0, 0])
    intersectPoint = Intersection(ray, sphereObjectList)

    if intersectPoint == None:
        # set background color
        for i in range( len(c) ):
            c[i] = background[i]
        return c

    # TODO: pass c into ADS() somehow
    c = ADS(1, 1, 1, 1, 1, 1)

    return c
