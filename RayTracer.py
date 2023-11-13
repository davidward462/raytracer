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
            match firstElement:

                case constants.output:
                    print(firstElement)
                    output = line[1]

                case constants.left:
                    print(firstElement)
                    left = line[1]

                case constants.right:
                    print(firstElement)
                    right = line[1]

                case constants.bottom:
                    print(firstElement)
                    bottom = line[1]

                case constants.top:
                    print(firstElement)
                    top = line[1]

                case constants.near:
                    print(firstElement)
                    near = [1]

                case constants.ambient:
                    print(firstElement)
                    ambient.append(line[0])
                    ambient.append(line[1])
                    ambient.append(line[2])

                case constants.back:
                    print(firstElement)
                    back.append(line[0])
                    back.append(line[1])
                    back.append(line[2])

                case constants.res:
                    print(firstElement)
                    res.append(line[1])
                    res.append(line[2])

                case constants.sphere:
                    print(firstElement)
                    sphereDataList.append(line)

                case constants.light:
                    print(firstElement)
                    lightDataList.append(line)

                case _:
                    print(" Error, no match with {firstElement} found.")

   # do raytracing
    print(" Begin raytracing...")
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

main()
