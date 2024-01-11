import numpy as np
import cupy as cp
import itertools

def isqrt(n):
    x = n
    #y = (x + 1) // 2
    y = (x + 1) >> 1
    while y < x:
        x = y
        #y = (x + n // x) // 2
        y = (x + n // x) >> 1
    return x

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

def moddiff(x,y):
#Let product (d) be the product of integers (p,q)
#let (x) be an integer coprime to (d)
#let  (y) be equivalent to d(mod x)
# (p(mod x)*q(mod x))(mod x) is equivalent to d(mod x)
#for any d(mod x), or (y) there are a number of pairs of integers less than (x)
#that when multiplied together and taken to (mod x) will be equialent to (y)
#Example:
#77(mod 3)=2
#(1*2)(mod 3)=2
#(2*1)(mod 3)=2
#possible scenarios are:
#p=3n+1
#q=3n+2
#or
#p=3n+1
#q=3n+2
#where p>q
#(p-q)(mod 3)=1 or 2
#therefore the possible differences between p and q are 3n+1 or 3n+2
#77(mod 5)=2
#(1*2)(mod 5)=2
#(2*1)(mod 5)=2
#(3*4)(mod 5)=2
#(4*3)(mod 5)=2
#(p-q)(mod 3)=1 or 4
#therefore the possible differences between p and q are 5n+1 or 5n+4
#moddiff provides the possible differences between p and q  to mod(divisor)
# for a given divisor and modulus 
    if y==0:
        print('mod is zero, moddiff of a factor impossible')
        return((1,(0,)))
    diffset=set()
    pp=set(range(1,x))
    while len(pp):
        found=False
        for i in pp:
            for j in pp:
                if (i*j)%x==y:
                    diffset.add((x+i-j)%x)
                    diffset.add((x-i+j)%x)
                    pp.discard(i)
                    pp.discard(j)
                    found=True
                if found:
                    break
            if found:
                break
    return((x,tuple(sorted(diffset))))

def moddiffdict(d):
    #print('moddiffdict')
    primegenerator=primegen()
    toreturn1=list()
    toreturn2=list()
    primeproduct=1
    while not primeproduct>((d**(1/3))**2):
        
        prime=next(primegenerator)
        toreturn1.append(prime)
        toreturn2.append(list(sorted(moddiff(prime,d%prime)[1],reverse=True)))
        primeproduct*=prime
    return (toreturn1,toreturn2)

def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


prime1=13
prime2=23
prime1=127
prime2=239
product=prime1*prime2
chunksize=10000
limit = int(isqrt(product)*1.2)
floatlimit=(product**.5)*1.2
#print('moddiff',list(moddiff(5,product%5)[1]))
mdifd=moddiffdict(product)
#print(mdifd)
#print(mdifd[1])

p_gpu=np.array(mdifd[0])
mul=list()
primeprod=int(np.prod(p_gpu))
for i in p_gpu:
    base =int(primeprod//i)
    print(type(base))
    while base%i!= 1:
        base+=base
    mul.append(base)
#print(mul)
floatmul=np.array(mul,dtype=float)
print('mul',mul)
print('floatmul',floatmul)
#print(mdifd[0])
#print(mdifd[1])
#print(np.shape(mdifd[1]))
p_lists=mdifd[1]
for chunk in chunked_iterable(itertools.product(*p_lists),10):
    block=np.array(chunk)
    floatblock=np.array(chunk,dtype=float)
    #print('block',block)
    #print('floatblock',floatblock)
    block*=mul
    floatblock*=floatmul
    #print('mul*block',block)
    #print('floatmul*floatblock',floatblock)
    block=np.sum(block,axis=1)
    floatblock=np.sum(floatblock,axis=1)
    #print('sumblock',block)
    #print('sumfloatblock',floatblock)
    block=np.mod(block,primeprod)
    floatblock=np.fmod(floatblock,primeprod)
    #print('modblock',block)
    #print('modfloatblock',floatblock)
    block=np.where(block<limit)
    floatblock=np.where(floatblock<floatlimit)
    print('where block',block)
    print('where floatblock',floatblock)
    print(block[0][0])
    print(floatblock[0][0])

    '''
    for i in block:
        d=i//2
        aves=d**2+product
        a=isqrt(aves)
    
        if ((a+d)*(a-d))==product:
            print('woohoo',a+d,a-d,product)
    '''