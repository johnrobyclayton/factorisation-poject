from datetime import datetime, timedelta


def generate_grid(x, y):
    grid=dict()
    for n in range(0,int(x[0]*y[0])):
        if n%x[0] in x[1] and n%y[0] in y[1]:
            grid[(n%x[0],n%y[0])]=n
    return((x[0]*y[0],sorted(set(grid.values()))))


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

def generate_diagonalSequence(p,q):
    #p is the smaller value
    #q is the larger value
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
    
    if p==q:
        return [(0,0)]
    start=0
    diag=0
    diagp=diag
    diagq=diag
    next=0
    nextd=p
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
    next=p
    while next!=0:
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

def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

#solve ax+b=cy+d given a,b,c,d

#a*x+b=c*x+d
#A=a
#B=-c
#C=d-b
#A*x+B*x=C
def diophantine(a,b,c,d):
  #a*x+b=c*y+d
  '''
  a=3
  b=1
  c=5
  d=2
  '''
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
    #print("The values of x and y are: ", x, ",", y)
    #print(a,'*(',c,'* x +',x,")+",b,"=",c,"* (",a,"* y +",y,")+",d)
    return(0,(a+x)%a,(c+y)%c)
  else:
    return(-2,0,0)#print("Solution not possible") 
    
def diophantine2():
    pass

def generate_diagonalSequence2(p,q,maxval):
    #p is the smaller value
    #q is the larger value
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
    
    
def generate_coordinates(p,q):
    #p is the smaller value and the list of diffs of the smaller value
    #q is the larger value and the list of diff of the larger value
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
    

    



def moddiff(x,y):
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


p=244451
q=634679
d=p*q
#d=299

#print('generate_grid',generate_grid((5,[1,4]),(7,[1,3,4,6])))
#print('generate_coordinates',generate_coordinates((5,[1,4]),(7,[1,3,4,6])))
#print('generate_diagonalsequence',generate_diagonalSequence(5,7))
#print('split_coordinates',split_coordinates(generate_coordinates((5,[1,4]),(7,[1,3,4,6]))))
#print('generate_grid2',generate_grid2((5,[1,4]),(7,[1,3,4,6])))
#print('generate_grid2',generate_grid2((7,[1,3,4,6]),(5,[1,4])))
'''
currenttime=datetime.now()
grid=generate_grid2(
    moddiff(2,d%2),
    moddiff(3,d%3)
)
endtime=datetime.now()
print(grid[0],len(grid[1],),len(grid[1])/grid[0],endtime-currenttime)
14924856
'''
'''
grid_2_53=generate_grid2(moddiff(2,d%2),moddiff(53,d%53),d**.5*((3**.5)-(1/(3**.5))))
print(grid_2_53)
grid_3_47=generate_grid2(moddiff(3,d%3),moddiff(47,d%47),d**.5*((3**.5)-(1/(3**.5))))
print(grid_3_47)
grid_5_43=generate_grid2(moddiff(5,d%5),moddiff(43,d%43),d**.5*((3**.5)-(1/(3**.5))))
print(grid_5_43)
grid_7_41=generate_grid2(moddiff(7,d%7),moddiff(41,d%41),d**.5*((3**.5)-(1/(3**.5))))
print(grid_7_41)
grid_11_37=generate_grid2(moddiff(11,d%11),moddiff(37,d%37),d**.5*((3**.5)-(1/(3**.5))))
print(grid_11_37)
grid_13_31=generate_grid2(moddiff(13,d%13),moddiff(31,d%31),d**.5*((3**.5)-(1/(3**.5))))
print(grid_13_31)
grid_17_29=generate_grid2(moddiff(17,d%17),moddiff(29,d%29),d**.5*((3**.5)-(1/(3**.5))))
print(grid_17_29)
grid_19_23=generate_grid2(moddiff(19,d%19),moddiff(23,d%23),d**.5*((3**.5)-(1/(3**.5))))
print(grid_19_23)

grid_2_53_19_23=generate_grid2(grid_2_53,grid_19_23,d**.5*((3**.5)-(1/(3**.5))))
print(grid_2_53_19_23[0])
grid_2_53=None
grid_19_23=None

grid_3_47_17_19=generate_grid2(grid_3_47,grid_17_29,d**.5*((3**.5)-(1/(3**.5))))
print(grid_3_47_17_19[0])
grid_3_47=None
grid_17_29=None

grid_5_43_13_31=generate_grid2(grid_5_43,grid_13_31,d**.5*((3**.5)-(1/(3**.5))))
print(grid_5_43_13_31[0])
grid_5_43=None
grid_13_31=None

grid_7_41_11_37=generate_grid2(grid_7_41,grid_11_37,d**.5*((3**.5)-(1/(3**.5))))
print(grid_7_41_11_37[0])
grid_7_41=None
grid_11_37=None

starttime=datetime.now()
grid1=generate_grid2(grid_2_53_19_23,grid_7_41_11_37,d**.5*((3**.5)-(1/(3**.5))))
endtime=datetime.now()
print('generate_grid2',endtime-starttime)
print(grid1)
grid_2_53_19_23=None
grid_7_41_11_37=None

starttime=datetime.now()
grid2=generate_grid2(grid_3_47_17_19,grid_5_43_13_31,d**.5*((3**.5)-(1/(3**.5))))
endtime=datetime.now()
print('generate_grid2',endtime-starttime)
print(grid2)
grid_3_47_17_19=None
grid_5_43_13_31=None

starttime=datetime.now()
grid=generate_grid2(grid1,grid2,d**.5*((3**.5)-(1/(3**.5))))
endtime=datetime.now()
print('generate_grid2',endtime-starttime)
print(grid)
'''
print(diophantine(30,17,41,11))  
print(diophantine(30,1,41,0))  
print(diophantine(30,0,41,1))  

#67297116731534860170