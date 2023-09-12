def generate_grid(x, y):
    grid=dict()
    for n in range(0,int(x[0]*y[0])):
        if n%x[0] in x[1] and n%y[0] in y[1]:
            grid[(n%x[0],n%y[0])]=n
    return((x[0]*y[0],sorted(set(grid.values()))))


def generate_diagonalSequence(p,q):
    if q<p:
        temp=p
        p=q
        q=temp
    if p==q:
        return [(0,0)]
    start=0
    diag=0
    diagp=diag
    diagq=diag
    next=p
    nextd=p
    if next>0:
        diagp+=p
        diag=diagp
    elif next<0:
        diagq+=q
        diag=diagq
    returnlist=list()
    returnlist.append((start,diag))
    while next!=0:
        start=next
        returnlist.append((start,diag))
        if(p+start>q):
            next=start-q
        elif p+start<q:
            next=start+p
        elif p+start==q:
            next=0
        if next>0:
            diagp+=p
            diag=diagp
        elif next<0:
            diagq+=q
            diag=diagq
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
    

    

def generate_grid2(x, y):
    grid=dict()
    grid[x[0]*y[0]]=set()
    a=x[0]
    c=y[0]
    for b in x[1]:
        for d in y[1]:
            print('a',a,'b',b,'c',c,'d',d,'res',(((c*d)-b)/abs(a-c)))
            grid[a*c].add(a*(((c*d)-b)/abs(a-c))+b)
    return grid


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
p=467
q=991
d=p*q
print('generate_grid',generate_grid((5,[1,4]),(7,[1,3,4,6])))
print('generate_coordinates',generate_coordinates((5,[1,4]),(7,[1,3,4,6])))
print('generate_diagonalsequence',generate_diagonalSequence(5,7))
print('split_coordinates',split_coordinates(generate_coordinates((5,[1,4]),(7,[1,3,4,6]))))
'''
print(
    #generate_grid(
    generate_grid2(
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