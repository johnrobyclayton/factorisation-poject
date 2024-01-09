import cupy as cp

# Define the arrays
array1 = []
array2 = []
for i in range(0, 10):
    for j in range(0, 10):
        array2.append(i * j)
    array1.append(array2)
    array2=[]

array3 = []
array4 = []
for i in range(0, 10):
    for j in range(0, 10):
        array4.append(i * j)
    array3.append(array4)
    array4=[]
# Convert lists to Cupy arrays
array1_gpu = cp.asarray(array1)
array3_gpu = cp.asarray(array3)
print(array1_gpu)
print(array3_gpu)
print(cp.shape(array1_gpu))
print(cp.shape(array3_gpu))

# Calculate the cross product on the GPU
cross_product_gpu = cp.add(array1_gpu, array3_gpu)

# Transfer the result back to the CPU if needed
cross_product_cpu = cp.asnumpy(cross_product_gpu)

print(cross_product_cpu)
