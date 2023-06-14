import primefac

#split binary into array of bits
def binarysplit(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

#extended GCD
def GCD(a, b):
    if a == 0: 
        return b, 0, 1
    gcd, s, t = GCD(b%a, a)
    y1 = s 
    x1 = t - (b//a) * s
    return gcd, x1, y1

#given a,b,c,d and a*x+b=c*y+d
#return flag,x,y
#flag 
#0:valid solution
#-1:infinite solutions
#-2:no solutions possible
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


#get differences from modulus factors
#for a divisor and modulus get the possible factors that can produce the modulus
#from the factors get the differences between the factors 
def modfactordiff(divisor,modulus):
    #initialise dictionary to return
    toreturn=set()
    
    #The multiple of the divisor
    multiple=0
    #print('divisor ',i,' modulus ',j)
    while (divisor*multiple+modulus<divisor**2):
        #candidate modulus product
        candidate=divisor*multiple+modulus
        #get prime factorisation of candidate
        primelist=list(primefac.primefac(candidate))
        #add 1 as a couple of factors even though 1 is not prime
        primelist.append(1)
        primelist.append(1)
        CandidatePasses=True
        #focus on factorising factors coprime with the test divisors 
        if GCD(candidate,divisor)[0]!=1:
            CandidatePasses=False
        if CandidatePasses:
            for eachprime in primelist:
                if eachprime>=divisor:
                    CandidatePasses=False
        #get the number of primes in the candidate prime factorisation
        lenlist=len(primelist)
        #use binary split of the list of primes
        #For each binary split of the prime list get the product of the partition
        partitionvalue=2**len(primelist)
        for partitionscheme in range(1,partitionvalue):
            partitionproduct=1
            scheme=binarysplit(partitionscheme)
            #print(partitionscheme,scheme)
            for pos in range(0,len(scheme)):
                if(scheme[pos]):
                    partitionproduct*=primelist[pos]
            
            if(partitionproduct<=divisor and candidate/partitionproduct<=divisor and CandidatePasses):
                #moddict[(i,j)].add((partitionproduct*candidate//partitionproduct,partitionproduct,candidate//partitionproduct))
                toreturn.add((divisor-partitionproduct+candidate//partitionproduct)%divisor)
                toreturn.add((divisor-candidate//partitionproduct+partitionproduct)%divisor)
        
        multiple+=1
    #print (toreturn)
    return toreturn

#Combine modfactordiff lists
def combinedifflists(firstdifflist,seconddifflist):
    #print('fs',firstdifflist,seconddifflist)
    returndifflistkey=firstdifflist[0]*seconddifflist[0]
    returndifflist=list()
    #returndifflist.append(0)
    #print('fs1',firstdifflist[1])
    #print('se1',seconddifflist[1])
    for firstdiff in firstdifflist[1]:
        for seconddiff in seconddifflist[1]:
            a=firstdifflist[0]
            b=firstdiff
            c=seconddifflist[0]
            d=seconddiff
            #diofresult=diophantine(firstdifflist[0],firstdiff,seconddifflist[0],seconddiff)
            diofresult=diophantine(a,b,c,d)
            #print('difresult',diofresult)
            #print(firstdifflist[0]*diofresult[1]+firstdiff,
            #      seconddifflist[0]*diofresult[2]+seconddiff)
            #print(a*diofresult[1]+b,
            #      c*diofresult[2]+d)
            if(diofresult[0]==0):
                #print(firstdifflist[0],firstdiff,seconddifflist[0],seconddiff,diofresult)
                returndifflist.append(a*diofresult[1]+b)
    #print(returndifflist)
    
    return(returndifflistkey,sorted(returndifflist))


#main
import json
import os

if __name__ == "__main__":
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
        while prime<30:
            for mod in range(1,prime):
                #print(prime,mod)
                if GCD(mod,prime)[0]==1:
                    #print(prime,mod)
                    #primelistdict[prime]['modlist'][mod]=list()
                    #print(primelistdict[prime]['modlist'][mod])
                    primelistdict[prime]['modlist'][mod]=sorted(modfactordiff(prime,mod))
            prime=next(primegenerator)
            if prime<30:
                primelistdict[prime]=dict()
                primelistdict[prime]['primelist']=[prime]
                primelistdict[prime]['modlist']=dict()
                
                
        #print(primedict)
        #print(primedict.keys())
        #print(combinedifflists((primedict[3][2]['mul'],primedict[3][2]['add']),(primedict[5][3]['mul'],primedict[5][3]['add'])))
        with open(primelistfilepath,'w') as saveprimelistdict:
            json.dump(primelistdict,saveprimelistdict)
    primelistdict=None
    if not os.path.exists(primelistfilepath):
        print('exiting as no prime list file found')
        exit(1)
    else:
        with open(primelistfilepath,'r') as readprimelistdict:
            primelistdict=json.load(readprimelistdict)
        #print(primelistdict)
        #switch to file#combineddict2=dict()
        central=dict()
        central['product']=1
        primelist=sorted(eval (i)  for i in primelistdict.keys())
        print(min(primelist))
        central['product']*=min(primelist)
        central['primelist']=list()
        central['primelist'].append(min(primelist))
        central['modlist']=dict()
        print('primelistdict2',primelistdict[str(2)])
        for key in primelistdict[str(min(primelist))]['modlist']:
            central['modlist'][key]=list()
            for element in primelistdict[str(min(primelist))]['modlist'][key]:
                central['modlist'][key].append(element)
        
        print('central',central)
        for i in primelist:
            if i!=2:
                
                central['primelist'].append(i)
                
        print(central)        



    """
        for prime1 in sorted(eval (i)  for i in primelistdict.keys()):
            #print('key',key)
            for prime2 in sorted(eval(j) for j in primelistdict.keys()):
                #print('key2',key2)
                if int(prime2)<=int(prime1):
                    continue
                if not os.path.exists(combinedlistpath):
                    os.mkdir(combinedlistpath)
                combinedlistfile=str(int(prime1)*int(prime2))+'_add_file.txt'
                filepath=os.path.join(combinedlistpath,combinedlistfile)
                if not os.path.exists(filepath):
                    #switch to file#combineddict2[int(prime1)*int(prime2)]=dict()
                    dicttowrite=dict()
                    #print('combineddict2',combineddict2)
                    #switch to file#combineddict2[int(prime1)*int(prime2)]['primelist']=[prime1,prime2]
                    dicttowrite['primelist']=[prime1,prime2]
                    #print('combineddict2',combineddict2)
                    #print(primelistdict[key])
                    #switch to file#combineddict2[int(prime1)*int(prime2)]['modlist']=dict()
                    dicttowrite['modlist']=dict()
                    for modkey1 in primelistdict[str(prime1)]['modlist'].keys():
                        #print('modkey',modkey)
                        for modkey2 in primelistdict[str(prime2)]['modlist'].keys():
                            #print('modkey2',modkey2)
                            
                            #switch to file#combineddict2[int(prime1)*int(prime2)]['modlist'][modkey1,modkey2]=list()
                            dicttowrite['modlist'][str(modkey1)+'_'+str(modkey2)]=list()
                            #print(primelistdict[key]['modlist'][modkey])
                            #print(primelistdict[key2]['modlist'][modkey2])
                            #switch to file#combineddict2[int(prime1)*int(prime2)]['modlist'][modkey1,modkey2]=combinedifflists((int(key),primelistdict[key]['modlist'][modkey]),(int(key2),primelistdict[key2]['modlist'][modkey2]))[1]
                            dicttowrite['modlist'][str(modkey1)+'_'+str(modkey2)]=combinedifflists((int(prime1),primelistdict[str(prime1)]['modlist'][modkey1]),(int(prime2),primelistdict[str(prime2)]['modlist'][modkey2]))[1]
        with open(filepath,'w') as savecombinedlistdict:
            json.dump(dicttowrite,savecombinedlistdict)
    #print(sorted(combineddict2[323]['modlist'].keys()))
    #print(combineddict2[13*17]['modlist']['3','7'])
    """    
    '''
    for diffmod in difflist.keys():
        for mod in range(1,prime):
            if GCD(mod,prime)[0]==1:
                difflist[diffmod][(prime,mod)]=dict()
                difflist[diffmod][(prime,mod)]['mul']=diffmod[0]*prime
                difflist[diffmod][(prime,mod)]['add']=combinedifflists(difflist[diffmod]['add'],)
    '''    