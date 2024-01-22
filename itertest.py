import itertools
import math

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
        
        
        

def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

def floatGCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = floatGCD(math.fmod(b,a), a)
    y1 = s 
    x1 = t - ((b-math.fmod(b,a))/a) * s
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


def floatdiophantine(a,b,c,d):
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
  gcd, x1, y1 = floatGCD(A,B)
  #Step 3 and 4 
  if (C % gcd == 0):
    x = x1 * ((C-math.fmod(C,gcd))/gcd)
    y = y1 * ((C-math.fmod(C,gcd))/gcd)
    while(x<0):
        x+=c
    while(x>c):
        x-=c    
    y = y1 * ((C-math.fmod(C,gcd))/gcd)
    while(y<0):
        y+=a
    while(y>a):
        y-=a
    #print("The values of x and y are: ", x, ",", y)
    #print(a,'*(',c,'* x +',x,")+",b,"=",c,"* (",a,"* y +",y,")+",d)
    return(0,x,y)
  else:
    return(-2,0,0)#print("Solution not possible") 



def generate_grid3(grid1, grid2):
    grid=dict()
    gridsize=grid1[0]*grid2[0]
    grid[gridsize]=set()
    A1=grid1[0]*diophantine(grid1[0],0,grid2[0],1)[1]
    A2=grid2[0]*(diophantine(grid1[0],1,grid2[0],0))[2]
    for a1 in grid1[1]:
        for a2 in grid2[1]:
            candidate=(A1*a2+A2*a1)%gridsize
            grid[gridsize].add(candidate)
    return (gridsize,tuple(sorted(grid[gridsize])))

def generate_grid4(factor1,list1, factor2,list2):
    gridsize=factor1*factor2
    A1=factor1*diophantine(factor1,0,factor2,1)[1]
    A2=factor2*diophantine(factor1,1,factor2,0)[2]
    for a1 in list1:
        for a2 in list2:
            yield((gridsize,(A1*a2+A2*a1)%gridsize))

def moddiffgen(prime,mod):
    if mod==0:
        #print('mod is zero, moddiff of a factor impossible')
        yield((1,(0,)))
    pp=set(range(1,int(prime)))
    diffs=set()
    while len(pp):
        #print(pp)
        found=False
        for i in pp:
            for j in pp:
                if (i*j)%prime==mod:
                    if ((prime+i-j)%prime) not in diffs:
                        #print(i,j,i*j,(i*j)%prime,prime,mod,((prime+i-j)%prime))
                        diffs.add((prime+i-j)%prime)
                        diffs.add((prime-i+j)%prime)
                        yield(prime,(prime+i-j)%prime)
                        if ((prime+i-j)%prime)!=0:
                            yield(prime,(prime-i+j)%prime)
                    pp.discard(i)
                    pp.discard(j)
                    found=True
                if found:
                    break
            if found:
                break

def floatmoddiffgen(prime,mod):
    if mod==0:
        #print('mod is zero, moddiff of a factor impossible')
        yield((1,(0,)))
    pp=set(range(1,int(prime)))
    diffs=set()
    while len(pp):
        #print(pp)
        found=False
        for i in pp:
            for j in pp:
                if  math.fmod((i*j),prime)==mod:
                    if (math.fmod((prime+i-j),prime)) not in diffs:
                        #print(i,j,i*j,(i*j)%prime,prime,mod,((prime+i-j)%prime))
                        diffs.add(math.fmod((prime+i-j),prime))
                        diffs.add(math.fmod((prime-i+j),prime))
                        yield(prime,math.fmod((prime+i-j),prime))
                        if (math.fmod((prime+i-j),prime))!=0:
                            yield(prime,math.fmod((prime-i+j),prime))
                    pp.discard(i)
                    pp.discard(j)
                    found=True
                if found:
                    break
            if found:
                break


def gridgen(factorlist1, factorlist2,maxval):
    islist1=True
    islist2=True
    '''
    try:
        factor1=next(factorlist1)
    except StopIteration:
        islist1=False
    try:
        factor2=next(factorlist2)
    except StopIteration:
        islist2=False
    '''
    #factor2=next(factorlist2)
    gridsize=factorlist1[0][0]*factorlist2[0][0]
    A1=factorlist1[0][0]*diophantine(factorlist1[0][0],0,factorlist2[0][0],1)[1]
    A2=factorlist2[0][0]*diophantine(factorlist1[0][0],1,factorlist2[0][0],0)[2]
    for a1 in factorlist1:
        for a2 in factorlist2:
            if((A1*a2[1]+A2*a1[1])%gridsize<maxval):
                yield((gridsize,(A1*a2[1]+A2*a1[1])%gridsize))
   
def floatgridgen(factorlist1, factorlist2,maxval):
    islist1=True
    islist2=True
    '''
    try:
        factor1=next(factorlist1)
    except StopIteration:
        islist1=False
    try:
        factor2=next(factorlist2)
    except StopIteration:
        islist2=False
    '''
    #factor2=next(factorlist2)
    gridsize=factorlist1[0][0]*factorlist2[0][0]
    A1=factorlist1[0][0]*floatdiophantine(factorlist1[0][0],0,factorlist2[0][0],1)[1]
    A2=factorlist2[0][0]*floatdiophantine(factorlist1[0][0],1,factorlist2[0][0],0)[2]
    for a1 in factorlist1:
        for a2 in factorlist2:
            if(math.fmod((A1*a2[1]+A2*a1[1]),gridsize)<maxval):
                yield((gridsize,math.fmod((A1*a2[1]+A2*a1[1]),gridsize)))



    
def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk

#primegenerator=primegen()
maxval=100
p=163
q=323
d=p*q
#moddiffgenerator=moddiffgen(gridgen(11,5),gridgen(13,6))
floatmoddiffgenerator2=moddiffgen(2.0,d%2.0)
floatmoddiffgenerator3=moddiffgen(3.0,d%3.0)
'''
gridgenerator6=gridgen(list(moddiffgenerator2),list(moddiffgenerator3),d**.5*1.2)
moddiffgenerator5=moddiffgen(5.0,d%5.0)
gridgenerator30=gridgen(list(gridgenerator6),list(moddiffgenerator5),d**.5*1.2)
moddiffgenerator7=moddiffgen(7.0,d%7.0)
gridgenerator210=gridgen(list(gridgenerator30),list(moddiffgenerator7),d**.5*1.2)
moddiffgenerator11=moddiffgen(11.0,d%11.0)
gridgenerator2310=gridgen(list(gridgenerator210),list(moddiffgenerator11),d**.5*1.2)
moddiffgenerator13=moddiffgen(13.0,d%13.0)
gridgenerator30030=gridgen(list(gridgenerator2310),list(moddiffgenerator13),d**.5*1.2)
moddiffgenerator17=moddiffgen(17.0,d%17.0)
gridgenerator510510=gridgen(list(gridgenerator30030),list(moddiffgenerator17),d**.5*1.2)
'''
#moddiffgenerator=moddiffgen(next(gridgenerator1),next(gridgenerator2))
#primeproductgenerator=primeproductuptogen(1000000)
for index in range(0,50,1):
    #print('prime',next(primegenerator))
    try:
        print(next(floatmoddiffgenerator3))
        #print(next(gridgenerator6))
        #print(next(gridgenerator510510),d**.5*1.2)
        #print(next(gridgenerator1))
        #print('moddiff',next(moddiffgenerator))
    #    print('primeprod',next(primeproductgenerator))
    except StopIteration:
        pass
