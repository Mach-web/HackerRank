# Task You are given a square matrix A with dimensions N*N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.
'''
Link to the problem:
https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''
import numpy as np

N = int(input())
# instantiate an empty array
matrix = np.empty((N, N))

for i in range(N):
    inputs = input().split(" ")
    for index, value in enumerate(inputs):
        matrix[i][index] = float(value)
# find the determinant
print(round(np.linalg.det(matrix), 2))
