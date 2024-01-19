import itertools

def primegen():
    listofprimes=list()
    if len(listofprimes)==0:
        listofprimes.append(2)
        yield listofprimes[-1]
    def isprime(listofprimes,isit):
        for x in listofprimes:
            if isit%x==0:
                return False
        return True
    while True:
        nextstart=listofprimes[-1]+1
        while not isprime(listofprimes,nextstart):
            nextstart+=1
        listofprimes.append(nextstart)
        #print(listofprimes)
        yield listofprimes[-1]

def primeproductuptogen(maxx):
    primegenerator=primegen()
    upto=1
    prime=next(primegenerator)
    while prime<maxx:
        #print('1prime',prime,'upto',upto)
        upto=1
        while (upto*prime)<maxx:
            upto*=prime
            #print('2prime',prime,'upto',upto)
            prime=next(primegenerator)
            #print('3prime',prime,'upto',upto)
        #print('4prime',prime,'upto',upto)
        yield upto
        upto=1
        #print('5prime',prime,'upto',upto)
        prime=next(primegenerator)
        #print('6prime',prime,'upto',upto)
        
        
        
def moddiffgen(prime,mod):
    if mod==0:
        #print('mod is zero, moddiff of a factor impossible')
        yield((1,(0,)))
    pp=set(range(1,prime))
    diffs=set()
    while len(pp):
        #print(pp)
        found=False
        for i in pp:
            for j in pp:
                if (i*j)%prime==mod:
                    if (prime+i-j) not in diffs:
                        #print(i,j,i*j,(i*j)%prime,prime,mod)
                        diffs.add((prime+i-j)%prime)
                        diffs.add((prime+i-j)%prime)
                        yield((prime+i-j)%prime)
                        yield((prime-i+j)%prime)
                    pp.discard(i)
                    pp.discard(j)
                    found=True
                if found:
                    break
            if found:
                break

def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

def diophantine(a,b,c,d):
  #a*x+b=c*y+d
  '''
  a=3
  b=1
  c=5
  d=2
  '''
  #print(a,"* x +",b,"=",c,"* y +",d)
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
  #print(A,B) 
  if A==0 and B==0:
    if C == 0: 
      return(-1,0,0)#print("Infinite Solutions are possible")
    else:
      return(-2,0,0)#print("Solution not possible")
  #Step 2 
  gcd, x1, y1 = GCD(A,B)
  #Step 3 and 4 
  if (C % gcd == 0):
    x = x1 * (C//gcd)
    y = y1 * (C//gcd)
    while(x<0):
        x+=c
    while(x>c):
        x-=c    
    y = y1 * (C//gcd)
    while(y<0):
        y+=a
    while(y>a):
        y-=a
    #print("The values of x and y are: ", x, ",", y)
    #print(a,'*(',c,'* x +',x,")+",b,"=",c,"* (",a,"* y +",y,")+",d)
    return(0,x,y)
  else:
    return(-2,0,0)#print("Solution not possible") 


def generate_grid3(factor1,list1, factor2,list2):
    gridsize=factor1*factor2
    A1=factor1*diophantine(factor1,0,factor2,1)[1]
    A2=factor2*diophantine(factor1,1,factor2,0)[2]
    #print(grid1[1])
    #print(grid2[1])
    #print(A1,A2)
    for a1 in grid1[1]:
        for a2 in grid2[1]:
            candidate=(A1*a2+A2*a1)%gridsize
            #print('A1',A1,'A2',A2,'a1',a1,'a2',a2,'candidate',candidate,'grid1',7,'grid2',11)
            grid[gridsize].add(candidate)
    return (gridsize,tuple(sorted(grid[gridsize])))


    
def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk

#primegenerator=primegen()
#moddiffgenerator=moddiffgen(510510,765049*107133%510510)
#primeproductgenerator=primeproductuptogen(1000000)
for index in range(0,25,1):
    #print('prime',next(primegenerator))
    try:
        pass
    #    print('moddiff',next(moddiffgenerator))
    #    print('primeprod',next(primeproductgenerator))
    except StopIteration:
        pass
print(generate_grid3((13,(2,4,6,7,9,11)),(19,(1,3,5,7,12,14,16,18)),15*19))
