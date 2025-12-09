#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    
def square_matrix_simple(matrix=[]):
    nmatrix = []
    nrow = []
    for i in matrix:
        for j in i:
            nrow.append(i*i)
        nmatrix.append(nrow)
    return nmatrix
