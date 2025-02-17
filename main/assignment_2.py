
import numpy as np

# Question 1
def neville_interpolation(x_values, y_values, x):

    n = len(x_values)
    q = [[0.0] * n for _ in range(n)]

    for i in range(n):
        q[i][0] = y_values[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i][j] = ((x - x_values[i - j]) * q[i][j - 1] - (x - x_values[i]) * q[i - 1][j - 1]) / (x_values[i] - x_values[i - j])

    return q[n - 1][n - 1]


x_values = [3.6, 3.8, 3.9]
y_values = [1.675, 1.436, 1.318]

interpolated_value = neville_interpolation(x_values[:3], y_values[:3], 3.7)

print("Question 1")
print(f"2nd degree interpolating value for f(3.7): {interpolated_value}")
print("---------------------------------------------------------------------")



# Question 2
x = [7.2, 7.4, 7.5, 7.6]
y = [23.5492, 25.3913, 26.8224, 27.4589]

poly = [] 

for i in range(len(x)): 
    poly.append(y[i]) 


for j in range(1, len(x)): 
    for i in range(len(x)-1, j-1, -1): 
        poly[i] = (poly[i]-poly[i-1])/(x[i]-x[i-j]) 

print("Question 2")
print(poly[1:])
print("---------------------------------------------------------------------")



# Question 3
