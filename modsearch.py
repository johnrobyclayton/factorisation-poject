import primefac
import pprint
import math
import decimal
from decimal import Decimal
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




def factors(modulus,divisor,listofkprimes):
    #initialise dictionary to return
    toreturn=dict()
    toreturn[(divisor,modulus)]=set()
    #The multiple of the divisor
    multiple=0
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
            for prime in listofkprimes:
                if(partitionproduct%prime==0 or (candidate/partitionproduct)%prime==0):
                    CandidatePasses=False
                    break
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
                    scheme=binarysplit(partitionscheme)
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
    primek=dict()
    klist=list()
    klist.append(dict())
    klist.append(dict())
    klist[0]['listofkprimes']=list()
    klist[0]['primeproduct']=1
    klist[1]['listofkprimes']=list()
    klist[1]['primeproduct']=1
    primegenerator = primegen()
    rootd=(d**.5)//1
    rootdthird=((rootd/(3**.5))**.5)//1
    #primeproduct=1
    #listofkprimes=list()
    prime1=next(primegenerator)
    prime2=next(primegenerator)
    prime3=next(primegenerator)
    print(d,d**.5,(d**.5)/(3**.5),((d**.5)/(3**.5))**.5,rootdthird)
    print(((42**2)*(3**.5))**2)
    klist[0]['primeproduct']*=prime1
    klist[0]['listofkprimes'].append(prime1)
    klist[0]['primeproduct']*=prime2
    klist[0]['listofkprimes'].append(prime2)
    klist[1]['primeproduct']*=prime1
    klist[1]['listofkprimes'].append(prime1)
    klist[1]['primeproduct']*=prime2
    klist[1]['listofkprimes'].append(prime2)
    while klist[0]['primeproduct']*prime3 < rootdthird:
        klist[0]['primeproduct']*=prime3
        klist[0]['listofkprimes'].append(prime3)
        klist[1]['primeproduct']*=prime3
        klist[1]['listofkprimes'].append(prime3)
        prime1=prime2
        prime2=prime3
        prime3=next(primegenerator)
    klist[0]['primeproduct']//=prime2
    klist[0]['listofkprimes'].pop()   
    klist[0]['primeproduct']//=prime1
    klist[0]['listofkprimes'].pop() 
    klist[1]['primeproduct']//=prime2
    klist[1]['listofkprimes'].pop()   
    klist[1]['primeproduct']//=prime1
    klist[1]['listofkprimes'].pop() 
    klist[0]['primeproduct']*=prime1
    klist[0]['listofkprimes'].append(prime1)
    klist[1]['primeproduct']*=prime2
    klist[1]['listofkprimes'].append(prime2)
    #print(klist)
    return klist
 


def primedisjointproduct(d):
    klist=list()
    klist.append(dict())
    klist.append(dict())
    klist[0]['listofkprimes']=list()
    klist[0]['primeproduct']=1
    klist[1]['listofkprimes']=list()
    klist[1]['primeproduct']=1
    primegenerator = primegen()
    rootd=(d**.5)//1
    rootdthird=((rootd/(3**.5))**.5)//1
    #primeproduct=1
    #listofkprimes=list()
    prime1=next(primegenerator)
    prime2=next(primegenerator)
    klist[0]['primeproduct']*=prime1
    klist[0]['listofkprimes'].append(prime1)
    while klist[0]['primeproduct']*prime2 < rootdthird:
        klist[0]['primeproduct']*=prime2
        klist[0]['listofkprimes'].append(prime2)
        prime1=prime2
        prime2=next(primegenerator)
    prime1=prime2
    prime2=next(primegenerator)
    klist[1]['primeproduct']*=prime1
    klist[1]['listofkprimes'].append(prime1)
    while klist[1]['primeproduct']*prime2 < rootdthird:
        klist[1]['primeproduct']*=prime2
        klist[1]['listofkprimes'].append(prime2)
        prime1=prime2
        prime2=next(primegenerator)
    #print(klist)
    return klist

def primemoddiff(p,m):
    toreturn=set()
    for i in range(1,p):
        for j in range(1,p):
            if (i*j)%p==m:
                toreturn.add((p-i+j)%p)
                toreturn.add((p-j+i)%p)
    return toreturn

