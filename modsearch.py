import primefac
import pprint
#print(list(primefac.primefac(2999999)))
pp=pprint.PrettyPrinter(indent=2)

def binarysplit(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]
#extended GCD
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
    if(x<=0):
        x+=a
    y = y1 * (C//gcd)
    if(y<=0):
        y+=c
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



'''
Get possible mod factors
For some p and q
The product of p and q is d
-----------------------------
The modulus of d by some number a
Is the modulus of 
    The modulus of p by a 
    multilied by 
    the modulust of q by a
by a
equals the modulus of d by a
-----------------------------
The modulus of p by a 
multilied by 
the modulust of q by a
equals
the modulus of d by a
plus a multiple of a
-----------------------------
For each multiple of a plus 
the modulus of d by a
get the prime factorisation
-----------------------------
partition each prime factorisation
of each multiple of a plus
the modulust of d by a
partition the prime factorisation into 2 partitions
-----------------------------
Get the product of each partition
-----------------------------
a pair of product of a pair of partitions will be the moduli of p and q by a
-----------------------------
for each product add a multiple of a to get p or q
'''




def factors(divisor):
    #initialise dictionary to return
    toreturn=dict()
    #for each possible moduli        
    for modulus in range(1,divisor):
        #initialise set in dictionary to return possible factors
        toreturn[(divisor,modulus)]=set()
        #The multiple of the divisor
        multiple=1
        #print('divisor ',i,' modulus ',j)
        while (divisor*multiple+modulus<divisor**2):
            #candidate modulus product
            candidate=divisor*multiple+modulus
            #get prime factorisation of candidate
            primelist=list(primefac.primefac(candidate))
            CandidatePasses=True
            for eachprime in primelist:
                if eachprime>=divisor:
                    CandidatePasses=False
            #get the number of primes in the candidate prime factorisation
            lenlist=len(primelist)
            #use binary split of the list of primes
            #For each binary split of the prime list get the product of the partition
            partitionvalue=2**len(primelist)
            for partitionscheme in range(1,partitionvalue):
                partitionproduct=1
                scheme=binarysplit(partitionscheme)
                #print(partitionscheme,scheme)
                for pos in range(0,len(scheme)):
                    if(scheme[pos]):
                        partitionproduct*=primelist[pos]
                if(partitionproduct%2==0 or (candidate/partitionproduct)%2==0):
                    CandidatePasses=False
                if(partitionproduct<=divisor and candidate/partitionproduct<=divisor and CandidatePasses):
                    #moddict[(i,j)].add((partitionproduct*candidate//partitionproduct,partitionproduct,candidate//partitionproduct))
                    toreturn[(divisor,modulus)].add((partitionproduct))
                    toreturn[(divisor,modulus)].add(candidate//partitionproduct)
            
            multiple+=1
    #print (toreturn)
    return toreturn
            
    '''
    delete = [key for key in moddict if len(moddict[key])>key[0]/4]
    for key in delete:
        del moddict[key]
    '''
    #for key in ((2*3*5,144871%2*3*5),(2*3*7,144871%2*3*7)):
    #    print(key,moddict[key])







def moddicts(intlist):
    toreturn=dict()        
    for i in (intlist):
        
        for j in range(1,i):
            toreturn[(i,j)]=set()
            k=1
            #print('divisor ',i,' modulus ',j)
            while (i*k+j<i**2):
                candidate=i*k+j
                primelist=list(primefac.primefac(candidate))
                p=1
                for e in primelist:
                    if e>=i:
                        p=0
                lenlist=len(primelist)
                #pp.pprint(primelist)
                partitionvalue=2**len(primelist)
                for partitionscheme in range(1,partitionvalue):
                    partitionproduct=1
                    scheme=trans(partitionscheme)
                    #print(partitionscheme,scheme)
                    for pos in range(0,len(scheme)):
                        if(scheme[pos]):
                            partitionproduct*=primelist[pos]
                    if(partitionproduct<=i and candidate/partitionproduct<=i and p):
                        #moddict[(i,j)].add((partitionproduct*candidate//partitionproduct,partitionproduct,candidate//partitionproduct))
                        toreturn[(i,j)].add((partitionproduct))
                        toreturn[(i,j)].add(candidate//partitionproduct)
                
                k+=1
    #print (toreturn)
    return toreturn
            
    '''
    delete = [key for key in moddict if len(moddict[key])>key[0]/4]
    for key in delete:
        del moddict[key]
    '''
    #for key in ((2*3*5,144871%2*3*5),(2*3*7,144871%2*3*7)):
    #    print(key,moddict[key])
#testdict=moddicts((30,42))

def primekproduct(d):
    primegenerator = primegen()
    root4d=(d**.25)//1
    #rootdthird=(rootd/3**.25)//1
    primeproduct=1
    listofkprimes=list()
    prime1=next(primegenerator)
    prime2=next(primegenerator)
    prime3=next(primegenerator)
    primeproduct*=prime1
    listofkprimes.append(prime1)
    while primeproduct*prime2 < root4d:
        listofkprimes.append(next(primegenerator))
        primeproduct*=listofkprimes[-1]
    #first=primegenerator.gi_frame.f_locals['listofprimes'][-1]
    first=listofkprimes[-1]
    start=primeproduct//first
    print('first start',start,rootdthird-start,first,(rootdthird-start)/first)
    multiplier=0
    while(listofkprimes[multiplier]*start<rootdthird):
        multiplier+=1
    multiplier-=1
    start*=listofkprimes[multiplier]
    print('second start',start,rootdthird-start,first,(rootdthird-start)/first)

    listoflprimes=list()
    listoflprimes.append(first)
    #print (d,(d**.5)//1,(d**.5/3**.5)//1,primeproduct,first,primeproduct//first)
    start=primeproduct//first
    #print('try1',first)
    if (d%(start+first)==0):
        print('factors found1:',start+first,d/(start+first))
    nextp=next(primegenerator)
    #print('try2',nextp)
    listoflprimes.append(nextp)


    






if __name__ == "__main__":
    product=144871
    divisor1=30
    divisor2=42
    factordict=factors(divisor1)
    trialdict=dict()
    for key in factordict.keys():
        trialdict[key]=factordict[key]
    factordict=factors(divisor2)
    for key in factordict.keys():
        trialdict[key]=factordict[key]
    for key in trialdict.keys():
        pass
        #print (key,'->',trialdict[key])
    factors1=list()
    for factor in trialdict[divisor1,product%divisor1]:
        factors1.append(factor)
        #print(factor)
    factors2=list()
    for factor in trialdict[divisor2,product%divisor2]:
        factors2.append(factor)
        #print(factor)
    #print(factors1)
    #print(factors2)
    factorfunctions1=dict()
    factorfunctions2=dict()
    for factor1 in factors1:
        for factor2 in factors2:
            factorfunctions1[(factor1,factor2)]=(diophantine(divisor1,factor1,divisor2,factor2))    
    for factorfunction in factorfunctions1.keys():
        if(factorfunctions1[factorfunction][0]==0):
            print(factorfunction)
            print(factorfunctions1[factorfunction])
        #for function in factorfunction.keys():
            #if function[0]==0:
                #print(factorfunction.key(),function)
            #print(factorfunctions1[factorfunctions])
            #factorfunctions2.append((divisor1,divisor2,factorfunction[1],product%divisor1))
            #factorfunctions2.append((divisor2,divisor1,factorfunction[2],product%divisor2))
    for factorfunction in factorfunctions1:
        pass
        #print(factorfunction)
        #print(factorfunction[0],'* (',factorfunction[1],'+',factorfunction[2],') +',factorfunction[3])
        #print(factorfunction[0]* factorfunction[1],'* x +',factorfunction[0]*factorfunction[2]+factorfunction[3])

    """
    trialdict=list()     
    #print((30,144871%30),sorted(testdict[(30,144871%30)]))                
    #print((42,144871%42),sorted(testdict[(42,144871%42)]))                
    for i in  sorted(testdict[(30,144871%30)],reverse=True):
        for j in sorted(testdict[(42,144871%30)],reverse=True):
            (w,x,y)=diophantine(30,i,42,j)
            if(w==0):
                #print(30,'*(',42,'* x +',x,")+",i,"=",42,"* (",30,"* y +",y,")+",j)
                trialdict.append((144871,30,42,30*42,i,30,x))
                trialdict.append((144871,30,42,30*42,j,42,y))
    def first(elem):
        return elem[5]*elem[6]
    trialsorted=sorted(trialdict, reverse=True, key=first)
    for ts in trialsorted:
        #ts[0]=d
        #ts[1]=firstdiv
        #ts[2]=seconddiv
        #ts[3]=product of firstdiv and seconddiv
        #ts[4]=mod of this div
        #ts[5]=this div
        #ts[6]=x or y
        print(ts[0]%ts[1],ts[0]%ts[2],ts[4],ts[6])        
    """