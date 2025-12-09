#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in matrix:
        nrow = []
        for j in i:
            z = j*j
            nrow.append(z)
        nmatrix.append(nrow)
    return nmatrix
