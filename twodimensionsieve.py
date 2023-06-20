
import primefac

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

def diophantine(a,b,c,d):
      #a*x+b=c*y+d
  #print(a,"* x +",b,"=",c,"* y +",d)
  A=a
  B=-c
  C=d-b
  #print('A',A,'B',B,'C',C)
  #Step 1 
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
    while(x<0):
        x+=c
    while(x>c):
        x-=c
    y = y1 * (C//gcd)
    while(y<0):
        y+=a
    while(y>a):
        y-=a
    return(0,x,y)
  else:
    return(-2,0,0)#print("Solution not possible") 

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
        yield listofprimes[-1]

def trianglefac():
    listofcomposites=list()
    if len(listofcomposites)==0:
        listofcomposites.append(2)
        yield listofcomposites[-1]
    while True:
        nextstart=len(listofcomposites)
        primegenerator=primegen()
        nextlayer=1
        for layer in range(0,nextstart+1):
            nextlayer*=next(primegenerator)
        listofcomposites.append(listofcomposites[-1]*nextlayer)
        yield listofcomposites[-1]

def binarysplit(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def factors(divisor,modulus):
    toreturn=set()
    multiple=0
    while (divisor*multiple+modulus<divisor**2):
        candidate=divisor*multiple+modulus
        primelist=list(primefac.primefac(candidate))
        CandidatePasses=True
        if GCD(candidate,divisor)[0]!=1:
            CandidatePasses=False
        if CandidatePasses:
            for eachprime in primelist:
                if eachprime>=divisor:
                    CandidatePasses=False
        lenlist=len(primelist)
        partitionvalue=2**len(primelist)
        for partitionscheme in range(1,partitionvalue):
            partitionproduct=1
            scheme=binarysplit(partitionscheme)
            for pos in range(0,len(scheme)):
                if(scheme[pos]):
                    partitionproduct*=primelist[pos]
            if(partitionproduct<=divisor and candidate/partitionproduct<=divisor and CandidatePasses):
                toreturn.add((divisor-partitionproduct+candidate//partitionproduct)%divisor)
                toreturn.add((divisor-candidate//partitionproduct+partitionproduct)%divisor)
        multiple+=1
    return toreturn

if __name__ == "__main__":
    p=21345703
    q=12345701
    p=123456791
    q=233460431
    p=2134567907
    q=1234567891
    p=12345678923
    q=21345678929
    p=123456789133
    q=213456789127
    p=1234516789133
    q=2134516789127
    p=21345703
    q=12345701

    product=p*q
    #primelist=[13,81,125]
    primegenerator=primegen()
    firstprime=next(primegenerator)
    oe=product%4==1
    eo=product%4==3
    primedict=dict()
    primeproduct=1
    for prime in range(1,6):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        #primedict[prime]['prime']=primelist[prime]
        primedict[prime]['mod']=product%primedict[prime]['prime']
        primeproduct*=primedict[prime]['prime']
        primedict[prime]['primeproduct']=primeproduct
        if prime==1:
            primedict[prime]['previousprime']=1
            primedict[prime]['previousprimeproduct']=1
        else:
            primedict[prime]['previousprime']=primedict[prime-1]['prime']
            primedict[prime]['previousprimeproduct']=primedict[prime-1]['primeproduct']
    #print(product,primeproduct,primedict)
    if oe:
        seed=(1,2)
    elif eo:
        seed=(2,1)
    compositeset = set()
    compositeset.add(seed)
    #print(primedict)
    for key in primedict.keys():
        #print('newprime',compositeset)
        newcompositeset=set()
        for element in compositeset:
            newcompositeset.add(element)
            #print('before',element,newcompositeset,compositeset)
            #print('add element',element)
            for multiplierx in range(1,primedict[key]['prime']):
                newcompositeset.add((element[0]+(primedict[key]['previousprimeproduct']*2)*multiplierx,element[1]))
                #print('xelement',(element[0]+(primedict[key]['previousprimeproduct']*2)*multiplierx,element[1]))
            for multipliery in range(1,primedict[key]['prime']):
                newcompositeset.add((element[0],element[1]+(primedict[key]['previousprimeproduct']*2)*multipliery))
                #print('yelement',(element[0],element[1]+(primedict[key]['previousprimeproduct']*2)*multipliery))
                
            for multiplierx in range(1,primedict[key]['prime']):
                for multipliery in range(1,primedict[key]['prime']):
                    #print('element',element,'mx',multiplierx,'my',multipliery)
                    #print((element[0]+2*multiplierx,element[1]+2*multipliery))
                    newcompositeset.add(((element[0]+(primedict[key]['previousprimeproduct']*2)*multiplierx,element[1]+(primedict[key]['previousprimeproduct']*2)*multipliery)))
            #print('after',newcompositeset,compositeset)
        compositeset=set()
        #print(len(newcompositeset))
        #print('before filter',compositeset,newcompositeset)
        for element in newcompositeset:
            if (element[0]+element[1])*(element[0]-element[1])%primedict[key]['prime']==primedict[key]['mod']:
                compositeset.add(element)
        #print('after filter',compositeset,newcompositeset)
        #compositeset=newcompositeset
        #print(len(compositeset))
        
    aveset=set()
    diffset=set()
    for element in compositeset:
        aveset.add(element[0])
        diffset.add(element[1])
    #print(len(aveset))
    #print(compositeset)
    print(product%4,product%primeproduct)
    print(sorted(diffset))
    #print(primedict)
    #print(len(diffset))
'''
        for even in range(2,8,2):
            for odd in range(1,even,2):
                if oe:
                    if ((even+odd)*(even-odd))%key==primedict[key]['mod'] and even-odd>0:
                        compositeset.add((even,odd))
        

    primedict=dict()
    primeproduct=1
    for prime in range(1,5):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        #primedict[prime]['prime']=primelist[prime]
        primedict[prime]['mod']=product%primedict[prime]['prime']
        primeproduct*=primedict[prime]['prime']
    print(product,primeproduct,primedict)
    avediff=set()
    oe=product%4==1
    if oe:
        for odd in range(0,primeproduct*2,2):
            o=odd
            for even in range(1,odd,2):
                e=even
                if GCD(e,o)[0]==1:
                    if oe:
                        val=(o-e)*(o+e)
                    else:
                        val=(e-o)*(e+o)
                    #print(val)
                    addoe=False
                    if val>0:
                        #print(val)
                        addoe=True
                        for prime in range(4,0,-1):
                            #print(val,val%primedict[prime]['prime'],primedict[prime]['mod'])
                            if val%primedict[prime]['prime']!=primedict[prime]['mod']:
                                
                                addoe=False
                                break
                        #print(val,addoe,oe)
                        if addoe and oe:
                            avediff.add((o,e))
                        if addoe and not oe:
                            avediff.add((e,o))
    if not oe:
        for even in range(0,primeproduct*2,2):
            e=even
            for odd in range(1,even,2):
                o=odd
                if GCD(e,o)[0]==1:
                    if oe:
                        val=(o-e)*(o+e)
                    else:
                        val=(e-o)*(e+o)
                    #print(val)
                    addoe=False
                    if val>0:
                        #print(val)
                        addoe=True
                        for prime in range(4,0,-1):
                            #print(val,val%primedict[prime]['prime'],primedict[prime]['mod'])
                            if val%primedict[prime]['prime']!=primedict[prime]['mod']:
                                
                                addoe=False
                                break
                        #print(val,addoe,oe)
                        if addoe and oe:
                            avediff.add((o,e))
                        if addoe and not oe:
                            avediff.add((e,o))
aveset=set()
diffset=set()
for element in avediff:
    aveset.add(element[0])
    diffset.add(element[1])
print('range',primeproduct*2)
print('aveset',sorted(aveset))
print('diffset',sorted(diffset))
print('ave',len(aveset)/(primeproduct*2))
print('diff',len(diffset)/(primeproduct*2))

'''        