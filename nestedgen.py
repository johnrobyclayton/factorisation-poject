import math
import time

#integer square root
def isqrt(n):
    x = n
    #y = (x + 1) // 2
    y = (x + 1) >> 1
    while y < x:
        x = y
        #y = (x + n // x) // 2
        y = (x + n // x) >> 1
    return x



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
    #print(prime,mod)
    if mod==0:
        #print('mod is zero, moddiff of a factor impossible')
        return([])
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
    #print('diff to return',prime,toreturn)
    return toreturn

def moddiff2(divisor,mod):
    #print(prime,mod)
    if mod==0:
        #print('mod is zero, moddiff of a factor impossible')
        return([])
    toreturn=[]
    difflist=[range(0,divisor)]
    for aves in range(0,divisor*2):
        for diffs in range(0,divisor*2):
            if aves%2!=diffs%2:
                if (aves**2-diffs**2)%divisor==mod:
                    if diffs not in toreturn:
                        toreturn.append(diffs)
    return toreturn        

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

def searchmins(moddiffdict):
    maxp=0
    prime=0
    #print('In a deeper search')
    #for x in moddiffdict.keys():
    #    print(moddiffdict[x])
    maxp=max(moddiffdict)
    prime=moddiffdict[maxp]['prime']
    primeprod=moddiffdict[maxp]['primeprod']
    diffs=moddiffdict[maxp]['diffs']
    primeprodmul=moddiffdict[maxp]['primeprodmul']
    primemul=moddiffdict[maxp]['primemul']
    diffmul=moddiffdict[maxp]['diffmullist']
    maxdiff=moddiffdict[maxp]['maxdiff']
    #print('insearch maxp',maxp,'prime',prime,'primeprod',primeprod)
    #print('insearch moddiffdict',moddiffdict)
    if maxp>2:
        #print('pop moddiffdict',moddiffdict,'maxp',maxp,'prime',prime)
        moddiffdict.pop(maxp,None)
        #print('pop moddiffdict',moddiffdict,'maxp',maxp,'prime',prime)
        #print('Going into a deeper search')
        previous=searchmins(moddiffdict)
        #print('leaving a deeper search')
        #print('prime1',prime)
        for pdiffs in previous:
            yields=dict()
            #print('localpdiffs init',localpdiffs)
            #print('prime',prime,'pdiffs',pdiffs,'diffs',diffs)
            #print('prime',prime,'diffs',diffs)
            for diff in diffs:#for each moddiff in the current prime
                localpdiffs=[]#list to contain the current combination of differences from smaller primes and the selected diff from this prime
                for pdiff in pdiffs:#for the string of diffs from each of the previous primes
                    localpdiffs.append(pdiff)#append to the local list of diffs
                localpdiffs.append(diff)#append the current diff for the current prime
                #print('localpdiffs',localpdiffs,'mulllist',diffmul)
                total=0#initialise the total
                iprimeprod=primeprod*prime
                #print('iprimeprod',iprimeprod)
                for diff,muldiff in zip(localpdiffs,diffmul):#
                    if type(diff)==tuple: 
                        diff=0
                    #print(type(diff),diff,type(muldiff),muldiff,type(primeprod),primeprod,type(prime),prime)
                    total=total+(diff*muldiff)%(iprimeprod)
                    #print('totalacc',total)
                total=total%(primeprod*prime)
                #print('total',total)
                #print('totalbefore yield',total)
                if total <maxdiff:
                    #print('totalbefore yield',total)
                    yields[total]=localpdiffs
                    #print(max(yields,default=False))
                #    print('yields1',yields)
                    #for x in yields:
                    #    print('yield block',x,yields[x],max(yields,default=False))
                    moretoyield=True
                    try:
                        toyield=yields[max(yields)]
                    except (ValueError, StopIteration):
                        moretoyield=False
                    while moretoyield:
                        #print('maxyields',(yields[max(yields)]))
                        #print('toyield',toyield)
                        yield toyield
                        #print('reducing',yields)
                        del yields[max(yields)]
                        try:
                            toyield=yields[max(yields)]
                        except (ValueError, StopIteration):
                            moretoyield=False
    elif maxp==2:
        #print('prime',prime,'diffs',diffs)
        #print('we got to 2')
        #print('prime2',prime)
        toyield=list()
        toyield.append(0)
        #print('toyield',toyield)
        yield toyield


def searchminsfloat(moddiffdict):
    maxp=0
    prime=0
    #print('In a deeper search')
    #for x in moddiffdict.keys():
    #    print(moddiffdict[x])
    maxp=max(moddiffdict)
    prime=moddiffdict[maxp]['prime']
    primeprod=moddiffdict[maxp]['primeprod']
    diffs=moddiffdict[maxp]['diffs']
    primeprodmul=moddiffdict[maxp]['primeprodmul']
    primemul=moddiffdict[maxp]['primemul']
    diffmul=moddiffdict[maxp]['diffmullist']
    maxdiff=float(moddiffdict[maxp]['maxdiff'])
    #print('insearch maxp',maxp,'prime',prime,'primeprod',primeprod)
    #print('insearch moddiffdict',moddiffdict)
    if maxp>2:
        #print('pop moddiffdict',moddiffdict,'maxp',maxp,'prime',prime)
        moddiffdict.pop(maxp,None)
        #print('pop moddiffdict',moddiffdict,'maxp',maxp,'prime',prime)
        #print('Going into a deeper search')
        previous=searchminsfloat(moddiffdict)
        #print('leaving a deeper search')
        #print('prime1',prime)
        for pdiffs in previous:
            yields=dict()
            #print('localpdiffs init',localpdiffs)
            #print('prime',prime,'pdiffs',pdiffs,'diffs',diffs)
            #print('prime',prime,'diffs',diffs)
            for diff in diffs:#for each moddiff in the current prime
                localpdiffs=[]#list to contain the current combination of differences from smaller primes and the selected diff from this prime
                for pdiff in pdiffs:#for the string of diffs from each of the previous primes
                    localpdiffs.append(pdiff)#append to the local list of diffs
                localpdiffs.append(diff)#append the current diff for the current prime
                #print('localpdiffs',localpdiffs,'mulllist',diffmul)
                total=0.0#initialise the total
                floatprimeprod=float(primeprod)*float(prime)
                #print('floatprimeprod',floatprimeprod)
                for diff,mulldiff in zip(localpdiffs,diffmul):#
                    if type(diff)==tuple: 
                        diff=0.0
                    diff=float(diff)
                    mulldiff=float(mulldiff)
                    #print(type(diff),diff,type(muldiff),muldiff,type(primeprod),primeprod,type(prime),prime)
                    total=total+math.fmod((diff*mulldiff),floatprimeprod)
                    #print('totalacc',total)
                total=math.fmod(total,floatprimeprod)
                #print('total',total)
                #print('totalbefore yield',total)
                if total <maxdiff:
                    #print('totalbefore yield',total)
                    yields[int(total)]=localpdiffs
                    #print(max(yields,default=False))
                    #print('yields1',yields)
                    #for x in yields:
                    #    print('yield block',x,yields[x],max(yields,default=False))
                    moretoyield=True
                    try:
                        toyield=yields[max(yields)]
                    except (ValueError, StopIteration):
                        moretoyield=False
                    while moretoyield:
                        #print('maxyields',(yields[max(yields)]))
                        #print('toyield',toyield)
                        yield toyield
                        #print('reducing',yields)
                        del yields[max(yields)]
                        try:
                            toyield=yields[max(yields)]
                        except (ValueError, StopIteration):
                            moretoyield=False
    elif maxp==2:
        #print('prime',prime,'diffs',diffs)
        #print('we got to 2')
        #print('prime2',prime)
        toyield=list()
        toyield.append(0)
        #print('toyield',toyield)
        yield toyield



def testdiff(d,diff):
    difference=diff//2
    average=isqrt(d+difference**2)
    return d==((average-difference)*(average+difference))


def makemoddiffdict(d):
    maxdiff=(d**.5)*1.2
    primeprod=1
    difflenprod=1
    primegenerator=primegen()
    moddiffdict=dict()
    prime=0
    while primeprod<(d**1.2):
    #while (primeprod/difflenprod)*100<(((d**.5)*1.2)):
        #print((primeprod/difflenprod)*100,((d**.5)*1.2))
        maxprime=max(moddiffdict,default=0)
        prime=next(primegenerator)
        moddiffdict[prime]=dict()
        moddiffdict[prime]['maxdiff']=maxdiff
        moddiffdict[prime]['prime']=prime
        moddiffdict[prime]['previousprime']=maxprime
        moddiffdict[prime]['primelist']=[]
        if maxprime!=0:
            for pr in moddiffdict[maxprime]['primelist']:
                moddiffdict[prime]['primelist'].append(pr)
        moddiffdict[prime]['primelist'].append(prime)
        moddiffdict[prime]['primeprod']=primeprod
        moddiffdict[prime]['difflenprod']=difflenprod
        moddiffdict[prime]['diffmullist']=[]
        for pr in moddiffdict[prime]['primelist']:
            base =int(moddiffdict[prime]['primeprod']*prime//pr)
            baseacc=base
            #print('maxprime',maxprime,'prime',pr,'base',base,'primeprod',moddiffdict[prime]['primeprod']*prime,'baseacc',baseacc)
            mul=1
            #print('prime',prime,'primeprod',primeprod,'base',moddiffdict[prime]['primeprod']//pr,'pr',pr,'base_i',base%pr!=1)
            while baseacc%pr!= 1:
                #print('2base',base,'pr',pr,'base_i',base%pr!=1)
                baseacc+=base
                mul+=1
                #print('prime',pr,'base',base,'primeprod',moddiffdict[prime]['primeprod']*prime,'baseacc',baseacc)
            moddiffdict[prime]['diffmullist'].append(baseacc)
                
        moddiffdict[prime]['diffs']=moddiff(prime,d%prime)
        moddiffdict[prime]['difflen']=len(moddiffdict[prime]['diffs'])
        moddiffdict[prime]['primeprodmul']=MULINV(primeprod,prime)
        moddiffdict[prime]['primemul']=MULINV(prime,primeprod)
        moddiffdict[prime]['avestep']= moddiffdict[prime]['primeprod']/moddiffdict[prime]['difflenprod']
        #print(moddiffdict)
        primeprod*=prime
        difflenprod*=moddiffdict[prime]['difflen']
    return moddiffdict    
starttime=time.perf_counter()
p=3202260623
q=6202260899


p=48264029161
q=88264029043
p=106289749
q=206289299

d=p*q
moddiffdict=makemoddiffdict(d)
for x in moddiffdict.keys():
    print(moddiffdict[x])
maxprime= max(moddiffdict)
maxmoddiffdict=moddiffdict[maxprime]
maxprimeprod=moddiffdict[maxprime]['primeprod']*maxprime
maxdiffmul=maxmoddiffdict['diffmullist']
#print('maxprime',maxprime,'maxprimeprod',maxprimeprod,'maxdiffmul',maxdiffmul)


moddiffgen=searchmins(moddiffdict)
#moddiffgen=searchminsfloat(moddiffdict)


more=True
found=False
tries=0
while more and not found:
    try:
        candidate=next(moddiffgen)
        #print('loop',candidate)
        #print('second',maxdiffmul)
        total=0
        for diff,muldiff in zip(candidate,maxdiffmul):
            if type(diff)==tuple:
                diff=0
            total=total+(diff*muldiff)%(maxprimeprod)
        total=total%(maxprimeprod)
        tries+=1
        #if (candidate[0]==0 and candidate[1]==1 and candidate[2]==0 and candidate[3]==4 and candidate[4]==8 and candidate[5]==11 and candidate[6]==13 and candidate[7]==18 and candidate[8]==14 and candidate[9]==4 and candidate[10]==9 and candidate[11]==31 and candidate[12]==16 and candidate[13]==1 and candidate[14]==11 and candidate[15]==9 and candidate[16]==54 and candidate[17]==51 ):
        
        #    print('candidate',candidate,'maxdiffmul',maxdiffmul,'maxprimeprod',maxprimeprod,'total',total)
        if testdiff(d,total):
            found=True
            print('woohoo',candidate,[x/maxprimeprod for x in maxdiffmul],total,p,q,d,'tries',tries)
    except StopIteration:
        more=False
endtime=time.perf_counter()
print(endtime-starttime)