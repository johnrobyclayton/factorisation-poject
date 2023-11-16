from datetime import datetime, timedelta


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
    

def diophantine(a,b,c,d):
    #solve ax+b=cy+d given a,b,c,d
    #a*x+b=c*x+d
    #A=a
    #B=-c
    #C=d-b
    #A*x+B*x=C
    #a*x+b=c*y+d
    #print(a,"* x +",b,"=",c,"* y +",d)
    A=a
    B=-c
    C=d-b


    '''
    #Solve: 3x + 6y = 9 
    #x
    a = 3
    #b
    b = -5
    #c
    c = 2
    '''
    #Step 1
    #print(A,B) 
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
        y = y1 * (C//gcd)
        while(x<0):
            x+=c
        while(x>c):
            x-=c    
        y = y1 * (C//gcd)
        while(y<0):
            y+=a
        while(y>a):
            y-=a
        #print("The values of x and y are: ", x, ",", y)
        #print(a,'*(',c,'* x +',x,")+",b,"=",c,"* (",a,"* y +",y,")+",d)
        return(0,x,y)
    else:
        return(-2,0,0)#print("Solution not possible") 

def diophantine_result(a,b,c,d):

    return(a*c,diophantine(a,b,c,d)[1]*a+b)
    





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

def fast_diophantine_result(a,b,c,d):
    (A,C)=diophantine_base(a,c)
    #print(A)
    #print(C)
    return(a*c,(A*d+C*b)%(a*c))


def generate_diagonalSequence2(p,q,maxval):
    #p and q are coprime
    #In a grid q wide and p high
    #nimber the cells starting from (p,q) (0,0) equals 0
    #Increase p and q by 1 each for the next cell which equals 1
    #continue increasing the cell value by 1 each time
    #continue until p is at p-1 and then p goes back to 0 
    #and then continue with p increasing with q 
    #and incrementing the value of the cell by 1 at each step
    #due to p and q being coprime this will continue until 
    #the entire grid is filled with numbers in sequence from0 to p*q-1
    #this function generates the values of the cell and q-p returned as a tuple
    #for each of the cells where p or q is 0.
    #do nolt bother claculating for leading figures greater than maxval
    
    if p==q:
        return [(0,0)]
    start=0
    diag=0
    diagp=diag
    diagq=diag
    next=0
    if next>0:
        diagp+=p
        diag=diagp
    elif next<0:
        diagq+=q
        diag=diagq
    elif next==0:
        diag=0
    returnlist=list()
    returnlist.append((start,diag))
    #print('p',p,'q',q)
    if p<q:
        next=p
    else:
        next=-q
    #print('p',p,'q',q,'next',next)
    while next!=0 and (diagp<maxval or diagq<maxval):
        start=next
        if next>0:
            diagp+=p
            diag=diagp
        elif next<0:
            diagq+=q
            diag=diagq
        returnlist.append((start,diag))
        if(p+start>q):
            next=start-q
        elif p+start<q:
            next=start+p
        elif p+start==q:
            next=0
    return returnlist
    

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

    diffset=set()
    pp=set(range(1,x))
    #print(pp)
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



    
def generate_coordinates(p,q):
    #for each co-ordinate calculate the sum and the difference
    #when calculating the diff diagonal value
    #the value from the q list is subtracted from the value of the p list
    coords=dict()
    
    for x in p[1]:
        for y in q[1]:
            coords[(x,y)]=dict()
            coords[(x,y)]['sum']=x+y
            coords[(x,y)]['diff']=y-x
    return coords

def sortfunc(e):
    return e['sum']

def split_coordinates(coords):
    split_coords=dict()
    returndict=dict()
    #diffset=set()
    #print(coords)
    for coord in coords.keys():
        coords[coord]['coord']=coord
        
        #diffset.add(coord['diff'])
        #print(coord,coords[coord])
        #print(coords[coord]['diff'])
        #print(split_coords.keys())
        if coords[coord]['diff'] in split_coords:
            split_coords[coords[coord]['diff']].append(coords[coord])
        else:
            split_coords[coords[coord]['diff']]=list()
            split_coords[coords[coord]['diff']].append(coords[coord])
        if coords[coord]['diff'] in returndict:
            returndict[coords[coord]['diff']].add(coord)
        else:
            returndict[coords[coord]['diff']]=set()
            returndict[coords[coord]['diff']].add(coord)

    return returndict
    

    





def generate_grid2(grid1, grid2, maxval):
    #starttime=datetime.now()
    diagseq=generate_diagonalSequence2(grid1[0],grid2[0],maxval)
    #endtime=datetime.now()
    #print('generate_diagonalsequnce',endtime-starttime)
    diagseqdict=dict()
    #convert ordered pairs into dict
    #starttime=datetime.now()
    for pair in diagseq:
        diagseqdict[pair[0]]=pair[1]
    #endtime=datetime.now()
    #print('digseq conversion',endtime-starttime)
    #split the coordinates of the cros prod of the two grids into groups with the same difference between the second value minus the first value 
    #starttime=datetime.now()
    splitcoords=split_coordinates(generate_coordinates(grid1,grid2))
    #endtime=datetime.now()
    #print('split coords',endtime-starttime)
    grid=dict()
    gridsize=grid1[0]*grid2[0]
    grid[gridsize]=set()
    #starttime=datetime.now()
    for diff in splitcoords.keys():
        for coord in splitcoords[diff]:
            if diff in diagseqdict:
                if diagseqdict[diff]+min(coord[0],coord[1])<maxval:
                    grid[gridsize].add(diagseqdict[diff]+min(coord[0],coord[1]))
    #endtime=datetime.now()
    #print('forfor',endtime-starttime)
    return (gridsize,tuple(sorted(grid[gridsize])))

def generate_grid3(grid1, grid2, maxval):
    grid=dict()
    gridsize=grid1[0]*grid2[0]
    grid[gridsize]=set()
    A1=grid1[0]*(diophantine(grid1[0],0,grid2[0],1))[1]
    A2=grid2[0]*(diophantine(grid1[0],1,grid2[0],0))[2]
    #print(grid1[1])
    #print(grid2[1])
    #print(A1,A2)
    for a1 in grid1[1]:
        for a2 in grid2[1]:
            candidate=(A1*a2+A2*a1)%gridsize
            #print('A1',A1,'A2',A2,'a1',a1,'a2',a2,'candidate',candidate,'grid1',7,'grid2',11)
            if candidate<maxval:
                grid[gridsize].add(candidate)
    return (gridsize,tuple(sorted(grid[gridsize])))

def moddiffdict(d):
    primegenerator=primegen()
    toreturn=list()
    primeproduct=1
    while not primeproduct>d:
        toreturn.append(dict())
        currentindex=len(toreturn)
        prime=next(primegenerator)
        toreturn[currentindex-1]["prime"]=prime
        toreturn[currentindex-1]["primeproduct"]=primeproduct
        toreturn[currentindex-1]["diffs"]=tuple(sorted(moddiff(prime,d%prime)[1],reverse=True))
        toreturn[currentindex-1]["diafbase"]=diophantine_base(primeproduct,prime)
        primeproduct*=prime
    return toreturn

def searchmoddiffdict(moddiffdict,primeindex):
    print('diff',moddiffdict[primeindex-1])
    ordereddiffs=list()
    if primeindex==1:
        moddiffdict[primeindex-1]["accumulated"]=moddiffdict[primeindex-1]["diffs"][0]
    else:
        for diff in moddiffdict[primeindex-1]['diffs']:
            if "accumulated" in moddiffdict[primeindex-2]:
                ordereddiffs.append((diff*moddiffdict[primeindex-1]['diafbase'][0]+moddiffdict[primeindex-2]['accumulated']*moddiffdict[primeindex-1]['diafbase'][1])%(moddiffdict[primeindex-1]['primeproduct']*moddiffdict[primeindex-1]['prime']))
        ordereddiffs=sorted(ordereddiffs,reverse=True)
    for biggestdiff in ordereddiffs:
        moddiffdict[primeindex-1]["accumulated"]=biggestdiff
        if primeindex<len(moddiffdict):
            searchmoddiffdict(moddiffdict,primeindex+1)
    #print(primeindex,len(moddiffdict))
    #if primeindex<len(moddiffdict):
        #searchmoddiffdict(moddiffdict,primeindex+1)



moddiffdict_299=moddiffdict(299)
print(moddiffdict_299)
searchmoddiffdict(moddiffdict_299,1)


