import sys

def GetArgs():

    # get number of argumens 
    argLen = len(sys.argv)

    argList = []

    # if arguments were added by user when running the program
    if argLen > 1:
        # starting at index 1
        for arg in sys.argv[1:]:
            argList.append(arg)
    else:
        print("No arguments passed.")
        argList.append("")

    return argList


def Raytrace(r):
    return 0

def main():

    print(f"Filename: {sys.argv[0]}")
    fileArgs = GetArgs()    
    print(fileArgs)

    # open file
    filePath = fileArgs[0]
    try:
        with open(filePath, 'r') as file:
            data = file.read()
            print(data)
    # catch errors
    except FileNotFoundError:
        print(f"The file at '{filePath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    # do raytracing
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

main()
