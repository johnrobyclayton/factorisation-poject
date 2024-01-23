


def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1


def MULINV(a,b):
    gcd,x,y=GCD(a,b)
    if x<0:
        return x+b
    else:
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
        yield listofprimes[-1]



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


p=13
q=23
d=p*q

primeprod=1
primegenerator=primegen()
while primeprod<(d**.5)+1.2:
    prime=next(primegenerator)
    print('prime mul',MULINV(prime,primeprod))
    print('primeprod mul',MULINV(primeprod,prime))
    print('primeprod',primeprod,'prime',prime)
    primeprod*=prime
    print(moddiff(prime,d%prime))