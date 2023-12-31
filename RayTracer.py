import sys
import re
import numpy as np
import constants 
import utility
import ppm
import sphere
import light
import color
import ray

def main():

    # program variables
    debug = False
    parseSuccess = True
    divLength = 20
    width = 400
    height = 400
    ppmValueScale = 255

    # reduse resolution when debugging/testing
    if debug:
        width = 100
        height = 100

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
    sphereDataList = []     # for temporary storage of sphere data
    lightDataList = []      # for temporary storage of light data
    back = []               # background color
    ambient = []
    output = ""

    # program entity variables
    sphereObjectList = []
    lightObjectList = []
    camera = np.array([0, 0, -1*near]) # TODO: should N here be negative?

    # Check number of arguments
    utility.CheckArgs(numberOfArgs, selfFilename)

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
    dataLineList = utility.Parse(data)

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

   # do raytracing
    if debug:
        print(" Begin raytracing...")

    # TODO: determine pixels on screen (something related to the camera)

    W = width // 2
    H = height // 2

    # For output file
    pixels = bytearray(3 * width * height)
    k = 0
    pixelsOut = []

    # Main recursive raytracing algorithm
    for row in range(height):
        for col in range(width):
            # for each pixel on the screen
            # determine ray_cr from eye through pixel

            uc = (-1 * W) + (W * (2 * col)/width )
            vr = (-1 * H) + (H * (2 * row)/height )

            camera[0] = uc
            camera[1] = vr

            # create ray
            origin = np.array([col-width/2+0.5, row-height/2+0.5, 100])
            direction = np.array([0, 0, -1])
            r = ray.Ray(origin, direction)
            r.SetDepth(1)

            # TODO: make sure arguments match, they are subject to change
            color = utility.Raytrace(r, sphereObjectList, lightObjectList, back)

            # Scale color value for ppm format
            for i in range( len(color) ):
                color[i] = utility.PpmColorScale(color[i])

            pixels[k] = color[0]
            pixels[k + 1] = color[1]
            pixels[k + 2] = color[2]
            k += 3

    if debug:
        print(" Complete.")

    ppm.save_image_p3(width, height, output, pixels)

    file.close()

main()
