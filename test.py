import sys
import re
import numpy as np
import constants 
import program
import ppm
import sphere
import light
import color
import ray

def testColorAdd(c1, c2):
    c1.AddColor(c2)
    print(c1)
    return c1 


def main():

    c1 = color.Color(0.5, 0.6, 0.7)
    c2 = color.Color(0.1, 0.2, 0.3)
    testColorAdd(c1, c2)
    
    x = color.Color(0, 0.1, 0.2)
    y = color.Color(0.2, 0.3, 0.4)
    z = color.Color(0.1, 0.1, 0.1)
    result = x.value + y.value + z.value
    print(result)


    return 0

main()
