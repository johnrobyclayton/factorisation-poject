#Function for Extended Euclidean 
def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

#solve ax+b=cy+d given a,b,c,d

#a*x+b=c*x+d
#A=a
#B=-c
#C=d-b
#A*x+B*x=C
a=3
b=1
c=5
d=2
print(a,"* x +",b,"=",c,"* y +",d)
A=a
B=-c
C=d-b


'''
#Solve: 3x + 6y = 9 
#x
a = 3
#b
b = -5
#c
c = 2
'''
#Step 1 
if A==0 and B==0:
  if C == 0: 
    print("Infinite Solutions are possible")
  else:
    print("Solution not possible")

#Step 2 
gcd, x1, y1 = GCD(A,B)

#Step 3 and 4 
if (C % gcd == 0):
  x = x1 * (C//gcd)
  y = y1 * (C//gcd)
  print("The values of x and y are: ", x, ",", y)
  print(a,'*(',c,'* x +',x,")+",b,"=",c,"* (",a,"* y +",y,")+",d)
else:
  print("Solution not possible") 
 
    