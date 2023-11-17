import sys
import re
import numpy as np
import constants 
import helper
import ppm
import sphere
import light
import color
import ray

def Raytrace(r):
    return 0

def main():

    # program variables
    debug = True
    parseSuccess = True
    verboseOutput = False
    divLength = 20

    # get all system arguments, including source file name 
    fileArgs = sys.argv   

    # get source filename
    selfFilename = fileArgs[0] 

    # number of arguments
    numberOfArgs = len(fileArgs)

    # graphical variables from input file
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

    # exit program if number of arguments is wrong
    if numberOfArgs < 2:
        print(f" Usage: {selfFilename} <inputFile>")
        sys.exit() 

    # check for flags
    if numberOfArgs == 3:
        flag = fileArgs[2]
        if flag == "-v":
            verboseOutput = True

    # open file
    filePath = fileArgs[1]
    data = ""
    try:
        with open(filePath, 'r') as file:
            data = file.read()

    # catch errors
    except FileNotFoundError:
        print(f" The file at '{filePath}' was not found.")
        sys.exit() 
    except Exception as e:
        print(f" An error occurred: {e}")
        sys.exit() 

    if debug:
        print(" Processing file...")

    # use parser function
    dataLineList = helper.Parse(data)

    for line in dataLineList:
        
        if len(line) > 1:
            firstElement = line[0] # string identifier for data in line
            if(firstElement == constants.output):
                output = line[1] # this is a string type

            elif(firstElement == constants.left):
                left = int(line[1])

            elif(firstElement == constants.right):
                right = int(line[1])

            elif(firstElement == constants.bottom):
                bottom = int(line[1])

            elif(firstElement == constants.top):
                top = int(line[1])

            elif(firstElement == constants.near):
                near = int(line[1])

            elif(firstElement == constants.ambient):
                ambient.append( float(line[1]) )
                ambient.append( float(line[2]) )
                ambient.append( float(line[3]) )

            elif(firstElement == constants.back):
                back.append( float(line[1]) )
                back.append( float(line[2]) )
                back.append( float(line[3]) )

            elif(firstElement == constants.res):
                res.append( int(line[1]) )
                res.append( int(line[2]) )

            elif(firstElement == constants.sphere):
                sphereDataList.append(line)

            elif(firstElement == constants.light):
                lightDataList.append(line)

            else:
                print(f" Error, no match with {firstElement} found.")
                parseSuccess = False

    # handle sphere and light data
    
    # count of each
    sphereCount = len(sphereDataList)
    lightCount = len(lightDataList)

    # create and store sphere objects in list
    for i in range(sphereCount):
        s = sphere.Sphere(sphereDataList[i])
        if s.Parse() < 0:
            parseSuccess = False
        sphereObjectList.append(s)

    for i in range(lightCount):
        l = light.Light(lightDataList[i])
        if l.Parse() < 0:
            parseSuccess = False
        lightObjectList.append(l)

    # check parsing status, exit if failed.
    if debug:
        if parseSuccess:
            print(f" Data in file '{filePath}' processed sucessfully.")
        else:
            print(f" Failure processing data in '{filePath}'")
            sys.exit() 

    # output data collected from file
    if verboseOutput:
        helper.PrintDivider(divLength)
        print(f" near: {near}\n left: {left}\n right: {right}\n bottom: {bottom}\n top: {top}\n res: {res}\n back: {back}\n ambient: {ambient}\n output: {output}")

        print(f" spheres: {sphereCount}")
        helper.PrintList(sphereObjectList)
        print(f" lights: {lightCount}")
        helper.PrintList(lightObjectList)
        helper.PrintDivider(divLength)

   # do raytracing
    if debug:
        print(" Begin raytracing...")

    # TODO: determine pixels on screen (something related to the camera)
    pixelList = []

    # Main recursive raytracing algorithm
    for pixel in pixelList:
        color = Raytrace()

    # For output file...
    width = 400
    height = 400
    pixels = bytearray(3 * width * height)

    # Create a gradient for illustration purposes only
    scale = 128.0 / width
    k = 0
    for i in range(height):
        for j in range(width):
            c = int((i + j) * scale)
            pixels[k] = c
            pixels[k + 1] = c
            pixels[k + 2] = c
            k += 3

    ppm.save_image_p3(width, height, output, pixels)
    #ppm.save_image_p6(width, height, output, pixels) # should this have a different output name?

    if debug:
        print(" Complete.")

    file.close()

main()
