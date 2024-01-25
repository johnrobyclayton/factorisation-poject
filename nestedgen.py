


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

def searchmins(moddiffdict):
    maxp=max(moddiffdict)
    prime=moddiffdict[maxp]['prime']
    primeprod=moddiffdict[maxp]['primeprod']
    diffs=moddiffdict[maxp]['diffs']
    primeprodmul=moddiffdict[maxp]['primeprodmul']
    primemul=moddiffdict[maxp]['primemul']
    
    if maxp!=2:
        moddiffdict.pop(maxp,None)
        previous=searchmins(moddiffdict)
        
        for pdiffs in previous:
            
            #print('localpdiffs init',localpdiffs)
            #print('prime',prime,'pdiffs',pdiffs,'diffs',diffs)
            for diff in diffs:
                localpdiffs=[]
                for pdiff in pdiffs:
                    localpdiffs.append(pdiff)
                localpdiffs.append(diff)
                #print('localpdiffs',localpdiffs)
                yield localpdiffs
    elif maxp==2:
        yield [0]

p=97
q=89
d=p*q

primeprod=1
primegenerator=primegen()
moddiffdict=dict()
while primeprod<(d**.5)+1.2:
    maxprime=max(moddiffdict,default=0)
    prime=next(primegenerator)
    moddiffdict[prime]=dict()
    moddiffdict[prime]['prime']=prime
    moddiffdict[prime]['primelist']=[]
    if maxprime!=0:
        for pr in moddiffdict[maxprime]['primelist']:
            moddiffdict[prime]['primelist'].append(pr)
    moddiffdict[prime]['primelist'].append(prime)
    moddiffdict[prime]['primeprod']=primeprod
    moddiffdict[prime]['diffs']=moddiff(prime,d%prime)
    moddiffdict[prime]['primeprodmul']=MULINV(primeprod,prime)
    moddiffdict[prime]['primemul']=MULINV(prime,primeprod)
    #print(moddiffdict)
    primeprod*=prime
for x in moddiffdict.keys():
    print(moddiffdict[x])
moddiffgen=searchmins(moddiffdict)
print(next(moddiffgen))
more=True
while more:
    #print('next moddiffgen')
    try:
        print(next(moddiffgen))
    except StopIteration:
        more=False