def combinedifflists(firstdifflist,seconddifflist):
    #print('fs',firstdifflist,seconddifflist)
    returndifflistkey=firstdifflist[0]*seconddifflist[0]
    returndifflist=list()
    #returndifflist.append(0)
    #print('fs1',firstdifflist[1])
    #print('se1',seconddifflist[1])
    for firstdiff in firstdifflist[1]:
        for seconddiff in seconddifflist[1]:
            a=firstdifflist[0]
            b=firstdiff
            c=seconddifflist[0]
            d=seconddiff
            #diofresult=diophantine(firstdifflist[0],firstdiff,seconddifflist[0],seconddiff)
            diofresult=diophantine(a,b,c,d)
            #print('difresult',diofresult)
            #print(firstdifflist[0]*diofresult[1]+firstdiff,
            #      seconddifflist[0]*diofresult[2]+seconddiff)
            #print(a*diofresult[1]+b,
            #      c*diofresult[2]+d)
            if(diofresult[0]==0):
                #print(firstdifflist[0],firstdiff,seconddifflist[0],seconddiff,diofresult)
                returndifflist.append(a*diofresult[1]+b)
    #print(returndifflist)
    return(returndifflistkey,returndifflist)
#(a,b,c,d)=(3,0,5,4)
#diofresult=diophantine(3,0,5,4)
#print(diofresult,a*diofresult[1]+b, c*diofresult[2]+d)
#main

if __name__ == "__main__":
    p=123456791
    q=233460431
    p=21345703
    q=12345701
    product=p*q
    root4d=(product**.3)//1
    primegenerator = primegen()
    primeproduct=1
    lenlist=1
    prime=next(primegenerator)#2
    prime=next(primegenerator)#3
    #prime=4
    diffdict=dict()
    while primeproduct<root4d:
        difflist=list(sorted(primemoddiff(prime,product%prime)))
        diffdict[prime]=difflist
        primeproduct*=prime
        #prime+=1
        prime=next(primegenerator)
    #print(moddict)    
    #print(pqmoddiffdict)
    #print(diffdict) 
    primedifflist=list()
    
    for key in sorted(diffdict.keys(),reverse=True):
        primedifflist.append(key)
    
    #print('primedifflist',primedifflist)
    difflistkey=primedifflist.pop()
    #print(difflistkey,primedifflist)
    
    combineddifflist=(difflistkey,diffdict[difflistkey])
    #print(combineddifflist)
    
    while primedifflist:
        difflistkey=primedifflist.pop()
        #print(difflistkey,primedifflist)
        nextdifflist=(difflistkey,diffdict[difflistkey])
        #print(nextdifflist)
        #print('interim',combineddifflist,nextdifflist)
        combineddifflist=combinedifflists(combineddifflist,nextdifflist)
    oddlist=list()
    evenlist=list()
    for element in sorted(combineddifflist[1]):
        if element&1:
            oddlist.append(element)
        else:
            evenlist.append(element)
    found=False
    mul=0
    print('1',combineddifflist[0],combineddifflist[1])
    #print(sorted(oddlist))
    while not found and mul*combineddifflist[0]<product:
        #print(mul)
        """
        if mul&0:
            for add in evenlist:
                diff= combineddifflist[0]*mul+add
                halfdiff=diff/2
                candidate =(halfdiff**2+product)**.5
                if candidate == math.trunc(candidate):
                    if (candidate+halfdiff)*(candidate-halfdiff)==product:
                        print('factors:',candidate+halfdiff,candidate-halfdiff)
                        found=True
                        break
        else:
            for add in oddlist:
                diff= combineddifflist[0]*mul+add
                halfdiff=diff/2
                candidate =(halfdiff**2+product)**.5
                #print(diff,halfdiff,candidate)
                if candidate == math.trunc(candidate):
                    if (candidate+halfdiff)*(candidate-halfdiff)==product:
                        print('factors:',candidate+halfdiff,candidate-halfdiff,'p',p,'q',q,'mul',mul,'multiplier',combineddifflist[0],'nummuls',len(combineddifflist[1])/2)
                        found=True
                        break
                        
        """                
        if mul&0:
            for add in evenlist:
                diff= combineddifflist[0]*mul+add
                halfdiff=diff/2
                dechalfdiff=Decimal(halfdiff)
                decproduct=Decimal(product)
                deccandidate=Decimal()
                deccandidate =(dechalfdiff**2+decproduct)**Decimal('.5')
                if deccandidate == math.trunc(deccandidate):
                    if (deccandidate+dechalfdiff)*(deccandidate-dechalfdiff)==decproduct:
                        print('factors:',deccandidate+dechalfdiff,deccandidate-dechalfdiff,'p',p,'q',q,'mul',mul,'multiplier',combineddifflist[0],'nummuls',len(combineddifflist[1])/2)
                        found=True
                        break
        else:
            for add in oddlist:
                diff= combineddifflist[0]*mul+add
                halfdiff=diff/2
                dechalfdiff = Decimal(halfdiff)
                decproduct=Decimal(product)
                deccandidate=Decimal()
                deccandidate =(dechalfdiff**2+decproduct)**Decimal('.5')
                #print(diff,halfdiff,candidate)
                if deccandidate == math.trunc(deccandidate):
                    if (deccandidate+dechalfdiff)*(deccandidate-dechalfdiff)==decproduct:
                        print('factors:',deccandidate+dechalfdiff,deccandidate-dechalfdiff,'p',p,'q',q,'mul',mul,'multiplier',combineddifflist[0],'nummuls',len(combineddifflist[1])/2)
                        found=True
                        break
                        
                        
                        
                        
                        
                        
                        
        if found:
            break
        mul+=1
                
            

