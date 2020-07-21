adding two arrays:

from array import*
x=array('i',[2,8,7,9])
y=array('i',[4,5,6,3])
z=array('i',[])
for i in range(len(x)):
    k=x[i]+y[i]
    z.append(k)

print(z)


-----users input------


x=[]
z=[]
n=int(input("enter the length of array 'x'="))
print("enter the value: ")
for i in range(n):
    a= int(input(""))
    x.append(a)
print(x)
y=[]
n=int(input("enter the length of array 'y'="))
print("enter the value: ")
for i in range(n):
    a= int(input(""))
    y.append(a)
print(y)
for i in range(len(x)):
    k=x[i]+y[i]
    z.append(k)

print(z)














