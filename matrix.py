import numpy as np

SMALL_NUMBER = 1e-8

def InvertMatrix(A):
    Ainv = np.zeros_like(A)
    Adjoint(A, Ainv)
    
    det = Det4x4(A)
    
    if np.abs(det) < SMALL_NUMBER:
        print("InvertMatrix: matrix is singular!")
        return None
    
    Ainv /= det
    return Ainv

def Adjoint(inMatrix, outMatrix):

    a1 = inMatrix[0][0]; b1 = inMatrix[0][1]
    c1 = inMatrix[0][2]; d1 = inMatrix[0][3]

    a2 = inMatrix[1][0]; b2 = inMatrix[1][1]
    c2 = inMatrix[1][2]; d2 = inMatrix[1][3]

    a3 = inMatrix[2][0]; b3 = inMatrix[2][1]
    c3 = inMatrix[2][2]; d3 = inMatrix[2][3]

    a4 = inMatrix[3][0]; b4 = inMatrix[3][1]
    c4 = inMatrix[3][2]; d4 = inMatrix[3][3]
    
    outMatrix[0][0] = Det3x3(b2, b3, b4, c2, c3, c4, d2, d3, d4)
    outMatrix[1][0] = -Det3x3(a2, a3, a4, c2, c3, c4, d2, d3, d4)
    outMatrix[2][0] = Det3x3(a2, a3, a4, b2, b3, b4, d2, d3, d4)
    outMatrix[3][0] = -Det3x3(a2, a3, a4, b2, b3, b4, c2, c3, c4)
    
    outMatrix[0][1] = -Det3x3(b1, b3, b4, c1, c3, c4, d1, d3, d4)
    outMatrix[1][1] = Det3x3(a1, a3, a4, c1, c3, c4, d1, d3, d4)
    outMatrix[2][1] = -Det3x3(a1, a3, a4, b1, b3, b4, d1, d3, d4)
    outMatrix[3][1] = Det3x3(a1, a3, a4, b1, b3, b4, c1, c3, c4)
    
    outMatrix[0][2] = Det3x3(b1, b2, b4, c1, c2, c4, d1, d2, d4)
    outMatrix[1][2] = -Det3x3(a1, a2, a4, c1, c2, c4, d1, d2, d4)
    outMatrix[2][2] = Det3x3(a1, a2, a4, b1, b2, b4, d1, d2, d4)
    outMatrix[3][2] = -Det3x3(a1, a2, a4, b1, b2, b4, c1, c2, c4)
    
    outMatrix[0][3] = -Det3x3(b1, b2, b3, c1, c2, c3, d1, d2, d3)
    outMatrix[1][3] = Det3x3(a1, a2, a3, c1, c2, c3, d1, d2, d3)
    outMatrix[2][3] = -Det3x3(a1, a2, a3, b1, b2, b3, d1, d2, d3)
    outMatrix[3][3] = Det3x3(a1, a2, a3, b1, b2, b3, c1, c2, c3)

def Det4x4(m):
    a1, a2, a3, a4 = m[0]
    b1, b2, b3, b4 = m[1]
    c1, c2, c3, c4 = m[2]
    d1, d2, d3, d4 = m[3]

    ans = a1 * Det3x3(b2, b3, b4, c2, c3, c4, d2, d3, d4) \
        - b1 * Det3x3(a2, a3, a4, c2, c3, c4, d2, d3, d4) \
        + c1 * Det3x3(a2, a3, a4, b2, b3, b4, d2, d3, d4) \
        - d1 * Det3x3(a2, a3, a4, b2, b3, b4, c2, c3, c4)
    return ans

def Det3x3(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    ans = a1 * Det2x2(b2, b3, c2, c3) \
        - b1 * Det2x2(a2, a3, c2, c3) \
        + c1 * Det2x2(a2, a3, b2, b3)
    return ans

def Det2x2(a, b, c, d):
    return a * d - b * c

def TestInvert():
    # Example usage:
    A = np.array([[1.0, 2.0, 3.0, 4.0],
                  [5.0, 6.0, 7.0, 8.0],
                  [9.0, 10.0, 11.0, 12.0],
                  [13.0, 14.0, 15.0, 16.0]])

    B = np.array([[5.0, 6.0, 6.0, 8.0],
                  [2.0, 2.0, 2.0, 8.0],
                  [6.0, 6.0, 2.0, 8.0],
                  [2.0, 3.0, 6.0, 7.0]])

    # test A
    Ainv = InvertMatrix(A)
    print("Original matrix:")
    print(A)
    print("\nInverted matrix:")
    print(Ainv)

    # test B
    Binv = InvertMatrix(B)
    print("Original matrix:")
    print(B)
    print("\nInverted matrix:")
    print(Binv)
