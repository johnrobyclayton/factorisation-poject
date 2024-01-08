import numpy as np
import cupy as cp
import itertools

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


