def multiply_matrix(row,col,b,matrix):
    for i in range(row):
        for j in range(col):
            matrix[i][j]=b*matrix[i][j]
    return matrix
matrix=[]
row=int(input())
col=int(input())
b=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))

#print(matrix)
newmatrix=multiply_matrix(row,col,b,matrix)
print(newmatrix)