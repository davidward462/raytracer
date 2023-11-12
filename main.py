import sys

def Raytrace(r):
    return 0

def main():
    
    # get all system arguments, including source file name 
    fileArgs = sys.argv   
    print(fileArgs)

    # get source filename
    selfFilename = fileArgs[0] 
    print(f" Filename: {selfFilename}")

    # exit program if number of arguments is wrong
    if len(fileArgs) < 2:
        print(f" Usage: {selfFilename} <inputFile>")
        sys.exit() 
        

    # open file
    filePath = fileArgs[1]
    try:
        with open(filePath, 'r') as file:
            data = file.read()
            print(data)
    # catch errors
    except FileNotFoundError:
        print(f" The file at '{filePath}' was not found.")
    except Exception as e:
        print(f" An error occurred: {e}")


    # do raytracing
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

main()
