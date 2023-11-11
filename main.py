def Raytrace(r):
    return 0

def main():

    # open file
    filePath = "text.txt"
    try:
        with open(filePath, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"The file at '{filePath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    

    # do raytracing
    pixelList = []
    for pixel in pixelList:
        color = Raytrace()

main()