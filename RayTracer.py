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
    sphereList = []
    lightList = []
    back = []
    ambient = []
    output = ""

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

    print()
    helper.PrintList(dataLineList)

   # do raytracing
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

main()
