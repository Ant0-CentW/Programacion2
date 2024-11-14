M=[[1,2,3,],[4,5,6],[7,8,9]]
suma=0
mult=1
sum=0
mult=0
for i in range(3):
    for j in range (3):
        f=i==j
        print(M[i][j])
        suma=sum+M[i][j]
        multi=mult*M[i][j]
