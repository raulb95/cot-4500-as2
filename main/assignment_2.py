
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
print("2nd degree interpolating value for f(3.7):", (interpolated_value))
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
result = 0
for i in range(len(poly)): 
    term = poly[i] 
    for j in range(i): 
        term = term * (7.3 - x[j]) 
    result += term 

print("Question 3")
print(result)
print("---------------------------------------------------------------------")



# Question 4

"""x = np.array([3.6, 3.8, 3.9])
f = np.array([1.675, 1.436, 1.318])
df = np.array([-1.195, -1.118, -1.182])"""

print("Question 4")
print("---------------------------------------------------------------------")



# Question 5
x_data = np.array([2, 5, 8, 10])
y_data = np.array([3, 5, 7, 9])

n = len(x_data)
A = np.zeros((n, n))
A[0, 0] = 1
A[n-1, n-1] = 1
for i in range(1, n-1):
    A[i, i-1] = x_data[i] - x_data[i-1]
    A[i, i] = 2 * (x_data[i+1] - x_data[i-1])
    A[i, i+1] = x_data[i+1] - x_data[i]

b = np.zeros(n)
for i in range(1, n-1):
    b[i] = 3 * (y_data[i+1] - y_data[i]) / (x_data[i+1] - x_data[i]) - \
           3 * (y_data[i] - y_data[i-1]) / (x_data[i] - x_data[i-1])

x = np.linalg.solve(A, b)

print("Question 5")
print("A:")
print(A)
print("B:")
print(b)
print("C:")
print(x)