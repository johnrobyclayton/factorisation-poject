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

def generate_diagonalSequence2(p,q):
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
    while len(pp):
        p =pp.pop()
        qq=set(range(p,x))
        qfound=False
        while qfound==False and len(qq):
            q=qq.pop()
            if (p*q)%x==y:
                diffset.add(q-p)
                diffset.add(x-(q-p))
                pp.discard(p)
                pp.discard(q)
                qq.discard(q)
                qfound=True


    return((x,tuple(diffset)))

def generate_grid2(x, y):
    diagseq=generate_diagonalSequence2(x[0],y[0])
    diagseqdict=dict()
    for pair in diagseq:
        diagseqdict[pair[0]]=pair[1]
    splitcoords=split_coordinates(generate_coordinates(x,y))
    #print('diagseq',diagseq)
    #print('diagseqdict',diagseqdict)
    #print('splitcoords',splitcoords)
    grid=dict()
    gridsize=x[0]*y[0]
    grid[gridsize]=set()
    for diff in splitcoords.keys():
        #print('coords',splitcoords[diff])
        for coord in splitcoords[diff]:
            #print(coord,diff,diagseqdict[diff])
            grid[gridsize].add(diagseqdict[diff]+min(coord[0],coord[1]))
    return (gridsize,tuple(sorted(grid[gridsize])))


p=467
q=991
d=p*q
#print('generate_grid',generate_grid((5,[1,4]),(7,[1,3,4,6])))
#print('generate_coordinates',generate_coordinates((5,[1,4]),(7,[1,3,4,6])))
#print('generate_diagonalsequence',generate_diagonalSequence(5,7))
#print('split_coordinates',split_coordinates(generate_coordinates((5,[1,4]),(7,[1,3,4,6]))))
#print('generate_grid2',generate_grid2((5,[1,4]),(7,[1,3,4,6])))
#print('generate_grid2',generate_grid2((7,[1,3,4,6]),(5,[1,4])))
grid1=generate_grid(
        generate_grid(
            generate_grid(
                moddiff(2,d%2)
                ,moddiff(3,d%3)
            ),
            generate_grid(
                moddiff(5,d%5)
                ,moddiff(7,d%7)
            )
        ),
        generate_grid(
            generate_grid(
                moddiff(11,d%11)
                ,moddiff(13,d%13)
            ),
            generate_grid(
                moddiff(17,d%17)
                ,moddiff(19,d%19)
            )
        )
    )

print(grid1[0],grid1[1][1:10],grid1[1][-1:-10])
grid2=generate_grid2(
        generate_grid2(
            generate_grid(
                moddiff(2,d%2)
                ,moddiff(3,d%3)
            ),
            generate_grid(
                moddiff(5,d%5)
                ,moddiff(7,d%7)
            )
        ),
        generate_grid2(
            generate_grid(
                moddiff(11,d%11)
                ,moddiff(13,d%13)
            ),
            generate_grid(
                moddiff(17,d%17)
                ,moddiff(19,d%19)
            )
        )
    )

print(grid2[0],grid2[1][1:10],grid1[1][-1:-10])

'''
print(
    #generate_grid(
    generate_grid(
        generate_grid(
            generate_grid(
                moddiff(2,d%2)
                ,moddiff(3,d%3)
            ),
            generate_grid(
                moddiff(5,d%5)
                ,moddiff(7,d%7)
            )
        ),
        generate_grid(
            generate_grid(
                moddiff(11,d%11)
                ,moddiff(13,d%13)
            ),
            generate_grid(
                moddiff(17,d%17)
                ,moddiff(19,d%19)
            )
        )
    )
)
'''