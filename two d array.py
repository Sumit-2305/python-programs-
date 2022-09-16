m = int(input("Input number of rows: "))
n = int(input("Input number of columns: "))
array = [[0 for col in range(n)] for row in range(m)]

for row in range(m):
    for col in range(n):
        array[row][col]= row*col

print(array)

