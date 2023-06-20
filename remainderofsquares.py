

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

def binarysplit(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

def generateModDict(topprime,product):
    primegenerator=primegen()
    firstprime=next(primegenerator)
    primedict=dict()
    
    primeproduct=1
    for prime in range(1,topprime+1):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        primedict[prime]['mod']=product%primedict[prime]['prime']
        primeproduct*=primedict[prime]['prime']
        primedict[prime]['primeproduct']=primeproduct
        if prime==1:
            primedict[prime]['previousprime']=1
            primedict[prime]['previousprimeproduct']=1
        else:
            primedict[prime]['previousprime']=primedict[prime-1]['prime']
            primedict[prime]['previousprimeproduct']=primedict[prime-1]['primeproduct']
    difflistdict=dict()
    difflistdict['eo']=dict()
    difflistdict['oe']=dict()
    for i in range(1,primeproduct*2):
        if i%2==0:
            difflistdict['oe'][i]=dict()
            difflistdict['oe'][i]['index']=i
        elif i%2==1:
            difflistdict['eo'][i]=dict()
            difflistdict['eo'][i]['index']=i
    
    #initialise the list of squares of the mods that are themselves modded
    #only the first half are needed as they will be reflected in the second half
    #add square mods to the difflistdict and aveset
    for diff in difflistdict['eo'].keys():
        difflistdict['eo'][diff]['squaremod']=(diff**2)%primeproduct
    for diff in difflistdict['oe'].keys():
        difflistdict['oe'][diff]['squaremod']=(diff**2)%primeproduct
    avesetdict=dict()
    avesetdict['eo']=set()
    avesetdict['oe']=set()
    for i in range(1,primeproduct*2+1,2):
        avesetdict['eo'].add((i**2)%primeproduct)
    for i in range(2,primeproduct*2+1,2):
        avesetdict['oe'].add((i**2)%primeproduct)
    for i in difflistdict['eo'].keys():
        difflistdict['eo'][i]['modset']=set()
        for j in avesetdict['eo']:
            difflistdict['eo'][i]['modset'].add((j-difflistdict['eo'][i]['squaremod']+primeproduct)%primeproduct)
    for i in difflistdict['oe'].keys():
        difflistdict['oe'][i]['modset']=set()
        for j in avesetdict['oe']:
            difflistdict['oe'][i]['modset'].add((j-difflistdict['oe'][i]['squaremod']+primeproduct)%primeproduct)
    moddict=dict()
    moddict['oe']=dict()
    moddict['eo']=dict()
    for i in range(1,primeproduct):
        moddict['oe'][i]=dict()
        moddict['oe'][i]['index']=set()
        for j in difflistdict['oe'].keys():
            if i in difflistdict['oe'][j]['modset']:
                moddict['oe'][i]['index'].add(difflistdict['oe'][j]['index'])
        moddict['eo'][i]=dict()
        moddict['eo'][i]['index']=set()
        for j in difflistdict['eo'].keys():
            if i in difflistdict['eo'][j]['modset']:
                moddict['eo'][i]['index'].add(difflistdict['eo'][j]['index'])
    #print('moddict-eo-53',sorted(moddict['eo'][53]['index']))
    if product%4==3:
        return (primeproduct*2,sorted(moddict['eo'][product%primeproduct]['index']))
    elif product%4==1:
        return (primeproduct*2,sorted(moddict['oe'][product%primeproduct]['index']))
    else:
        return (0,list())

def generateModDict2(topprime,product):
    primegenerator=primegen()
    firstprime=next(primegenerator)
    primedict=dict()
    
    primeproduct=1
    for prime in range(1,topprime+1):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        #primedict[prime]['mod']=product%primedict[prime]['prime']
        primeproduct*=primedict[prime]['prime']
        primedict[prime]['primeproduct']=primeproduct
        if prime==1:
            primedict[prime]['previousprime']=1
            primedict[prime]['previousprimeproduct']=1
        else:
            primedict[prime]['previousprime']=primedict[prime-1]['prime']
            primedict[prime]['previousprimeproduct']=primedict[prime-1]['primeproduct']
    difflistdict=dict()
    difflistdict['eo']=dict()
    difflistdict['oe']=dict()
    for i in range(1,primeproduct*2):
        if i%2==0:
            difflistdict['oe'][i]=dict()
            #difflistdict['oe'][i]['index']=i
        elif i%2==1:
            difflistdict['eo'][i]=dict()
            #difflistdict['eo'][i]['index']=i
    
    #initialise the list of squares of the mods that are themselves modded
    #only the first half are needed as they will be reflected in the second half
    #add square mods to the difflistdict and aveset
    for diff in difflistdict['eo'].keys():
        difflistdict['eo'][diff]['squaremod']=(diff**2)%primeproduct
    for diff in difflistdict['oe'].keys():
        difflistdict['oe'][diff]['squaremod']=(diff**2)%primeproduct
    diffsetdict=dict()
    diffsetdict['eo']=set()
    diffsetdict['oe']=set()
    avesetdict=dict()
    avesetdict['eo']=set()
    avesetdict['oe']=set()
    for i in range(1,primeproduct*2+1,2):
        avesetdict['eo'].add((i**2)%primeproduct)
        diffsetdict['oe']=avesetdict['eo']
    for i in range(2,primeproduct*2+1,2):
        avesetdict['oe'].add((i**2)%primeproduct)
        diffsetdict['eo']=avesetdict['oe']
    modsquarediffdict=dict()
    modsquarediffdict['oe']=dict()
    modsquarediffdict['eo']=dict()
    for diff in diffsetdict['oe']:
        modsquarediffdict['oe'][diff]=set()
        for ave in avesetdict['oe']:
            modsquarediffdict['oe'][diff].add((ave-diff+primeproduct)%primeproduct)
    for diff in diffsetdict['eo']:
        modsquarediffdict['eo'][diff]=set()
        for ave in avesetdict['eo']:
            modsquarediffdict['eo'][diff].add((ave-diff+primeproduct)%primeproduct)
    #print(modsquarediffdict['oe'])
    #print(modsquarediffdict['eo'])
    #print(difflistdict['eo'].keys())        
    for i in difflistdict['eo'].keys():
        difflistdict['eo'][i]['modset']=set()
        difflistdict['eo'][i]['modset']=modsquarediffdict['eo'][(i**2)%primeproduct]
    for i in difflistdict['oe'].keys():
        difflistdict['oe'][i]['modset']=set()
        difflistdict['oe'][i]['modset']=modsquarediffdict['oe'][(i**2)%primeproduct]
    moddict=dict()
    moddict['oe']=dict()
    moddict['eo']=dict()
    for i in range(1,primeproduct):
        moddict['oe'][i]=dict()
        moddict['oe'][i]['index']=set()
        for j in difflistdict['oe'].keys():
            if i in difflistdict['oe'][j]['modset']:
                moddict['oe'][i]['index'].add(j)
        moddict['eo'][i]=dict()
        moddict['eo'][i]['index']=set()
        for j in difflistdict['eo'].keys():
            if i in difflistdict['eo'][j]['modset']:
                moddict['eo'][i]['index'].add(j)
    #print('moddict-eo-53',sorted(moddict['eo'][53]['index']))
    if product%4==3:
        return (primeproduct*2,sorted(moddict['eo'][product%primeproduct]['index']))
    elif product%4==1:
        return (primeproduct*2,sorted(moddict['oe'][product%primeproduct]['index']))
    else:
        return (0,list())

def generateModDict3(topprime,product):
    primegenerator=primegen()
    firstprime=next(primegenerator)
    primedict=dict()
    primeproduct=1
    for prime in range(1,topprime+1):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        primeproduct*=primedict[prime]['prime']
        primedict[prime]['primeproduct']=primeproduct
        if prime==1:
            primedict[prime]['previousprime']=1
            primedict[prime]['previousprimeproduct']=1
        else:
            primedict[prime]['previousprime']=primedict[prime-1]['prime']
            primedict[prime]['previousprimeproduct']=primedict[prime-1]['primeproduct']
    difflistdict=dict()
    difflistdict['eo']=dict()
    difflistdict['oe']=dict()
    for i in range(1,primeproduct*2):
        if i%2==0:
            difflistdict['oe'][i]=dict()
        elif i%2==1:
            difflistdict['eo'][i]=dict()
    for diff in difflistdict['eo'].keys():
        difflistdict['eo'][diff]['squaremod']=(diff**2)%primeproduct
    for diff in difflistdict['oe'].keys():
        difflistdict['oe'][diff]['squaremod']=(diff**2)%primeproduct
    avediffset=set()
    for i in range(1,primeproduct*2+1,2):
        avediffset.add((i**2)%primeproduct)
    modsquarediffdict=dict()
    for diff in avediffset:
        modsquarediffdict[diff]=set()
        for ave in avediffset:
            modsquarediffdict[diff].add((ave-diff+primeproduct)%primeproduct)
    for i in difflistdict['eo'].keys():
        difflistdict['eo'][i]['modset']=set()
        difflistdict['eo'][i]['modset']=modsquarediffdict[difflistdict['eo'][i]['squaremod']]
    for i in difflistdict['oe'].keys():
        difflistdict['oe'][i]['modset']=set()
        difflistdict['oe'][i]['modset']=modsquarediffdict[difflistdict['oe'][i]['squaremod']]
    moddict=dict()
    moddict['oe']=dict()
    moddict['eo']=dict()
    for i in range(1,primeproduct):
        moddict['oe'][i]=dict()
        moddict['oe'][i]['index']=set()
        for j in difflistdict['oe'].keys():
            if i in difflistdict['oe'][j]['modset']:
                moddict['oe'][i]['index'].add(j)
        moddict['eo'][i]=dict()
        moddict['eo'][i]['index']=set()
        for j in difflistdict['eo'].keys():
            if i in difflistdict['eo'][j]['modset']:
                moddict['eo'][i]['index'].add(j)
    if product%4==3:
        return (primeproduct*2,sorted(moddict['eo'][product%primeproduct]['index']))
    elif product%4==1:
        return (primeproduct*2,sorted(moddict['oe'][product%primeproduct]['index']))
    else:
        return (0,list())





def generateModDictExport(topprime):
    primegenerator=primegen()
    firstprime=next(primegenerator)
    primedict=dict()
    primeproduct=1
    for prime in range(1,topprime+1):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        primeproduct*=primedict[prime]['prime']
        primedict[prime]['primeproduct']=primeproduct
        if prime==1:
            primedict[prime]['previousprime']=1
            primedict[prime]['previousprimeproduct']=1
        else:
            primedict[prime]['previousprime']=primedict[prime-1]['prime']
            primedict[prime]['previousprimeproduct']=primedict[prime-1]['primeproduct']
    difflistdict=dict()
    difflistdict['eo']=dict()
    difflistdict['oe']=dict()
    for i in range(1,primeproduct*2):
        if i%2==0:
            difflistdict['oe'][i]=dict()
        elif i%2==1:
            difflistdict['eo'][i]=dict()
    for diff in difflistdict['eo'].keys():
        difflistdict['eo'][diff]['squaremod']=(diff**2)%primeproduct
    for diff in difflistdict['oe'].keys():
        difflistdict['oe'][diff]['squaremod']=(diff**2)%primeproduct
    avediffset=set()
    for i in range(1,primeproduct*2+1,2):
        avediffset.add((i**2)%primeproduct)
    modsquarediffdict=dict()
    for diff in avediffset:
        modsquarediffdict[diff]=set()
        for ave in avediffset:
            modsquarediffdict[diff].add((ave-diff+primeproduct)%primeproduct)
    for i in difflistdict['eo'].keys():
        difflistdict['eo'][i]['modset']=set()
        difflistdict['eo'][i]['modset']=modsquarediffdict[difflistdict['eo'][i]['squaremod']]
    for i in difflistdict['oe'].keys():
        difflistdict['oe'][i]['modset']=set()
        difflistdict['oe'][i]['modset']=modsquarediffdict[difflistdict['oe'][i]['squaremod']]
    moddict=dict()
    moddict['oe']=dict()
    moddict['eo']=dict()
    for i in range(1,primeproduct):
        moddict['oe'][i]=dict()
        moddict['oe'][i]['index']=set()
        for j in difflistdict['oe'].keys():
            if i in difflistdict['oe'][j]['modset']:
                moddict['oe'][i]['index'].add(j)
        moddict['eo'][i]=dict()
        moddict['eo'][i]['index']=set()
        for j in difflistdict['eo'].keys():
            if i in difflistdict['eo'][j]['modset']:
                moddict['eo'][i]['index'].add(j)
    return moddict


def generateModDictExport2(topprime):
    primegenerator=primegen()
    firstprime=next(primegenerator)
    primedict=dict()
    primeproduct=1
    for prime in range(1,topprime+1):
        primedict[prime]=dict()
        primedict[prime]['prime']=next(primegenerator)
        primeproduct*=primedict[prime]['prime']
        primedict[prime]['primeproduct']=primeproduct
        if prime==1:
            primedict[prime]['previousprime']=1
            primedict[prime]['previousprimeproduct']=1
        else:
            primedict[prime]['previousprime']=primedict[prime-1]['prime']
            primedict[prime]['previousprimeproduct']=primedict[prime-1]['primeproduct']
    difflistdict=dict()
    difflistdict['eo']=dict()
    difflistdict['oe']=dict()
    for i in range(1,primeproduct*2):
        if i%2==0:
            difflistdict['oe'][i]=dict()
        elif i%2==1:
            difflistdict['eo'][i]=dict()
    for diff in difflistdict['eo'].keys():
        difflistdict['eo'][diff]['squaremod']=(diff**2)%primeproduct
    for diff in difflistdict['oe'].keys():
        difflistdict['oe'][diff]['squaremod']=(diff**2)%primeproduct
    avediffset=set()
    for i in range(1,primeproduct*2+1,2):
        avediffset.add((i**2)%primeproduct)
    modsquarediffdict=dict()
    for diff in avediffset:
        modsquarediffdict[diff]=set()
        for ave in avediffset:
            modsquarediffdict[diff].add((ave-diff+primeproduct)%primeproduct)
    for i in difflistdict['eo'].keys():
        difflistdict['eo'][i]['modset']=set()
        difflistdict['eo'][i]['modset']=modsquarediffdict[difflistdict['eo'][i]['squaremod']]
    for i in difflistdict['oe'].keys():
        difflistdict['oe'][i]['modset']=set()
        difflistdict['oe'][i]['modset']=modsquarediffdict[difflistdict['oe'][i]['squaremod']]
    moddict=dict()
    moddict['oe']=dict()
    moddict['eo']=dict()
    moddict['primeproduct']=primeproduct
    moddict['cycle']=primeproduct*2
    for i in range(1,primeproduct):
        if GCD(i,primeproduct)[0]==1:
            moddict['oe'][i]=set()
            for j in difflistdict['oe'].keys():
                if i in difflistdict['oe'][j]['modset']:
                    moddict['oe'][i].add(j)
            moddict['eo'][i]=set()
            for j in difflistdict['eo'].keys():
                if i in difflistdict['eo'][j]['modset']:
                    moddict['eo'][i].add(j)
    return moddict



if __name__ == "__main__":
    print(generateModDictExport2(2))
    parentdir='.'
    combinedlistfolder='combinedlistfolder'
    primelistfile='primedict.txt'
    primelistfilepath=os.path.join(parentdir,primelistfile)
    combinedlistpath=os.path.join(parentdir,combinedlistfolder)
    #print(combinedifflists((6,modfactordiff(6,5)),(17,modfactordiff(17,5))))
    if not os.path.exists(primelistfilepath):
        primegenerator=primegen()
        prime=next(primegenerator)
        #prime*=next(primegenerator)
        primelistdict=dict()
        primelistdict[prime]=dict()
        primelistdict[prime]['primelist']=[prime]
        primelistdict[prime]['modlist']=dict()
    """
    '''
    difflistdict=dict()
    for i in squaremodlist:
        difflist.append(i)
    skipfirst=True
    for i in reversed(squaremodlist):
        if skipfirst:
            skipfirst=False
            continue
        difflist.append(i)
            
    squaremoddict=dict()
    for i in difflist:
        squaremoddict[i]
    for i in difflist:
        squaremoddict[i]=set()
        for j in range(1,primeproduct):
            squaremoddict[i].add(((j**2)%primeproduct-(i**2)%primeproduct+15)%15)
    moddict=dict()
    for i in range(0,15):
        moddict[i]=set()
        for key in squaremoddict.keys():
            if i in squaremoddict[key]:
                moddict[i].add(key)
    print(squaremoddict)
    print(moddict)
    '''