from datetime import datetime, timedelta

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


#prime number generator
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

#extended GCD
def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1
#multiplicative inverse
#(a*MULINV(a,b))%b equivalent to 1
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
    toreturn=list()
    primeproduct=1
    while not primeproduct>d:
        
        prime=next(primegenerator)
        toreturn.append(dict())
        currentindex=len(toreturn)-1
        toreturn[currentindex]["prime"]=prime
        toreturn[currentindex]["primeproduct"]=primeproduct
        toreturn[currentindex]["diffs"]=tuple(sorted(moddiff(prime,d%prime)[1],reverse=True))
        toreturn[currentindex]["diafbase"]=diophantine_base(primeproduct,prime)
        toreturn[currentindex]["accumulated"]=0
        toreturn[currentindex]["diff"]=0
        toreturn[currentindex]["maxp"]=0
        primeproduct*=prime
    return toreturn

def testdiff(d,diff):
    difference=diff//2
    average=isqrt(d+difference**2)
    return d==((average-difference)*(average+difference))


def searchmoddiffdict(moddiffdict,primeindex,d,maxdiff,found):
    #print('diff',moddiffdict[primeindex-1])
    mod4=d%4
    ordereddiffs=list()
    for diff in moddiffdict[primeindex-1]['diffs']:
        ordereddiffs.append(dict())
        ##ordereddiffs[len(ordereddiffs)-1]["diff"]=diff
        ordereddiffs[len(ordereddiffs)-1]["calcdiff"]=(diff*moddiffdict[primeindex-1]['diafbase'][0]+moddiffdict[primeindex-2]['accumulated']*moddiffdict[primeindex-1]['diafbase'][1])%(moddiffdict[primeindex-1]['primeproduct']*moddiffdict[primeindex-1]['prime'])
    ordereddiffs=sorted(ordereddiffs,key=lambda x: x["calcdiff"],reverse=True)
    
    for biggestdiff in ordereddiffs:
        ##moddiffdict[primeindex-1]["gcd"]=GCD(moddiffdict[primeindex-1]["accumulated"],moddiffdict[primeindex-1]["diff"])
        moddiffdict[primeindex-1]["accumulated"]=biggestdiff["calcdiff"]
        diffmod4=moddiffdict[primeindex-1]["accumulated"]%4
        ##moddiffdict[primeindex-1]["diff"]=biggestdiff["diff"]
        ##moddiffdict[primeindex-1]["mod4"]=moddiffdict[primeindex-1]["accumulated"]%16
        if moddiffdict[primeindex-1]["primeproduct"]>maxdiff and found==False:
            
            if moddiffdict[primeindex-1]["accumulated"]<maxdiff:
                ##if primeindex-1>=moddiffdict[0]['maxp']:
                    if moddiffdict[primeindex-1]["accumulated"]==moddiffdict[primeindex-2]["accumulated"]:
                        if mod4==3 and diffmod4==2 or mod4==1 and diffmod4==0:
                            #print(moddiffdict[primeindex-1]["accumulated"],maxdiff,primeindex-1)
                            #moddiffdict[0]['maxp']=primeindex-1
                            
                            ##if moddiffdict[primeindex-2]["accumulated"]!=0:
                                ##moddiffdict[primeindex-1]['acrate']=moddiffdict[primeindex-1]["accumulated"]/moddiffdict[primeindex-2]["accumulated"]
                            if testdiff(d,moddiffdict[primeindex-1]["accumulated"]):
                                difference=moddiffdict[primeindex-1]["accumulated"]//2
                                average=isqrt(d+difference**2)
                                print(d,average+difference,average-difference,primeindex-1,moddiffdict[0]['maxp'])
                                #for i in range(primeindex-1,0,-1):
                                    #print(moddiffdict[i])
                                found=True
                                break
                            #print(d%4,moddiffdict[primeindex-1]["accumulated"]%4)
        if (primeindex<len(moddiffdict) 
            and found==False 
            and moddiffdict[primeindex-1]["accumulated"]<maxdiff):
            #and moddiffdict[primeindex-1]["primeproduct"]*200<maxdiff):
            found=searchmoddiffdict(moddiffdict,primeindex+1,d,maxdiff,found)
    return found
    #print(primeindex,len(moddiffdict))
    #if primeindex<len(moddiffdict):
        #searchmoddiffdict(moddiffdict,primeindex+1)



#print(moddiffdict(209*103))
p=149
q=277
#time 0:00:00
p=1423
q=2801
#time 0:00:00
p=14107
q=27361
#time 0:00:00.002041
p=140053
q=270463
#time 0:00:00.012980
p=1400453
q=2700833
#time 0:00:00.153649
#p=14000801
#q=27001259
#time 0:00:00.004029
p=140000953
q=270001639
#time 0:00:03.058141
#p=1400000999
#q=2700001657
#time 0:00:34.640859
#p=14000002063
#q=27000002621
#time 0:00:49.965088
#p=140000001061
#q=270000001717
#time 0:14:06.851745
#p=140000002951
#q=270000003979
#time 0:00:58.449312
#p=40094690950920881030683735292761468389214899724061
#q=37975227936943673922808872755445627854565536638199
d=p*q
#d=d*863*863
#d=d*(isqrt(d)+isqrt(isqrt(d)))(isqrt(d)-isqrt(isqrt(d)))

maxdiff=int(isqrt(d)*3**.5-1/(3**.5))
starttime=datetime.now()
searchmoddiffdict(moddiffdict(d),1,d,maxdiff,False)
endtime=datetime.now()
print('time',endtime-starttime)

'''
primegenerator=primegen()
prime=next(primegenerator)
while prime<50:
    if d ** ((prime - 2) // 2) % prime != 1 or True:
        print(d ** ((prime - 2) // 2) % prime,moddiff(prime,d%prime))
    prime=next(primegenerator)
'''

