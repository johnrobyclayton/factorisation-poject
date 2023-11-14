import primefac

def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

def binarysplit(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]
#print(binarysplit(13))


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

def factormoddiff(p,m,f):
    toreturn=set()
    returnfilter=set()
    for i in range(1,p):
        for j in range(1,p):
            if (i*j)%p==m:
                toreturn.add((p-i+j)%p)
                toreturn.add((p-j+i)%p)
    for i in range(1,p):
        for j in range(1,p):
            if (i*j)%p==f:
                toreturn.add((p-i+j)%p)
                toreturn.add((p-j+i)%p)
    return toreturn.intersection(returnfilter)

def factormoddiff(divisor,modulus):
    #initialise dictionary to return
    toreturn=set()
    #print('factormoddiff',divisor,modulus)
    
    #The multiple of the divisor
    multiple=0
    candidate=divisor*multiple+modulus
    #print('divisor ',i,' modulus ',j)
    while (candidate<divisor**2):
        #candidate modulus product
        #candidate=divisor*multiple+modulus
        #get prime factorisation of candidate
        primelist=list(primefac.primefac(candidate))
        primelist.append(1)
        primelist.append(1)
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
        partitionvalue=2**lenlist
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
        candidate=divisor*multiple+modulus
    #print (toreturn)
    return toreturn

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x



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
    p=41
    q=39

    product=p*q
    primegenerator = primegen()
    
    maxaverage=product**.5*(3**.5+1/(3**.5))/2
    maxdiff=product**.5*(3**.5-1/(3**.5))/2
    binlen=len(binarysplit(int(maxdiff)))-2
    print('binlen',binlen)
    modprod=product%(2**binlen)
    print(modprod)
    print(list(primefac.primefac(modprod)))
    print(product-modprod)
    print(product%4)
    
    
