matrix1=[]
matrix_rows=int(input("enter a row  records : "))
matrix_cols=int(input("enter a col records : "))
for r in range(matrix_rows):
    row_values=[]
    for c in range(matrix_cols):
        matrix2=int(input("enter a row values :  "))
        row_values.append(matrix2)
    matrix1.append(row_values)
for row in matrix1:
    for col in row: 
        print(col,end=" ")
    print()
