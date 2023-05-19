import primefac
import pprint
print(list(primefac.primefac(2999999)))

def trans(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

pp=pprint.PrettyPrinter(indent=2)

moddict=dict()        
for i in (2*3*5,2*3*7):
    for j in range(1,i):
        moddict[(i,j)]=set()
        k=1
        #print('divisor ',i,' modulus ',j)
        while (i*k+j<i**2):
            candidate=i*k+j
            primelist=list(primefac.primefac(candidate))
            p=1
            for e in primelist:
                if e>=i:
                    p=0
            lenlist=len(primelist)
            #pp.pprint(primelist)
            partitionvalue=2**len(primelist)
            for partitionscheme in range(1,partitionvalue):
                partitionproduct=1
                scheme=trans(partitionscheme)
                #print(partitionscheme,scheme)
                for pos in range(0,len(scheme)):
                    if(scheme[pos]):
                        partitionproduct*=primelist[pos]
                if(partitionproduct<=i and candidate/partitionproduct<=i and p):
                    #moddict[(i,j)].add((partitionproduct*candidate//partitionproduct,partitionproduct,candidate//partitionproduct))
                    moddict[(i,j)].add((partitionproduct))
                    moddict[(i,j)].add(candidate//partitionproduct)
            k+=1

'''
delete = [key for key in moddict if len(moddict[key])>key[0]/4]
for key in delete:
    del moddict[key]
'''
#for key in ((2*3*5,144871%2*3*5),(2*3*7,144871%2*3*7)):
#    print(key,moddict[key])     
print(sorted(moddict[(30,144871%30)]))                
print(sorted(moddict[(42,144871%42)]))                
        
