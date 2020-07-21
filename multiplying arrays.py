A=[]
n=int(input("enter the length of array 'A'= "))
print("enter the value: ")
for i in range(n):
    a=[]
    for j in range(n):
       a.append (int(input("")))
    A.append(a)
print(A)
B=[]
n=int(input("enter the length of array 'B'="))
print("enter the value: ")
for i in range(n):
    b = []
    for j in range(n):
       b.append (int(input("")))
    B.append(b)
print(B)

print ("display array A in matrix form: ")
for i in range(n):
    for j in range(n):
        print(A[i][j], end="")
    print()

print ("display array B in matrix form: ")
for i in range(n):
    for j in range(n):
        print(B[i][j], end="")
    print()

result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k]*B[k][j]


print("mul of matrix is: ")
for r in result:
    print(r)


------OR-------

A=[]
n=int(input("enter the length of array 'A'= "))
print("enter the value: ")
for i in range(n):
    a=[]
    for j in range(n):
       a.append (int(input("")))
    A.append(a)
print(A)
B=[]
n=int(input("enter the length of array 'B'="))
print("enter the value: ")
for i in range(n):
    b = []
    for j in range(n):
       b.append (int(input("")))
    B.append(b)
print(B)

print ("display array A in matrix form: ")
for i in range(n):

    print(A[i], end="")
    print()

print ("display array B in matrix form: ")
for i in range(n):

    print(B[i], end="")
    print()

result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k]*B[k][j]


print("mul of matrix is: ")
for r in result:
    print(r)



------sysytem input------

A=[
    [2,3,1],
    [4,5,7],
    [8,9,6]
]
print(A)
B=[
    [1,4,7],
    [5,8,2],
    [9,6,1]
]
print(B)

print ("display array A in matrix form: ")
for i in range(len(A)):
    for j in range(len(B)):
      print(A[i][j], end="")
    print()

print ("display array B in matrix form: ")
for i in range(len(B)):
    for j in range(len(B)):
        print(B[i][j], end="")
    print()

result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k]*B[k][j]


print("mul of matrix is: ")
for r in result:
    print(r)


---------OR----------

A=[
    [2,3,1],
    [4,5,7],
    [8,9,6]
]
print(A)
B=[
    [1,4,7],
    [5,8,2],
    [9,6,1]
]
print(B)

print ("display array A in matrix form: ")
for i in range(len(A)):

    print(A[i], end="")
    print()

print ("display array B in matrix form: ")
for i in range(len(B)):

    print(B[i], end="")
    print()

result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k]*B[k][j]


print("mul of matrix is: ")
for r in result:
    print(r)







