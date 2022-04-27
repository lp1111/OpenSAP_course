"""
Write a program that lets the user input a two-dimensional matrix (Hint: you could use a list of lists to store the matrix).
The program should first ask the user how many rows and columns the matrix should contain.
Next, the program should ask the user for the elements of the matrix.
Your program should read the values from the user row by row.
If, for example, the matrix has the dimension 2 by 3, the values should be read as follows:

First row, first value
First row, second value
First row, third value
Second row, first value
Second row, second value
Second row, third value
Finally, the program should calculate and print the sums of the values in each row.
"""

i = int(input("Type the number of rows:", ))
j = int(input("Type the number of columns:", ))
matrix = []

for a in range(i):
    matrix.append([])
    for b in range(j):
        c = int(input("row" + " " + str(a + 1) + " " + "column" + " " + str(b + 1) + ":"))
        matrix[a].append(c)

for d in range(len(matrix)):
    suma = sum(matrix[d])
    print("Sum of row" + " " + str(d + 1) + ":" + str(suma), )




