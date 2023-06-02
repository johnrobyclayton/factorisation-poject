import primefac
import math
import decimal
from decimal import *


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









 



def binarysplit(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def factormoddiff(divisor,modulus):
    #initialise dictionary to return
    toreturn=set()
    
    #The multiple of the divisor
    multiple=0
    #print('divisor ',i,' modulus ',j)
    while (divisor*multiple+modulus<divisor**2):
        #candidate modulus product
        candidate=divisor*multiple+modulus
        #get prime factorisation of candidate
        primelist=list(primefac.primefac(candidate))
        CandidatePasses=True
        if GCD(candidate,divisor)[0]!=1:
            CandidatePasses=False
        if CandidatePasses:
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
            
            if(partitionproduct<=divisor and candidate/partitionproduct<=divisor and CandidatePasses):
                #moddict[(i,j)].add((partitionproduct*candidate//partitionproduct,partitionproduct,candidate//partitionproduct))
                toreturn.add((divisor-partitionproduct+candidate//partitionproduct)%divisor)
                toreturn.add((divisor-candidate//partitionproduct+partitionproduct)%divisor)
        
        multiple+=1
    #print (toreturn)
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
            #print(a,b,c,d,diofresult,a*diofresult[1]+b)
            #print('difresult',diofresult)
            #print(firstdifflist[0]*diofresult[1]+firstdiff,
            #      seconddifflist[0]*diofresult[2]+seconddiff)
            #print(a*diofresult[1]+b,
            #      c*diofresult[2]+d)
            if(diofresult[0]==0):
                #print(firstdifflist[0],firstdiff,seconddifflist[0],seconddiff,diofresult)
                returndifflist.append(a*diofresult[1]+b)
    #print(returndifflist)
    
    return(returndifflistkey,sorted(returndifflist))
#(a,b,c,d)=(3,0,5,4)
#diofresult=diophantine(3,0,5,4)
#print(diofresult,a*diofresult[1]+b, c*diofresult[2]+d)
#main

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
    p=123456791
    q=233460431

    product=p*q
    print(product)
    root4d=(product**(1/4))//1
    compositegenerator = trianglefac()
'''
    compositeproduct=1
    primeindex=0
    while compositeproduct<root4d:
        composite=next(compositegenerator)#2
        primeindex+=1
    print(composite,primeindex)
    
    diffdict=dict()
    
    diffdict[(compositeproduct%composite)]=list(sorted(factormoddiff(composite,product%composite)))
    print(diffdict)

    """    
    while compositeproduct<root4d:
        
        #diffdict[composite]=difflist
        compositeproduct*=composite
        combineddifflist=combinedifflists(combineddifflist,diffdict)
        #moddict[prime]=[product%prime,p%prime,q%prime]
        #pqmoddiffdict[prime]=((((p-q)**2)**.5)//1)%prime
        print('diffdict',diffdict)
        primedifflist=list()    
        #composite=next(primegenerator)
    #print('moddict',moddict)    
    #print('pqmoddict',pqmoddiffdict)
    """ 
    
    """   
    for p in range (0,power):
        primedifflist.append(key)
    
    #print('primedifflist',primedifflist)
    difflistkey=primedifflist.pop()
    #print('popped1',difflistkey,primedifflist)
    
    combineddifflist=(difflistkey,diffdict[difflistkey])
    #print('combineddifflist1',combineddifflist)
    
    while primedifflist:
        difflistkey=primedifflist.pop()
        #print('popped2',difflistkey,primedifflist)
        nextdifflist=(difflistkey,diffdict[difflistkey])
        #print('nextdifflist',nextdifflist)
        #print('interim',combineddifflist,nextdifflist)
        combineddifflist=combinedifflists(combineddifflist,nextdifflist)
        #print('combineddifflist',combineddifflist)
    print('combineddifflist',combineddifflist[0])
    oddlist=list()
    evenlist=list()
    for element in sorted(combineddifflist[1]):
        if element%2==1:
            oddlist.append(element)
        else:
            evenlist.append(element)
    #print(evenlist)
    found=False
    
    mul=0
    #print('mul',mul,combineddifflist[0],mul*combineddifflist[0],product,q-p)
    #print('one',combineddifflist[0],combineddifflist[1])
    #print(sorted(oddlist))
    while not found and mul*combineddifflist[0]<product:
        #print(mul)
        if (mul%2)==0:
            #if mul==22:
            #    print(evenlist)
            for add in evenlist:
                diff= combineddifflist[0]*mul+add
                halfdiff=diff//2
                candidate =(halfdiff**2+product)**.5
                #if mul==22 and add==3307050:
                #    print('halfdiff',halfdiff,'candidate',candidate)
                #    print(Decimal(candidate+halfdiff),Decimal(candidate-halfdiff),Decimal(candidate+halfdiff)*Decimal(candidate-halfdiff))
                if candidate == math.trunc(candidate):
                    if Decimal(candidate+halfdiff)*Decimal(candidate-halfdiff)==Decimal(product):
                        print('factorsE:',candidate+halfdiff,candidate-halfdiff,'p',p,'q',q,'mul',mul,'multiplier',combineddifflist[0],'add',add,'nummuls',len(evenlist),len(oddlist),len(evenlist)/combineddifflist[0])
                        found=True
                        break
        else:
            for add in oddlist:
                diff= combineddifflist[0]*mul+add
                halfdiff=diff//2
                #if mul==22 and add==3307050:
                #    print('halfdiff',halfdiff)
                candidate =(halfdiff**2+product)**.5
                #print(diff,halfdiff,candidate)
                if candidate == math.trunc(candidate):
                    if Decimal(candidate+halfdiff)*Decimal(candidate-halfdiff)==Decimal(product):
                        print('factorsO:',candidate+halfdiff,candidate-halfdiff,'p',p,'q',q,'mul',mul,'multiplier',combineddifflist[0],'add',add,'nummuls',len(evenlist),len(oddlist),len(oddlist)/combineddifflist[0])
                        found=True
                        break
                        
        if found:
            break
        mul+=1
        #print('mul',mul,combineddifflist[0],mul*combineddifflist[0],product,q-p)
    """
'''
