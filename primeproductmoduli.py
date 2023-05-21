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

primegenerator = primegen()
#print(next(primegenerator))
d=27313427*53313461
rootd=(d**.5)//1
rootdthird=(rootd/3**.5)//1
primeproduct=1
listofkprimes=list()
listofkprimes.append(next(primegenerator))
primeproduct*=listofkprimes[-1]
while primeproduct < rootdthird:
    listofkprimes.append(next(primegenerator))
    primeproduct*=listofkprimes[-1]
#first=primegenerator.gi_frame.f_locals['listofprimes'][-1]
first=listofkprimes[-1]
start=primeproduct//first
print('first start',start,rootdthird-start,first,(rootdthird-start)/first)
multiplier=0
while(listofkprimes[multiplier]*start<rootdthird):
    multiplier+=1
multiplier-=1
start*=listofkprimes[multiplier]
print('second start',start,rootdthird-start,first,(rootdthird-start)/first)

listoflprimes=list()
listoflprimes.append(first)
#print (d,(d**.5)//1,(d**.5/3**.5)//1,primeproduct,first,primeproduct//first)
start=primeproduct//first
#print('try1',first)
if (d%(start+first)==0):
    print('factors found1:',start+first,d/(start+first))
nextp=next(primegenerator)
#print('try2',nextp)
listoflprimes.append(nextp)
while(d%(start+listoflprimes[-1])!=0 and (start+listoflprimes[-1])<rootd):
    #print('try3',nextp,(start+listoflprimes[-1]),rootd)
    nextp=next(primegenerator) 
    listoflprimes.append(nextp)
found=False
if d%(start+listoflprimes[-1])==0:
    print('factors found2:',start+nextp,d/(start+nextp),nextp)
    found=True
print('search2')
if found==False:
    for firstoneidx,firstone in enumerate(listoflprimes):
        for secondoneidx,secondone in enumerate(listoflprimes[firstoneidx+1:]):
            print('try4',firstoneidx,firstone,secondoneidx,secondone)
            if d%(start+firstone*secondone)==0:
                print('factors found3:',start+firstone*secondone,d/(start+firstone*secondone),firstone,secondone)
                found=True
            if (start+firstone*secondone)>rootd:
                print('try5',firstoneidx,firstone,secondoneidx,secondone)
                break
            if found:
                break
        if found:
            break












