#temp variable for creating matrix
matrix1=[]
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input("enter first matrix values : "))
        row.append(value)
    matrix1.append(row)
print("first matrix result is ",matrix1)
matrix2=[]
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input("entersecond matrix values :  "))
        row.append(value)
    matrix2.append(row)
print("second matrix result is ",matrix2)
sum1=[]
sum2=[]
for i in range(2):
    for j in range(2):
        sum1=matrix1[i][j]+matrix2[i][j]
    sum2.append(sum1)
print(sum2)


