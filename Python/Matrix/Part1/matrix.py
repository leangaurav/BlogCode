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