"""    
    print(combineddifflist)
"""



"""
    multiplier=0
    while(klist[1][listofkprimes][multiplier]*start<rootdthird):
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
"""
"""
if __name__ == "__main__":
    product=533149*1005019
    print(product,product**.5,product**.5/3**.5)
    print(product%6,4049%6,6091%6,product%10,4049%10,6091%10,4049%60,6091%60)
    klist=primedisjointproduct(product)
    #print(factors(product%klist[0]['primeproduct'],klist[0]['primeproduct'],klist[0]['listofkprimes']))
    #print(factors(product%klist[1]['primeproduct'],klist[1]['primeproduct'],klist[1]['listofkprimes']))
    klist[0]['factors']=factors(product%klist[0]['primeproduct'],klist[0]['primeproduct'],klist[0]['listofkprimes'])
    klist[1]['factors']=factors(product%klist[1]['primeproduct'],klist[1]['primeproduct'],klist[1]['listofkprimes'])
    #print(klist[0]['listofkprimes'])
    #print(klist[1]['listofkprimes'])
    #print(klist[0]['factors'])
    #print(klist[1]['factors'])
    #print(klist[0]['primeproduct'])
    #print(klist[1]['primeproduct'])
    #print(klist)
    factorfunctions1=dict()
    factorfunctions2=list()
    for factor1 in klist[0]['factors'][(klist[0]['primeproduct'],product%klist[0]['primeproduct'])]:
        #print(factor1)
        for factor2 in klist[1]['factors'][(klist[1]['primeproduct'],product%klist[1]['primeproduct'])]:
            #print(factor2)
            #print(factor1,factor2)
            #print(klist[0]['primeproduct'],factor1,klist[1]['primeproduct'],factor2)
            factorfunctions1[(factor1,factor2)]=(diophantine(klist[0]['primeproduct'],factor1,klist[1]['primeproduct'],factor2))    
            #print(factorfunctions1[(factor1,factor2)])
    count=0
    addlist=list()
    for factorfunction in factorfunctions1.keys():
        if factorfunctions1[factorfunction][0]==0:
            #print(klist[0]['primeproduct'],klist[1]['primeproduct'])
            #print(factorfunction)
            #print(factorfunctions1[factorfunction])
            #print(klist[0]['primeproduct'],'* x +',factorfunction[0],'=',klist[1]['primeproduct'],'* y +',factorfunction[1])
            #print(klist[0]['primeproduct'],'* (',klist[1]['primeproduct'],'* x +',factorfunctions1[factorfunction][1],') +',factorfunction[0],'=',
            #      klist[1]['primeproduct'],'* (',klist[0]['primeproduct'],'* y +',factorfunctions1[factorfunction][2],') +',factorfunction[1])
            addlist.append(klist[0]['primeproduct']*factorfunctions1[factorfunction][1]+factorfunction[0])
            #factorfunctions2.append((divisor1,divisor2,factorfunction[1],product%divisor1))
            #factorfunctions2.append((divisor2,divisor1,factorfunction[2],product%divisor2))
            count +=1
    #print(count)
    #print(product,product**.5,product**.5/3**.5,(product**.5-product**.5/3**.5)/(klist[0]['primeproduct']*klist[1]['primeproduct'])*count)
    print(sorted(addlist))
    print(len(addlist))
    

"""


"""

if __name__ == "__main__":
    product=144871
    divisor1=30
    divisor2=42
    factordict=factors(product%divisor1,divisor1,[2,3,5])
    trialdict=dict()
    for key in factordict.keys():
        trialdict[key]=factordict[key]
    factordict=factors(product%divisor2,divisor2,[2,3,5,7])
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
        for function in factorfunction.keys():
            if function[0]==0:
                print(factorfunction.key(),function)
            #print(factorfunctions1[factorfunctions])
            #factorfunctions2.append((divisor1,divisor2,factorfunction[1],product%divisor1))
            #factorfunctions2.append((divisor2,divisor1,factorfunction[2],product%divisor2))
    for factorfunction in factorfunctions1:
        pass
        #print(factorfunction)
        #print(factorfunction[0],'* (',factorfunction[1],'+',factorfunction[2],') +',factorfunction[3])
        #print(factorfunction[0]* factorfunction[1],'* x +',factorfunction[0]*factorfunction[2]+factorfunction[3])

"""
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