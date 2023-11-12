import sys
import re
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
    #print(fileArgs)

    # get source filename
    selfFilename = fileArgs[0] 
    #print(f" Filename: {selfFilename}")

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

    # split lines
    dataLines = data.split('\n')
    print(dataLines)

    # process data
    for line in dataLines:
        x = re.search("NEAR", line)
        if x != None:
            print(x.string)

    # do raytracing
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

main()
