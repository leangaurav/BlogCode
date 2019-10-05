def print_matrix(mat):
    if not mat: # if matrix is empty or None print []
        print("[]")
    else:
        for i in range( len(mat) ):
            for j in range( len(mat[i]) ):
                print( mat[i][j] , end = ' ')
            print()

def input_matrix(m, n):
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
           num = input("Enter element (%d,%d):" % (i,j) )
           row.append(num)
        mat.append(row)
    return mat

def zeros(m,n):
    mat = [ [0 for j in range(n)] for i in range(m) ]
    return mat

def ones(m,n):
    mat = [ [1 for j in range(n)] for i in range(m) ]
    return mat

def copy(mat):
    return [ [data for data in row] for row in mat]

#  Part-2
def create_linear_matrix(m,n):
    start = 1
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(start)
            start += 1
        mat.append(row)
    return mat

def main_diagonal_sum(mat):
    s = 0
    if len(mat) != len(mat[0]):# make sure it is square matrix
        return s
    for i in range(len(mat)):
        s += mat[i][i]
    return s

def off_diagonal_sum(mat):
    s = 0
    if len(mat) != len(mat[0]):# make sure it is square matrix
        return s
    l = len(mat)
    for i in range(l):
        s += mat[i][l - i - 1]
    return s

def add_scalar(mat, scalar, inplace = False):
    if inplace:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] += scalar
        return False
    else:
        res = []
        for i in range(len(mat)):
            row = []
            for j in range(len(mat[0])):
                row.append(mat[i][j] + scalar)
            res.append(row)
        return res

def sub_scalar(mat, scalar, inplace = False):
    # Implement
    pass

def mul_scalar(mat, scalar, inplace = False):
    # Implement
    pass
    
def equals(lhs, rhs):
    if id(lhs) == id(rhs): # if user passes same matrix in lhs and rhs
        return True
        
    if len(lhs) != len(rhs) or len(lhs[0]) != len(rhs[0]):
        return False # dimensions are not same
    
    for i in range(len(lhs)):
        for j in range(len(lhs[0])):
            if lhs[i][j] != rhs[i][j]: #return false if any element doesn't match
                return False
    
    return True # everything is good
    
def add(lhs, rhs):
    if len(lhs) == 0 or len(rhs) == 0 \
        or (len(lhs) != len(rhs)) or (len(lhs[0]) != len(rhs[0])):
        return None # sad part first
       
    res = []
    for i in range(len(lhs)):
        row = []
        for j in range(len(lhs[0])):
            row.append(lhs[i][j] + rhs[i][j])
        res.append(row)
    return res

def sub(lhs, rhs):
    if len(lhs) == 0 or len(rhs) == 0 \
        or (len(lhs) != len(rhs)) or (len(lhs[0]) != len(rhs[0])):
        return None # sad part first
       
    res = []
    for i in range(len(lhs)):
        row = []
        for j in range(len(lhs[0])):
            row.append(lhs[i][j] - rhs[i][j])
        res.append(row)
    return res
    
def transpose(mat):
    trans = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        trans.append(row)
    return trans
    
def neg(mat, inplace = False):
    if inplace:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = -mat[i][j]
        return None
    else:
        res = []
        for i in range(len(mat)):
            row = []
            for j in range(len(mat[0])):
                row.append(-mat[i][j])
            res.append(row)
        return res