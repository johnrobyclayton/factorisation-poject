from datetime import datetime, timedelta
def generate_grid(x, y):
    grid=dict()
    for n in range(0,int(x[0]*y[0])):
        if n%x[0] in x[1] and n%y[0] in y[1]:
            grid[(n%x[0],n%y[0])]=n
    return((x[0]*y[0],sorted(set(grid.values()))))


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
    

    
def moddiff2(x,y):
    diffset=set()
    mulls=set()
    for i in range(1,x):
        for j in range(i,x):
            mulls.add((i,j))
    while len(mulls):
        nextmulls=set()
        candidate=mulls.pop()
        #print('candidate',candidate,'mulls',mulls)
        if (candidate[0]*candidate[1])%x==y:
            diffset.add((x+candidate[0]-candidate[1])%x)
            diffset.add((x+candidate[1]-candidate[0])%x)
            for pair in mulls:
                #print('pair',pair,'candidate',candidate)
                if not(pair[0]==candidate[0] or pair[0]==candidate[1] or pair[1]==candidate[0] or pair[1]==candidate[1]):
                    nextmulls.add(pair)
            mulls=nextmulls
        for pair in mulls:
            nextmulls.add(pair)
        #print('mulls',mulls)
        #print('nextmulls',nextmulls)
        #print('diffset',diffset)
        mulls=nextmulls
    return((x,tuple(sorted(diffset))))        
        
            
    
    



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
    starttime=datetime.now()
    diagseq=generate_diagonalSequence2(grid1[0],grid2[0],maxval)
    endtime=datetime.now()
    print('generate_diagonalsequnce',endtime-starttime)
    diagseqdict=dict()
    #convert ordered pairs into dict
    starttime=datetime.now()
    for pair in diagseq:
        diagseqdict[pair[0]]=pair[1]
    endtime=datetime.now()
    print('digseq conversion',endtime-starttime)
    #split the coordinates of the cros prod of the two grids into groups with the same difference between the second value minus the first value 
    starttime=datetime.now()
    splitcoords=split_coordinates(generate_coordinates(grid1,grid2))
    endtime=datetime.now()
    print('split coords',endtime-starttime)
    grid=dict()
    gridsize=grid1[0]*grid2[0]
    grid[gridsize]=set()
    starttime=datetime.now()
    for diff in splitcoords.keys():
        for coord in splitcoords[diff]:
            if diff in diagseqdict:
                if diagseqdict[diff]+min(coord[0],coord[1])<maxval:
                    grid[gridsize].add(diagseqdict[diff]+min(coord[0],coord[1]))
    endtime=datetime.now()
    print('forfor',endtime-starttime)
    return (gridsize,tuple(sorted(grid[gridsize])))


p=137
q=293
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

grid=generate_grid2(moddiff(2,d%2),moddiff(3,d%3),d**.5)
print(grid)

print(moddiff(5,d%5))
grid=generate_grid2(grid,moddiff(5,d%5),d**.5)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
grid=generate_grid2(grid,moddiff(7,d%7),d**.5)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
grid=generate_grid2(grid,moddiff(11,d%11),d**.5)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
grid=generate_grid2(grid,moddiff(13,d%13),d**.5)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
grid=generate_grid2(grid,moddiff(17,d%17),d**.5)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
grid=generate_grid2(grid,moddiff(19,d%19),d**.5)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
starttime=datetime.now()
grid=generate_grid2(grid,moddiff(23,d%23),d**.5)
endtime=datetime.now()
print('generate_grid2',endtime-starttime)
print(grid)
grid=(grid[0],tuple([i for i in grid[1] if i<d**.5]))
print(grid)
starttime=datetime.now()
print(moddiff(137,5))
endtime=datetime.now()
print('moddiff',endtime-starttime)
starttime=datetime.now()
print(moddiff2(137,5))
endtime=datetime.now()
print('moddiff2',endtime-starttime)
    