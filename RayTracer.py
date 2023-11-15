import sys
import re
import constants 
import helper
import sphere
import light

def Raytrace(r):
    return 0

def main():

    # input file variables
    # TODO: determine if any of these should be made into objects

    near = 0
    left = 0
    right = 0
    bottom = 0
    top = 0
    res = []
    sphereDataList = []
    lightDataList = []
    back = []
    ambient = []
    output = ""

    sphereObjectList = []
    lightObjectList = []

    parseSuccess = True

    # get all system arguments, including source file name 
    fileArgs = sys.argv   

    # get source filename
    selfFilename = fileArgs[0] 

    # exit program if number of arguments is wrong
    if len(fileArgs) < 2:
        print(f" Usage: {selfFilename} <inputFile>")
        sys.exit() 

    # open file
    filePath = fileArgs[1]
    data = ""
    try:
        with open(filePath, 'r') as file:
            data = file.read()

    # catch errors
    except FileNotFoundError:
        print(f" The file at '{filePath}' was not found.")
    except Exception as e:
        print(f" An error occurred: {e}")

    print(" Processing file...")

    # split file on newline
    dataLines = data.split('\n')

    # store split lines
    dataLineList = []

    # process data
    for line in dataLines:
        # split on >= 1 spaces, or >= 1 tabs
        splitLine = re.split(" +|\t+", line)
        dataLineList.append(splitLine)

    for line in dataLineList:
        firstElement = line[0]
        if len(line) > 1:
            if(firstElement == constants.output):
                output = line[1]

            elif(firstElement == constants.left):
                left = line[1]

            elif(firstElement == constants.right):
                right = line[1]

            elif(firstElement == constants.bottom):
                bottom = line[1]

            elif(firstElement == constants.top):
                top = line[1]

            elif(firstElement == constants.near):
                near = [1]

            elif(firstElement == constants.ambient):
                ambient.append(line[0])
                ambient.append(line[1])
                ambient.append(line[2])

            elif(firstElement == constants.back):
                back.append(line[0])
                back.append(line[1])
                back.append(line[2])

            elif(firstElement == constants.res):
                res.append(line[1])
                res.append(line[2])

            elif(firstElement == constants.sphere):
                sphereDataList.append(line)

            elif(firstElement == constants.light):
                lightDataList.append(line)

            else:
                print(f" Error, no match with {firstElement} found.")
                parseSuccess = False

    # check parsing status, exit if failed.
    if parseSuccess:
        print(f" File at '{filePath}' parsed sucessfully.")
    else:
        print(f" Parsing of '{filePath}' failed.")
        sys.exit() 

    sphereCount = len(sphereDataList)
    lightCount = len(lightDataList)

    # for testing
    print(f" spheres: {sphereCount}")
    print(f" lights: {lightCount}")

    # create and store sphere objects in list
    for i in range(sphereCount):
        s = sphere.Sphere(sphereDataList[i])
        sphereObjectList.append(s)

    for i in range(lightCount):
        l = light.Light(lightDataList[i])
        lightObjectList.append(l)

    helper.PrintList(sphereObjectList)
    helper.PrintList(lightObjectList)

   # do raytracing
    print(" Begin raytracing...")
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

    print(" Complete.")

    file.close()

main()
