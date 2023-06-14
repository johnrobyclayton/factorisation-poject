def initialeo(n):
    return 4+8*n

def initialoe(n):
    return 8*n

def initialaccumeo(n):
    return 4*n+8*((n**2+n)//2)+3

def initialaccumoe(n):
    return 8*((n**2+n)//2)-3

def oetest(n):
    return n%4==1

def eotest(n):
    return n%4==3    

if __name__ == "__main__":
    for i in range(0,5):
        print(initialeo(i),initialaccumeo(i),initialoe(i),initialaccumoe(i))