import numpy as np

SMALL_NUMBER = 1e-8

def invert_matrix(A):
    Ainv = np.zeros_like(A)
    adjoint(A, Ainv)
    
    det = det4x4(A)
    
    if np.abs(det) < SMALL_NUMBER:
        print("invert_matrix: matrix is singular!")
        return None
    
    Ainv /= det
    return Ainv

def adjoint(in_mat, out_mat):

    '''
    a1, a2, a3, a4, b1, b2, b3, b4 = in_mat[0]
    c1, c2, c3, c4, d1, d2, d3, d4 = in_mat[1]
    e1, e2, e3, e4, f1, f2, f3, f4 = in_mat[2]
    g1, g2, g3, g4, h1, h2, h3, h4 = in_mat[3]
    '''

    a1 = in_mat[0][0]; b1 = in_mat[0][1]
    c1 = in_mat[0][2]; d1 = in_mat[0][3]

    a2 = in_mat[1][0]; b2 = in_mat[1][1]
    c2 = in_mat[1][2]; d2 = in_mat[1][3]

    a3 = in_mat[2][0]; b3 = in_mat[2][1]
    c3 = in_mat[2][2]; d3 = in_mat[2][3]

    a4 = in_mat[3][0]; b4 = in_mat[3][1]
    c4 = in_mat[3][2]; d4 = in_mat[3][3]
    
    out_mat[0][0] = det3x3(b2, b3, b4, c2, c3, c4, d2, d3, d4)
    out_mat[1][0] = -det3x3(a2, a3, a4, c2, c3, c4, d2, d3, d4)
    out_mat[2][0] = det3x3(a2, a3, a4, b2, b3, b4, d2, d3, d4)
    out_mat[3][0] = -det3x3(a2, a3, a4, b2, b3, b4, c2, c3, c4)
    
    out_mat[0][1] = -det3x3(b1, b3, b4, c1, c3, c4, d1, d3, d4)
    out_mat[1][1] = det3x3(a1, a3, a4, c1, c3, c4, d1, d3, d4)
    out_mat[2][1] = -det3x3(a1, a3, a4, b1, b3, b4, d1, d3, d4)
    out_mat[3][1] = det3x3(a1, a3, a4, b1, b3, b4, c1, c3, c4)
    
    out_mat[0][2] = det3x3(b1, b2, b4, c1, c2, c4, d1, d2, d4)
    out_mat[1][2] = -det3x3(a1, a2, a4, c1, c2, c4, d1, d2, d4)
    out_mat[2][2] = det3x3(a1, a2, a4, b1, b2, b4, d1, d2, d4)
    out_mat[3][2] = -det3x3(a1, a2, a4, b1, b2, b4, c1, c2, c4)
    
    out_mat[0][3] = -det3x3(b1, b2, b3, c1, c2, c3, d1, d2, d3)
    out_mat[1][3] = det3x3(a1, a2, a3, c1, c2, c3, d1, d2, d3)
    out_mat[2][3] = -det3x3(a1, a2, a3, b1, b2, b3, d1, d2, d3)
    out_mat[3][3] = det3x3(a1, a2, a3, b1, b2, b3, c1, c2, c3)

def det4x4(m):
    a1, a2, a3, a4 = m[0]
    b1, b2, b3, b4 = m[1]
    c1, c2, c3, c4 = m[2]
    d1, d2, d3, d4 = m[3]

    ans = a1 * det3x3(b2, b3, b4, c2, c3, c4, d2, d3, d4) \
        - b1 * det3x3(a2, a3, a4, c2, c3, c4, d2, d3, d4) \
        + c1 * det3x3(a2, a3, a4, b2, b3, b4, d2, d3, d4) \
        - d1 * det3x3(a2, a3, a4, b2, b3, b4, c2, c3, c4)
    return ans

def det3x3(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    ans = a1 * det2x2(b2, b3, c2, c3) \
        - b1 * det2x2(a2, a3, c2, c3) \
        + c1 * det2x2(a2, a3, b2, b3)
    return ans

def det2x2(a, b, c, d):
    return a * d - b * c

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
Ainv = invert_matrix(A)
print("Original matrix:")
print(A)
print("\nInverted matrix:")
print(Ainv)

# test B
Binv = invert_matrix(B)
print("Original matrix:")
print(B)
print("\nInverted matrix:")
print(Binv)
