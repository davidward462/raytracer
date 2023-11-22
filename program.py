import sys
import re
import color

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


# Ambient, diffuste, specular lighting function
'''
PIXEL_COLOR[c] = Ka*Ia[c]*O[c] +
    for each point light (p) 
        { Kd*Ip[c]*(N dot L)*O[c]+Ks*Ip[c]*(R dot V)n } 
    + Kr*(Color returned from reflection ray)

PIXEL_COLOR[c] = Ka*Ia[c]*O[c] + Kd*Ip[c]*(N dot L)*O[c]+Ks*Ip[c]*(R dot V)n + Kr*(Color returned from reflection ray)
'''
def ADS(ka, kd, ks, pos, Lpos, N):
    print(" call ADS()...")

    L = Normalize(Lpos - pos)
    V = Normalize( -1 * pos)
    # reflect 

    ambient = np.array([0, 0, 0])
    diffuse = np.array([0, 0, 0])
    specular = np.array([0, 0, 0])


    result = ambient + diffuse + specular


    return resultColor
