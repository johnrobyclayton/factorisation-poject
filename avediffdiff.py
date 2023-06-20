def initialeo(n):
    return 4+8*n

def initialoe(n):
    return 8*n

def initialaccumeo(n):
    return 4*n+8*((n**2+n)//2)+3

def initialaccumoe(n):
    return 8*((n**2+n)//2)-3

def oetest(n):
    return n%4==1

def eotest(n):
    return n%4==3    

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x



if __name__ == "__main__":
    p=21345703
    q=12345701
    p=123456791
    q=233460431
    p=2134567907
    q=1234567891
    p=12345678923
    q=21345678929
    p=123456789133
    q=213456789127
    p=1234516789133
    q=2134516789127
    p=113
    q=43

    product=p*q
    start=int(((3**.5+1)*product**.5)/(3**.5*4)//1)
    if eotest(product):
        #print('its an even plus minus an odd')
        found=False
        
        #n=int((isqrt(product)/3**.5)//2)
        nplus=start+1
        nminus=start
        print(nplus,nminus)
        while not found:
            #print('even plus minus odd',(product-initialaccumeo(n))%initialeo(n))
            #print(product,product-initialaccumeo(n),initialaccumeo(n),initialeo(n))
            if (product-initialaccumeo(nplus))%initialeo(nplus) == 0:
                found=True
                adjust=(product-initialaccumeo(nplus))//initialeo(nplus)
                average=(nplus+1)*2+2*adjust
                diff=1+2*adjust
                print('eop',average-diff,'q',average+diff,'resultant',(average-diff)*(average+diff),'product',product,'nplus',nplus)
                if (average-diff)*(average+diff) != product:
                    found=False
            if (product-initialaccumeo(nminus))%initialeo(nminus) == 0 and not found:
                found=True
                adjust=(product-initialaccumeo(nminus))//initialeo(nminus)
                average=(nminus+1)*2+2*adjust
                diff=1+2*adjust
                print('eop',average-diff,'q',average+diff,'resultant',(average-diff)*(average+diff),'product',product,'nminus',nminus)
                if (average-diff)*(average+diff) != product:
                    found=False
            nplus+=1
            nminus-=1
    if oetest(product):
        #print('its an odd plus minus an even')
        found=False
        #n=int((isqrt(product)/3**.5)//2)
        nplus=start+1
        nminus=start
        print(nplus,nminus)
        while not found:
            #print('odd plus minus even')
            #print(product,product-initialaccumoe(n),initialaccumoe(n),initialeo(n-1),n)
            if(product-initialaccumoe(nplus))%initialeo(nplus-1)==0:
                found=True
                adjust=(product-initialaccumoe(nplus))//initialeo(nplus-1)
                average=nplus*2+1+2*adjust
                diff=2+2*adjust
                print('oep',average-diff,'q',average+diff,'resultant',(average-diff)*(average+diff),'product',product,'nplus',nplus)
                if (average-diff)*(average+diff) != product:
                    found=False
            if(product-initialaccumoe(nminus))%initialeo(nminus-1)==0 and not found:
                found=True
                adjust=(product-initialaccumoe(nminus))//initialeo(nminus-1)
                average=nminus*2+1+2*adjust
                diff=2+2*adjust
                print('oep',average-diff,'q',average+diff,'resultant',(average-diff)*(average+diff),'product',product,'nminus',nminus)
                if (average-diff)*(average+diff) != product:
                    found=False
            nplus+=1
            nminus-=1
