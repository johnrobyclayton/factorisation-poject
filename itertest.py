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

def moddiff(prime,mod):
    if mod==0:
        #print('mod is zero, moddiff of a factor impossible')
        return((1,(0,)))
    pp=set(range(1,int(prime)))
    diffs=set()
    toreturn=[]
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
                        toreturn.append((prime+i-j)%prime)
                        if ((prime+i-j)%prime)!=0:
                            toreturn.append((prime-i+j)%prime)
                    pp.discard(i)
                    pp.discard(j)
                    found=True
                if found:
                    break
            if found:
                break
    return toreturn

def MULINV(a,b):
    gcd,x,y=GCD(a,b)
    if x<0:
        return x+b
    else:
        return x
    
def diophantine_base(x,y):
    #diophantine ax+b=cy+d
    #example 3x+2=5y+3
    #   0 | 1 | 2 | 3 | 4
    # --------------------- 
    #0| 0 | 6 |12 | 3 | 9
    #1|10 | 1 | 7 |13 | 4
    #2| 5 |11 | 2 | 8 |14
    # result is 15x+8
    # diophantine_base is values at coordinates (0,1) and (1,0)
    # return (10,6)
    # return y*(multiplicative inverse of x to modulus y) , x*(multiplicative inverse of y to modulus x)
    #   0 | 1 | 2 
    # ------------ 
    #0| 0 |10 | 5 
    #1| 6 | 1 |11 
    #2|12 | 7 | 2 
    #3| 3 |13 | 8
    #4| 9 | 4 |14
    invxy=MULINV(x,y)
    invyx=MULINV(y,x)
    return(x*invxy,y*invyx)


def moddiffdict(d,start=1):
    #print('moddiffdict')
    primegenerator=primegen()
    eat=1
    prime=next(primegenerator)
    while eat*prime<start:
        eat*=prime
        prime=next(primegenerator) 
    toreturn=list()
    primeproduct=1
    while not primeproduct>d:
        
        prime=next(primegenerator)
        toreturn.append(dict())
        currentindex=len(toreturn)-1
        toreturn[currentindex]["prime"]=prime
        toreturn[currentindex]["primeproduct"]=primeproduct
        toreturn[currentindex]["diffs"]=tuple(sorted(moddiff(prime,d%prime)))#[1],reverse=True))
        toreturn[currentindex]['mod']=d%prime
        toreturn[currentindex]["diafbase"]=diophantine_base(primeproduct,prime)
        toreturn[currentindex]["accumulated"]=0
        toreturn[currentindex]["diff"]=0
        toreturn[currentindex]["maxp"]=0
        primeproduct*=prime
    return toreturn


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
        print('mod is zero, moddiff of a factor impossible')
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
p=1680013
q=3300001
d=p*q
#moddiffgenerator=moddiffgen(gridgen(11,5),gridgen(13,6))
floatmoddiffgenerator2=floatmoddiffgen(2.0,math.fmod(d,2.0))
floatmoddiffgenerator3=floatmoddiffgen(3.0,math.fmod(d,3.0))

floatgridgenerator6=floatgridgen(list(floatmoddiffgenerator2),list(floatmoddiffgenerator3),d**.5*1.2)
floatmoddiffgenerator5=floatmoddiffgen(5.0,math.fmod(d,5.0))

floatgridgenerator30=floatgridgen(list(floatgridgenerator6),list(floatmoddiffgenerator5),d**.5*1.2)
floatmoddiffgenerator7=floatmoddiffgen(7.0,math.fmod(d,7.0))

floatgridgenerator210=floatgridgen(list(floatgridgenerator30),list(floatmoddiffgenerator7),d**.5*1.2)
floatmoddiffgenerator11=floatmoddiffgen(11.0,math.fmod(d,11.0))
floatgridgenerator2310=floatgridgen(list(floatgridgenerator210),list(floatmoddiffgenerator11),d**.5*1.2)
floatmoddiffgenerator13=floatmoddiffgen(13.0,math.fmod(d,13.0))
floatgridgenerator30030=floatgridgen(list(floatgridgenerator2310),list(floatmoddiffgenerator13),d**.5*1.2)
floatmoddiffgenerator17=floatmoddiffgen(17.0,math.fmod(d,17.0))
floatgridgenerator510510=floatgridgen(list(floatgridgenerator30030),list(floatmoddiffgenerator17),d**.5*1.2)
floatmoddiffgenerator19=floatmoddiffgen(19.0,math.fmod(d,19.0))
floatgridgenerator9699690=floatgridgen(list(floatgridgenerator510510),list(floatmoddiffgenerator19),d**.5*1.2)
floatmoddiffgenerator23=floatmoddiffgen(23.0,math.fmod(d,23.0))
floatgridgenerator23=floatgridgen(list(floatgridgenerator9699690),list(floatmoddiffgenerator23),d**.5*1.2)
floatmoddiffgenerator29=floatmoddiffgen(29.0,math.fmod(d,29.0))
floatgridgenerator29=floatgridgen(list(floatgridgenerator23),list(floatmoddiffgenerator29),d**.5*1.2)
floatmoddiffgenerator31=floatmoddiffgen(31.0,math.fmod(d,31.0))
floatgridgenerator31=floatgridgen(list(floatgridgenerator29),list(floatmoddiffgenerator31),d**.5*1.2)
floatmoddiffgenerator37=floatmoddiffgen(37.0,math.fmod(d,37.0))
floatgridgenerator37=floatgridgen(list(floatgridgenerator31),list(floatmoddiffgenerator37),d**.5*1.2)
floatmoddiffgenerator41=floatmoddiffgen(41.0,math.fmod(d,41.0))
floatgridgenerator41=floatgridgen(list(floatgridgenerator37),list(floatmoddiffgenerator41),d**.5*1.2)
floatmoddiffgenerator43=floatmoddiffgen(43.0,math.fmod(d,43.0))
floatgridgenerator43=floatgridgen(list(floatgridgenerator41),list(floatmoddiffgenerator43),d**.5*1.2)
floatmoddiffgenerator47=floatmoddiffgen(47.0,math.fmod(d,47.0))
floatgridgenerator47=floatgridgen(list(floatgridgenerator43),list(floatmoddiffgenerator47),d**.5*1.2)
floatmoddiffgenerator53=floatmoddiffgen(53.0,math.fmod(d,53.0))

#moddiffgenerator=moddiffgen(next(gridgenerator1),next(gridgenerator2))
#primeproductgenerator=primeproductuptogen(1000000)
for index in range(0,0,1):
    #print('prime',next(primegenerator))
    try:
        print(next(floatgridgenerator47))
        print(next(floatmoddiffgenerator53))
        #print(next(gridgenerator510510),d**.5*1.2)
        #print(next(gridgenerator1))
        #print('moddiff',next(moddiffgenerator))
    #    print('primeprod',next(primeproductgenerator))
    except StopIteration:
        pass
print(moddiff(13,1))
#print(moddiffdict(123456,1))