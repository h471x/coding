n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = input("Enter the element at position ({}, {}): ".format(i, j))
        row.append(element)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)
