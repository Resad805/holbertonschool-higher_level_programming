#!/usr/bin/python3

    
def square_matrix_simple(matrix=[]):
    nmatrix = []
    nrow = []
    for i in matrix:
        for j in i:
            nrow.append(i*i)
        nmatrix.append(nrow)
    return nmatrix
