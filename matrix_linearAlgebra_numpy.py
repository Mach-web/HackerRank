# Task You are given a square matrix A with dimensions N*N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.
import numpy as np

N = int(input())
matrix = np.empty((N, N))

for i in range(N):
    inputs = input().split(" ")
    for index, value in enumerate(inputs):
        matrix[i][index] = float(value)
        
print(round(np.linalg.det(matrix), 2))
