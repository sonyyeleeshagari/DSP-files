print("enter the order of matrix:")
a=input("enter the no.of rows for first matrix=")
b=input("enter the no.of coloumns for first matrix=")
c=input("enter the no.of rows for second matrix=")
d=input("enter the no.of coloumns for second matrix=")
e=[]
f=[]
print("enter the elements for matrix1:")
for i in range (0,a,1):
	for j in range(0,b,1):
		e[i,j]=int(input("enter the elements="))
print("enter the elements for matrix2:")
for i in range(0,a,1):
	for j in range(0,b,1):
		f[i,j]=int(input("enter the elements="))
c=[]
for i in range(0,a,1):
	for j in range(0,b,1):
		c[i,j]=0
print("multiplication of two matrices is=")
for i in range(0,a,1):
	for j in range(0,b,1):
		for k in range(0,b,1):
			c[i,j]=c[i,j]+(e[i,j]*f[k,j])
print c
