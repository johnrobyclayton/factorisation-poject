import numpy as np
import cupy as cp
import itertools

def isqrt(n):
    x = n
    #y = (x + 1) // 2
    y = (x + 1) >> 1
    while y < x:
        x = y
        #y = (x + n // x) // 2
        y = (x + n // x) >> 1
    return x

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
        #print(listofprimes)
        yield listofprimes[-1]

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
    if y==0:
        print('mod is zero, moddiff of a factor impossible')
        return((1,(0,)))
    diffset=set()
    pp=set(range(1,x))
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

def moddiffdict(d):
    #print('moddiffdict')
    primegenerator=primegen()
    toreturn1=list()
    toreturn2=list()
    primeproduct=1
    while not primeproduct>((d**(1/3))**2):
        
        prime=next(primegenerator)
        toreturn1.append(prime)
        #currentindex=len(toreturn)-1
        #toreturn[currentindex]["primeproduct"]=primeproduct
        toreturn2.append(list(sorted(moddiff(prime,d%prime)[1],reverse=True)))
        #toreturn[currentindex]['mod']=d%prime
        #toreturn[currentindex]["diafbase"]=diophantine_base(primeproduct,prime)
        #toreturn[currentindex]["accumulated"]=0
        #toreturn[currentindex]["diff"]=0
        #toreturn[currentindex]["maxp"]=0
        primeproduct*=prime
    return (toreturn1,toreturn2)

# Define a function for GPU computation
@cp.fuse()
def compute_mod_sum(arr, mod_value, max_value):
    return cp.sum(arr) % mod_value < max_value


prime1=13
prime2=23
product=prime1*prime2
#print('moddiff',list(moddiff(5,product%5)[1]))
mdifd=moddiffdict(product)
p_gpu=cp.array(mdifd[0])
mul=list()
primeprod=int(np.prod(p_gpu))
for i in p_gpu:
    base =primeprod//i
    while base%i!= 1:
        base+=base
    mul.append(base)
#print(mul)
#print(mdifd[0])
#print(mdifd[1])
#print(np.shape(mdifd[1]))
p_lists=mdifd[1]
diffarray_gpu = cp.array(list(itertools.product(*p_lists)), dtype=int)
#diffarray=np.array(list(itertools.product(tuple(mdifd[1]))),dtype=int)
#print(diffarray_gpu)

# Specify the mod values and maximum values
mod_values = cp.prod(cp.array(mdifd[0]))
#print(mod_values)
max_values = 10  # You can adjust this based on your requirements
# Create a Cupy array to store the filtered results


filtered_result_gpu = cp.zeros_like(diffarray_gpu, dtype=bool)

array1=list()
array2=list()
for i in range(0,10):
    for j in range(0,10):
        
        array2.append(i*j)
    array1.append(array2)
print(array1)
array3=list()
array4=list()
for i in range(0,10):
    for j in range(0,10):
        
        array4.append(i*j)
    array3.append(array2)
print(array3)

#print(filtered_result_gpu)
'''
# Perform the computation on the GPU asynchronously
with cp.cuda.Device(0):  # Adjust the GPU device index if needed
    stream = cp.cuda.Stream()
    
    # Filter the results asynchronously on the GPU
    with stream:
        cp.ElementwiseKernel(
            'T x', 'bool y', 'y = compute_mod_sum(x, mod_values, max_values)', 'filter_kernel'
        )(diffarray_gpu, filtered_result_gpu)

# Transfer the filtered result back to the CPU for further processing
filtered_result_cpu = cp.asnumpy(filtered_result_gpu)
'''

'''
p_gpu=cp.array([2,3,5,7])

p=[2,3,5,7]
p[0]=[1]
p[1]=[1,2]
p[2]=[0,1,4]
p[3]=[1,3,4,6]

diffarray=np.array(list(itertools.product(p[0],p[1],p[2],p[3])),dtype=int)


p_cpu=[2,3,5,7]
mul=[]
for i in p_cpu:
    base =np.prod(p_cpu)//i
    while base%i!= 1:
        base+=base
    mul.append(base)
print(mul)
print(mul*diffarray)
print(np.sum(mul*diffarray,axis=1))
print(sorted(np.sum(mul*diffarray,axis=1)%np.prod(p_cpu)))


# Define the primes and associated lists
p = [2, 3, 5, 7]
p_lists = [[1], [1, 2], [0, 1, 4], [1, 3, 4, 6]]

# Generate combinations using Cupy
diffarray_cpu = np.array(list(itertools.product(*p_lists)), dtype=int)
diffarray_gpu = cp.asarray(diffarray_cpu)

# Define a function for GPU computation
@cp.fuse()
def compute_mod_sum(arr, mod_value, max_value):
    return cp.sum(arr) % mod_value < max_value

# Specify the mod values and maximum values
mod_values = cp.prod(p)
max_values = 10  # You can adjust this based on your requirements

# Perform the computation on the GPU
filtered_result_gpu = cp.compress(
    compute_mod_sum(diffarray_gpu, mod_values, max_values),
    diffarray_gpu,
    axis=0,
)

# Transfer the result back to the CPU if needed
filtered_result_cpu = cp.asnumpy(filtered_result_gpu)

print(filtered_result_cpu)
import itertools
import numpy as np
import cupy as cp

# Define the primes and associated lists
p = [2, 3, 5, 7]
p_lists = [[1], [1, 2], [0, 1, 4], [1, 3, 4, 6]]

# Generate combinations using Cupy
diffarray_cpu = np.array(list(itertools.product(*p_lists)), dtype=int)
diffarray_gpu = cp.asarray(diffarray_cpu)

# Define a function for GPU computation
@cp.fuse()
def compute_mod_sum(arr, mod_value, max_value):
    return cp.sum(arr) % mod_value < max_value

# Specify the mod values and maximum values
mod_values = cp.prod(p)
max_values = 10  # You can adjust this based on your requirements

# Create a Cupy array to store the filtered results
filtered_result_gpu = cp.zeros_like(diffarray_gpu, dtype=bool)

# Perform the computation on the GPU asynchronously
with cp.cuda.Device(0):  # Adjust the GPU device index if needed
    stream = cp.cuda.Stream()
    
    # Filter the results asynchronously on the GPU
    with stream:
        cp.ElementwiseKernel(
            'T x', 'bool y', 'y = compute_mod_sum(x, mod_value, max_value)', 'filter_kernel'
        )(diffarray_gpu, filtered_result_gpu)

# Transfer the filtered result back to the CPU for further processing
filtered_result_cpu = cp.asnumpy(filtered_result_gpu)

# Continue with the remaining computations on the GPU

# Synchronize the CPU and GPU to ensure all asynchronous operations are complete
cp.cuda.Stream.null.synchronize()

# Further processing on the CPU with the filtered results
cpu_result = diffarray_cpu[filtered_result_cpu]

print(cpu_result)
'''